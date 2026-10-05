#!/usr/bin/env python3
"""Generate the Python AI Crash Course repository from the original class folders.

    python scripts/build.py \
        --src "/path/to/Hello Python" \
        --ai-pdf "/path/to/AI-Terms-Explained.pdf" \
        --chapters "/path/to/chapters.txt" \
        --repo /path/to/python-ai-crash-course

Requires: pip install -r scripts/requirements.txt
Only generated files are rewritten. `.git` and `scripts/` are never touched.
Everything is verified at the end: notebooks validate, assignment solutions pass their
checks (and the blank starters fail them), every relative link resolves, and every
video chapter is mapped to a place in the repo.
"""
import argparse
import contextlib
import hashlib
import io
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote

import nbformat
import pymupdf
from nbformat import v4

sys.path.insert(0, str(Path(__file__).parent))
import ai_terms as ai  # noqa: E402
import assignments as asg  # noqa: E402
import curriculum as cur  # noqa: E402
import practice  # noqa: E402

VIDEO_ID = "J9BI0jGOds8"
VIDEO_URL = f"https://www.youtube.com/watch?v={VIDEO_ID}"
REPO_URL = "https://github.com/mayank953/python-ai-crash-course"
MAX_OUTPUT_CHARS = 20_000
GENERATED = ["python", "ai-concepts", "roadmap", "assignments", "README.md", "INDEX.md",
             "LICENSE", "CONTRIBUTING.md", ".gitignore", "requirements.txt",
             "part-1-python", "part-2-ai", "bonus"]   # last three: old layout, cleaned if present
SECTION_ORDER = [cur.SEC_SETUP, cur.SEC_TYPES, cur.SEC_OPS, cur.SEC_FLOW, cur.SEC_DS, cur.SEC_FUNC, cur.SEC_MORE]
ICON = {cur.PDF: "📄", cur.THEORY: "📘", cur.CODE: "💻", cur.EXERCISE: "✏️", cur.SCRIPT: "🐍"}
LABEL = {cur.PDF: "Whiteboard notes (PDF)", cur.THEORY: "Theory notebook",
         cur.CODE: "Code notebook", cur.EXERCISE: "Exercises", cur.SCRIPT: "Practice script"}
KERNEL = {"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"}


# ------------------------------------------------------------------ small helpers
def seconds(ts):
    parts = [int(p) for p in ts.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def vid(ts):
    """Markdown link to the video at a timestamp."""
    return f"[`{ts}`]({VIDEO_URL}&t={seconds(ts)}s)"


def gh_slug(title):
    """GitHub heading anchor: lowercase, drop punctuation, each space becomes a hyphen."""
    return re.sub(r"[^\w\s-]", "", title.lower()).strip().replace(" ", "-")


def folder_of(lesson):
    return f"python/{lesson.folder}"


def parse_chapters(path):
    chapters = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("-----"):
            break
        m = re.match(r"^(\d+:\d{2}(?::\d{2})?)\s+(.+)$", line.strip())
        if m:
            chapters.append((m.group(1), m.group(2)))
    return chapters


def clean_dir(root):
    for name in GENERATED:
        p = root / name
        if p.is_dir():
            shutil.rmtree(p)
        elif p.exists():
            p.unlink()


def finalize_nb(nb, seed):
    """Stable cell ids (keeps diffs small between rebuilds), then validate."""
    nb.nbformat, nb.nbformat_minor = 4, 5
    for i, c in enumerate(nb.cells):
        c["id"] = hashlib.md5(f"{seed}:{i}".encode()).hexdigest()[:8]
    nbformat.validate(nb)


# ------------------------------------------------------------------ copying lessons
def resolve(src_root, rel):
    base = src_root.parent if rel.startswith("OOPS Session/") else src_root
    return base / rel


def header_cell(lesson):
    """Markdown cell added to the top of every copied notebook."""
    if lesson.chapters:
        links = " · ".join(f"{vid(t)} {name}" for t, name in lesson.chapters)
        first = f"> 📺 **Watch:** {links}"
    else:
        first = ""
    heading = f"{lesson.num}. {lesson.title}" if lesson.num[0].isdigit() else lesson.title
    second = f"> 📂 **{heading}** · [lesson page](README.md) · [course home](../../README.md)"
    return v4.new_markdown_cell("\n".join(x for x in (first, second) if x))


def copy_notebook(src, dst, lesson, notes):
    nb = nbformat.read(src, as_version=4)
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream":
                text = "".join(out["text"]) if isinstance(out["text"], list) else out["text"]
                if len(text) > MAX_OUTPUT_CHARS:
                    first = text.splitlines()[0] if text.strip() else ""
                    out["text"] = (f"{first}\n... (output shortened: this loop printed {len(text.splitlines()):,} "
                                   "lines before it was interrupted)\n")
                    notes.append(f"shortened an oversized output in {src.name}")
    nb.cells.insert(0, header_cell(lesson))
    dst.parent.mkdir(parents=True, exist_ok=True)
    finalize_nb(nb, f"{lesson.folder}/{dst.name}")
    nbformat.write(nb, dst)


def copy_lesson(lesson, src_root, repo, notes):
    out_dir = repo / folder_of(lesson)
    for rel, new_name, _kind in lesson.files:
        src = resolve(src_root, rel)
        if not src.exists():
            raise FileNotFoundError(f"missing source for lesson {lesson.num}: {src}")
        dst = out_dir / new_name
        if src.suffix == ".ipynb":
            copy_notebook(src, dst, lesson, notes)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


# ------------------------------------------------------------------ tables
def lesson_row(lesson, base, blurb):
    video = vid(lesson.chapters[0][0]) if lesson.chapters else "—"
    links = " ".join(f"[{ICON[k]}]({base}{lesson.folder}/{n} \"{LABEL[k]}\")"
                     for _r, n, k in lesson.files if k != cur.SCRIPT)
    cells = [lesson.num, f"[{lesson.title}]({base}{lesson.folder}/)", video, links]
    if blurb:
        cells.insert(2, practice.LESSONS[lesson.num][0])
    return "| " + " | ".join(cells) + " |"


def lesson_tables(base, blurb=False):
    out = []
    head = "| # | Lesson | " + ("What you learn | " if blurb else "") + "Video | Files |"
    sep = "|---|--------|" + ("---------------|" if blurb else "") + "-------|-------|"
    for section in SECTION_ORDER:
        out += [f"### {section}", "", head, sep]
        out += [lesson_row(l, base, blurb) for l in cur.PART1 if l.section == section]
        out.append("")
    return "\n".join(out)


ICON_LEGEND = "📄 whiteboard notes (PDF) · 📘 theory notebook · 💻 code notebook · ✏️ exercises"

PARTS_OVERVIEW = """| Topic | Video range |
|-------|-------------|
| Python setup & basics | 0:00 to 51:57 |
| Data types, strings & type casting | 51:57 to 2:15:50 |
| Operators & string formatting | 2:15:50 to 3:28:43 |
| Conditionals & loops | 3:28:43 to 5:33:56 |
| Data structures | 5:33:56 to 8:41:36 |
| Functions & functional programming | 8:41:36 to 10:47:48 |
| AI concepts explained (21 terms) | 10:47:48 to 13:01:38 |"""


def chapter_overview(chapters):
    where = {}
    for l in cur.PART1:
        for t, _ in l.chapters:
            where.setdefault(t, []).append(f"[Lesson {l.num}](python/{l.folder}/)")
    for t in ai.TERMS:
        where.setdefault(t.ts, []).append(f"[{t.title}](ai-concepts/README.md#{gh_slug(t.title)})")
    where.setdefault(ai.INTRO_TS[0], []).append("[AI concepts overview](ai-concepts/README.md)")
    where.setdefault(ai.RECAP.ts, []).append(f"[Recap](ai-concepts/README.md#{gh_slug(ai.RECAP.title)})")
    where.setdefault(ai.FINAL_TS[0], []).append("[Final thoughts](ai-concepts/README.md#final-thoughts)")
    rows, missing = ["| Time | Chapter | In this repo |", "|------|---------|--------------|"], []
    for ts, title in chapters:
        if ts not in where:
            missing.append((ts, title))
            continue
        rows.append(f"| {vid(ts)} | {title} | {' · '.join(dict.fromkeys(where[ts]))} |")
    if missing:
        raise SystemExit(f"Chapters not mapped to a lesson or term: {missing}")
    return "\n".join(rows)


def assignment_rows(prefix):
    rows = ["| Checkpoint | After lessons | Problems | Starter | Solutions |", "|---|---|---|---|---|"]
    for a in asg.ASSIGNMENTS:
        rows.append(f"| {a['title'].split(': ', 1)[1]} | {a['lessons']} | {len(a['problems'])} | "
                    f"[notebook]({prefix}{a['id']}.ipynb) | [solutions]({prefix}solutions/{a['id']}.ipynb) |")
    return "\n".join(rows)


def resource_rows():
    rows = ["| Resource | What it is | Use it for | Chapter |", "|---|---|---|---|"]
    for label, url, what, _how, ts, term in ai.RESOURCE_GUIDE:
        rows.append(f"| [{label}]({url}) | {what} | {term} | {vid(ts)} |")
    return "\n".join(rows)


# ------------------------------------------------------------------ lesson pages
def lesson_page(lesson, prev_l, next_l):
    L = [f"# {lesson.num}. {lesson.title}", ""]
    blurb, tasks = practice.LESSONS[lesson.num]
    L += [blurb, ""]
    if lesson.chapters:
        L += ["**Watch**", ""] + [f"- {vid(t)} {name}" for t, name in lesson.chapters] + [""]
    if lesson.num in ("37", "38"):
        L += ["> Lessons 37 and 38 together span the chapters from `8:41:36` to `9:10:11`.", ""]
    L += ["**Files**", "", "| File | What it is |", "|---|---|"]
    L += [f"| {ICON[k]} [`{n}`]({n}) | {LABEL[k]} |" for _r, n, k in lesson.files]
    L += ["", "**Try it yourself**", ""] + [f"{i}. {t}" for i, t in enumerate(tasks, 1)] + [""]
    for a in asg.ASSIGNMENTS:
        if a["after"] == lesson.num:
            L += [f"🎯 **Checkpoint:** that completes a section. Test yourself with "
                  f"[{a['title']}](../../assignments/{a['id']}.ipynb) "
                  f"(solutions: [here](../../assignments/solutions/{a['id']}.ipynb)).", ""]
    nav = []
    if prev_l:
        nav.append(f"[← {prev_l.num} {prev_l.title}](../{prev_l.folder}/)")
    nav.append("[Course home](../../README.md)")
    if next_l:
        nav.append(f"[{next_l.num} {next_l.title} →](../{next_l.folder}/)")
    return "\n".join(L + ["---", " · ".join(nav), ""])


def part1_readme():
    return "\n".join([
        "# Python: Complete All Resources", "",
        "46 lessons in order. Each lesson folder holds the whiteboard PDF, a theory notebook, "
        "a code notebook and sometimes exercises, plus a README with the video timestamps and three small tasks.", "",
        f"Legend: {ICON_LEGEND}", "", lesson_tables("", blurb=True),
        "### Checkpoint assignments", "", assignment_rows("../assignments/"), "", "[Course home](../README.md)", ""])


# ------------------------------------------------------------------ AI pages
def extract_ai_images(pdf_path):
    doc = pymupdf.open(pdf_path)
    infos = sorted(doc[0].get_image_info(xrefs=True), key=lambda i: (round(i["bbox"][1]), round(i["bbox"][0])))
    out = {}
    for n, info in enumerate(infos, 1):
        img = doc.extract_image(info["xref"])
        out[f"{n:02d}"] = (img["image"], "jpg" if img["ext"] == "jpeg" else img["ext"])
    return out


def write_ai_images(by_index, dest):
    dest.mkdir(parents=True, exist_ok=True)
    names = {}
    for idx, fname, _alt in ai.COVER_CARDS:
        data, ext = by_index[idx]
        names[idx] = Path(fname).with_suffix("." + ext).name
        (dest / names[idx]).write_bytes(data)
    for t in list(ai.TERMS) + [ai.RECAP]:
        for i, (idx, _alt) in enumerate(t.cards):
            data, ext = by_index[idx]
            names[idx] = f"{t.key}{'' if i == 0 else '-' + str(i + 1)}.{ext}"
            (dest / names[idx]).write_bytes(data)
    return names


def term_block(t, names):
    L = [f"### {t.title}", "", f"{vid(t.ts)} · *{t.tagline}*", ""]
    for idx, alt in t.cards:
        L += [f"![{alt}](images/{names[idx]})", ""]
    L += [t.summary, ""] + [f"- {p}" for p in t.points] + [""]
    if t.key in ai.ACTIVITIES:
        L += [f"**Try it:** {ai.ACTIVITIES[t.key]}", ""]
    if t.links:
        L += ["**Resources:** " + " · ".join(f"[{a}]({b})" for a, b in t.links), ""]
    return L


def ai_readme(names):
    L = ["# AI Concepts Explained", "",
         f"Video: {vid(ai.INTRO_TS[0])} to `13:01:38`. **21 terms in 5 stages**, from the chat window you already use "
         "to what comes next.", "", f"![{ai.COVER_CARDS[0][2]}](images/{names['01']})", "",
         "There is no code in this part. The goal is a working vocabulary, so that when someone says "
         "*context window*, *RAG* or *MCP* you know what they mean and why it matters. Every term has a card from the "
         "course diagram, a short explanation, one hands-on activity, and links to the tools used in the video.", "",
         "**Study materials**", "",
         "- [`ai-terms-explained.pdf`](ai-terms-explained.pdf): the full diagram from the video",
         f"- [{ai.R_AI_TERMS[0]}]({ai.R_AI_TERMS[1]}): the interactive version",
         "- [Quiz](#quiz): twelve questions to test yourself", "",
         f"![{ai.COVER_CARDS[1][2]}](images/{names['02']})", "", "## Contents", ""]
    for s, (title, _blurb) in ai.STAGES.items():
        terms = [t for t in ai.TERMS if t.stage == s] + ([ai.RECAP] if s == 5 else [])
        L += [f"**Stage {s}: {title}**  ", " · ".join(f"[{t.title}](#{gh_slug(t.title)})" for t in terms), ""]
    L += ["**Also:** [Resources explained](#resources-explained) · [Quiz](#quiz)", ""]
    for s, (title, blurb) in ai.STAGES.items():
        L += ["---", "", f"## Stage {s}: {title}", "", f"*{blurb}*", ""]
        for t in [t for t in ai.TERMS if t.stage == s]:
            L += term_block(t, names)
        if s == 5:
            L += term_block(ai.RECAP, names)
    L += ["---", "", "## Final thoughts", "",
          f"{vid(ai.FINAL_TS[0])} {ai.FINAL_TS[1]}: close the loop and decide where to go next.", "",
          "## Resources explained", "",
          "Every link used in the video, what it is, and how to get value from it in a few minutes.", ""]
    for label, url, what, how, ts, term in ai.RESOURCE_GUIDE:
        L += [f"### [{label}]({url})", "", f"{what} Related chapter: {vid(ts)} ({term}).", "", "How to use it:", ""]
        L += [f"{i}. {h}" for i, h in enumerate(how, 1)] + [""]
    L += ["> Some of these sites block automated link checkers. If a link does not open for you, search for its title.",
          "", "## Quiz", "", "Try to answer before opening the answer.", ""]
    for i, (q, a) in enumerate(ai.QUIZ, 1):
        L += [f"<details><summary><b>{i}.</b> {q}</summary>", "", a, "", "</details>", ""]
    return "\n".join(L + ["[Course home](../README.md)", ""])


# ------------------------------------------------------------------ assignments
def run_cells(ns, cells):
    """Run code strings in a shared namespace; return captured stdout for each."""
    outs = []
    for src in cells:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exec(compile(src, "<cell>", "exec"), ns)
        outs.append(buf.getvalue())
    return outs


def verify_assignments():
    """Every solution passes its check; every blank starter fails it."""
    count = 0
    for a in asg.ASSIGNMENTS:
        ns = {}
        for n, p in enumerate(a["problems"], 1):
            count += 1
            try:
                run_cells(dict(ns), [p["starter"], p["check"]])
            except BaseException:
                pass
            else:
                raise SystemExit(f"{a['id']} problem {n}: blank starter unexpectedly PASSES its check")
            try:
                run_cells(ns, [p["solution"], p["check"]])
            except BaseException as exc:
                raise SystemExit(f"{a['id']} problem {n}: solution FAILS its check: {exc!r}")
    return count


def build_assignments(repo):
    a_dir = repo / "assignments"
    s_dir = a_dir / "solutions"
    s_dir.mkdir(parents=True, exist_ok=True)
    for a in asg.ASSIGNMENTS:
        for solved in (False, True):
            nb = v4.new_notebook()
            nb.metadata["kernelspec"] = KERNEL
            nb.metadata["language_info"] = {"name": "python"}
            up = "../../" if solved else "../"
            nb.cells.append(v4.new_markdown_cell(
                f"> 📂 **{a['title']}** · [assignments]({'../' if solved else ''}README.md) · [course home]({up}README.md)"))
            body = ("Compare with your own attempt. Try each problem yourself first!" if solved else
                    "Replace each `...` with your code, run the cell, then run the check cell below it. "
                    "A green tick means you passed. Reference solutions are in the `solutions` folder, but try first.")
            nb.cells.append(v4.new_markdown_cell(
                f"# {a['title']}{' (Solutions)' if solved else ''}\n\n**Covers:** {a['lessons']}\n\n{a['intro']}\n\n{body}"))
            ns, counter = {}, 1
            for n, p in enumerate(a["problems"], 1):
                nb.cells.append(v4.new_markdown_cell(f"## Problem {n}: {p['title']}\n\n{p['prompt']}"))
                code = p["solution"] if solved else p["starter"]
                check = p["check"] + f"\nprint('✅ Problem {n} passed')"
                cell, chk = v4.new_code_cell(code), v4.new_code_cell(check)
                if solved:
                    for c, out in zip((cell, chk), run_cells(ns, [code, check])):
                        c.execution_count = counter
                        counter += 1
                        if out:
                            c.outputs = [v4.new_output("stream", name="stdout", text=out)]
                nb.cells += [cell, chk]
            finalize_nb(nb, f"{a['id']}:{solved}")
            nbformat.write(nb, (s_dir if solved else a_dir) / f"{a['id']}.ipynb")
    (a_dir / "README.md").write_text(
        "# Checkpoint assignments\n\nOne assignment at the end of each section of the Python lessons. Each problem gives you a blank "
        "to fill, a check cell that tells you whether you got it right, and a reference solution.\n\n"
        + assignment_rows("") + "\n\n**How to use:** finish the lessons in the section, open the assignment notebook, "
        "solve the problems in order, and only then look at the solutions.\n\n[Course home](../README.md)\n",
        encoding="utf-8")


# ------------------------------------------------------------------ index and top-level docs
def index_page():
    L = ["# Complete index", "", "Every file in the repository and every external link, in one place.", "",
         "## Lessons and files", "", "| Lesson | File | Type | Video |", "|---|---|---|---|"]
    for l in cur.PART1:
        video = vid(l.chapters[0][0]) if l.chapters else "—"
        for _r, name, kind in l.files:
            L.append(f"| {l.num} {l.title} | [{name}]({folder_of(l)}/{name}) | {ICON[kind]} {LABEL[kind]} | {video} |")
    L += ["", "## Assignments", "", "| Notebook | Type |", "|---|---|"]
    for a in asg.ASSIGNMENTS:
        L.append(f"| [{a['id']}](assignments/{a['id']}.ipynb) | ✏️ Assignment |")
        L.append(f"| [{a['id']} (solutions)](assignments/solutions/{a['id']}.ipynb) | ✅ Solutions |")
    L += ["", "## AI section", "", "| File | What it is |", "|---|---|",
          "| [ai-concepts/README.md](ai-concepts/README.md) | 21 terms, activities, resource guide, quiz |",
          "| [ai-concepts/ai-terms-explained.pdf](ai-concepts/ai-terms-explained.pdf) | The full diagram from the video |",
          "| [ai-concepts/images/](ai-concepts/images/) | One card image per term |", "",
          "## External resources", "", resource_rows(), "",
          "## Video", "", f"- [Full course on YouTube]({VIDEO_URL})", "", "[Course home](README.md)", ""]
    return "\n".join(L)


def stage_table():
    rows = ["| Stage | Terms |", "|---|---|"]
    for s, (title, _b) in ai.STAGES.items():
        terms = [t for t in ai.TERMS if t.stage == s] + ([ai.RECAP] if s == 5 else [])
        names = ", ".join(f"[{t.title}](ai-concepts/README.md#{gh_slug(t.title)})" for t in terms)
        rows.append(f"| {s}. {title} | {names} |")
    return "\n".join(rows)


def main_readme(chapters, n_files, n_pdf):
    thumb = f"https://img.youtube.com/vi/{VIDEO_ID}/maxresdefault.jpg"
    return f"""# Python AI Crash Course

[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch%20the%20course-red?logo=youtube&logoColor=white)]({VIDEO_URL})
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Learn Python from zero, then understand the AI vocabulary behind tools like ChatGPT and Claude.**
This repository holds every note, notebook and practice file for the 13-hour course.

> 🧭 **New to AI? [Follow the roadmap](roadmap/README.md)** for the best order to learn Python and AI from scratch.

[![Course video]({thumb})]({VIDEO_URL})

## Contents

- [AI roadmap for beginners](roadmap/README.md)
- [What you will learn](#what-you-will-learn)
- [Start here](#start-here)
- [How each lesson works](#how-each-lesson-works)
- [Course outline](#course-outline) · [Chapter overview](#chapter-overview)
- [Python: Complete All Resources](#python-complete-all-resources) · [Checkpoint assignments](#checkpoint-assignments)
- [AI Concepts](#ai-concepts) · [Resources explained](#resources-explained)
- [Repository layout](#repository-layout) · [FAQ](#faq)

## What you will learn

**Python:** install Python and Jupyter, variables and data types, strings and slicing, operators,
if/else decisions, loops, lists, tuples, sets and dictionaries, functions up to `lambda`, `map`, `filter` and `reduce`, plus exception handling and object-oriented programming.

**AI concepts:** 21 core terms in 5 stages, from *LLM*, *prompting* and *temperature* through *tokens*, *attention* and
*transformers*, to *RAG*, *MCP*, *agents* and *reasoning models*.

**Who it is for:** complete beginners. You need a computer and curiosity, nothing else.

## Start here

1. **Watch** the [course on YouTube]({VIDEO_URL}). Use the chapter links below to jump to a topic.
2. **Get the files:** click *Code*, then *Download ZIP* (or use `git clone`).
3. **Set up** Python and Jupyter (below), then open the lesson folder that matches the chapter.
4. **Not sure where to begin?** Follow the [roadmap](roadmap/README.md).

### Set up in five minutes

You need Python 3.9 or newer.

```bash
git clone {REPO_URL}.git
cd python-ai-crash-course
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
jupyter lab
```

Prefer Anaconda? Install it (shown at {vid('20:31')} in the video), run `jupyter notebook` in the repo folder and open any `.ipynb`.
No install at all? Upload a notebook to [Google Colab](https://colab.research.google.com/).
The notebooks only use the Python standard library.

## How each lesson works

Every lesson folder in [`python/`](python/) follows the same pattern:

| Step | File | What to do |
|---|---|---|
| 1 | Video | Watch the chapter (timestamps are linked in each lesson). |
| 2 | 📄 `whiteboard-notes.pdf` | The notes drawn during the lesson. Skim before or after the video. |
| 3 | 📘 `theory.ipynb` | A written explanation with small examples. Read it. |
| 4 | 💻 `code.ipynb` | The code from class. **Run it and change the values** to see what happens. |
| 5 | ✏️ `exercises*.ipynb` | Practice questions (where available). |
| 6 | 🎯 Try it yourself | Three small tasks in each lesson README. |
| 7 | 🎯 Checkpoint assignment | At the end of every section, with automatic checks. |

Each notebook starts with a banner linking to its video chapter, so the reference is always one click away.

## Course outline

{PARTS_OVERVIEW}

## Chapter overview

All {len(chapters)} chapters of the video, with the place in this repository that matches each one.

<details>
<summary><b>Show the full chapter table</b></summary>

{chapter_overview(chapters)}

</details>

## Python: Complete All Resources

{ICON_LEGEND}

Hover over an icon to see what it is. Each lesson title opens its own page with timestamps and tasks.

{lesson_tables("python/")}
### Checkpoint assignments

Test yourself at the end of every section. Each problem has a check cell that tells you instantly whether you got it right.

{assignment_rows("assignments/")}

## AI Concepts

The second half of the course explains **21 AI terms in 5 stages**. There is no code; the goal is to understand the language
of AI. Everything lives in [`ai-concepts/`](ai-concepts/README.md): one card per term from the course diagram, a short
explanation, a hands-on activity, a quiz, and the full diagram as a [PDF](ai-concepts/ai-terms-explained.pdf).

![The Complete AI Vocabulary map](ai-concepts/images/vocabulary-map.jpg)

{stage_table()}

### Resources explained

The video uses a handful of tools and articles. Here is what each one is and when to use it
(step-by-step guides are in the [AI section](ai-concepts/README.md#resources-explained)).

{resource_rows()}

> Some of these sites block automated link checkers. If one does not open, search for its title.

## Repository layout

```
python-ai-crash-course/
├── README.md                 you are here
├── INDEX.md                  every file and link in one table
├── requirements.txt          jupyterlab
├── roadmap/
│   └── README.md             the beginner roadmap for learning Python and AI
├── python/
│   ├── README.md             lesson list with summaries
│   └── NN-topic/             one folder per lesson
│       ├── README.md         timestamps, files, tasks
│       ├── whiteboard-notes.pdf
│       ├── theory.ipynb
│       └── code.ipynb
├── assignments/              six checkpoint assignments
│   └── solutions/
├── ai-concepts/
│   ├── README.md             21 terms, activities, resources, quiz
│   ├── ai-terms-explained.pdf
│   └── images/
└── scripts/                  maintainer tooling (learners can ignore)
```

The complete list of files and links is in [INDEX.md](INDEX.md).
The repo holds {n_files} notebooks and scripts and {n_pdf} PDFs.

## FAQ

**A notebook looks odd on GitHub.** Download the repo and open it locally with Jupyter for the best experience.

**`python` is not found.** On macOS and Linux use `python3`. On Windows try `py`.

**Which file do I open first in a lesson?** Watch the video, then `theory.ipynb`, then `code.ipynb`.

**Do I need an AI account for the AI concepts?** No. The activities work with any free chatbot, and the tools are free websites.

**I got stuck or found a mistake.** Open an [issue]({REPO_URL}/issues) with the lesson number and what happened.

## Contributing

Corrections and clearer explanations are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the [MIT License](LICENSE). Created by **Mayank Aggarwal**. If this helped you, star the repo and
share the [video]({VIDEO_URL}) with a friend who is starting out.
"""


LICENSE = """MIT License

Copyright (c) 2026 Mayank Aggarwal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

CONTRIBUTING = """# Contributing

Thanks for helping learners! The most useful contributions are:

- **Typos and wrong explanations** in notebooks or READMEs.
- **Broken links** (please say which page and which link).
- **New practice questions** for a lesson, ideally with a short solution.

## How

1. Open an issue describing the problem and naming the lesson (for example "Lesson 27: lists").
2. For small fixes, open a pull request that changes only the file concerned.
3. Keep notebooks runnable from top to bottom using only the standard library.

## A note on the `scripts/` folder

The lesson pages, tables and assignment notebooks are produced by `scripts/build.py` from the original class files, so the
text and links stay consistent. If you change a README by hand, mention it in your pull request and the maintainer will
carry the change into the generator.
"""


# ------------------------------------------------------------------ roadmap
def roadmap_readme():
    def lf(num):
        l = next(x for x in cur.PART1 if x.num == num)
        return f"../python/{l.folder}/"

    def span(a, b):
        return f"[lessons {a} to {b}]({lf(a)})"

    ac = "../ai-concepts/README.md"
    return f"""# AI Roadmap for Beginners

**Follow this roadmap to get started in AI if you are new.** You do not need a degree, a powerful computer or a maths
background. You need a sensible order to learn things in, and this page gives you one, with every step linked to
material in this repository.

> **In one line:** learn Python basics, learn the language of AI, learn to prompt and give context well, build small
> things with code, then grow into RAG, tools and agents.

[Back to the course home](../README.md)

## Why start with Python

- **It reads like plain English.** You spend your time on ideas, not on punctuation, so you get working programs quickly.
- **AI tooling is Python-first.** Most tutorials, libraries and example code for working with AI models are written in
  Python, so the skill you build here keeps paying off.
- **It is useful beyond AI.** The same basics carry over to automation, data work and web projects.
- **You stay in control.** Even if you mostly use AI tools, Python lets you automate boring tasks and read and check the
  code an assistant writes for you, instead of treating it as magic.
- **Errors stop being scary.** Once you can read a traceback, debugging, with or without an AI helper, becomes routine.

## Why learn the vocabulary of AI

- **You will hear the words everywhere.** Tokens, context window, RAG, MCP and agents appear on every product page.
  Knowing them lets you judge what a claim really means.
- **You get better results.** Temperature, prompting and context change the answers you receive.
- **You avoid costly surprises.** Understanding tokens and hallucination helps with both cost and trust.
- **You choose the right tool.** Should you prompt better, retrieve documents (RAG), fine-tune, or build an agent?
  The vocabulary is how you decide.

## The roadmap at a glance

| Stage | Goal | Start here | Suggested pace* |
|---|---|---|---|
| 1 | Python basics | {span('01', '16')} | 1 to 2 weeks |
| 2 | Decisions and loops | {span('17', '25')} | about 1 week |
| 3 | Data structures | {span('26', '36')} | 1 to 2 weeks |
| 4 | Functions | {span('37', '44')} | about 1 week |
| 5 | Speak the language of AI | [AI concepts]({ac}) | 3 to 5 days |
| 6 | Use AI well | [Prompting and context]({ac}#prompting) | ongoing |
| 7 | Build with AI | Mini projects below | 2 to 4 weeks |
| 8 | Keep growing | Pick one project and ship it | ongoing |

\\*A suggestion for about an hour of study a day. Go faster or slower; finishing matters more than speed.

---

## Stage 1: Python basics

**Goal:** install Python, run code, and work with numbers, text and operators.

- Do: {span('01', '16')}. Start with [installing Python]({lf('02')}).
- Test yourself: [Checkpoint 1](../assignments/A1-setup-and-basics.ipynb), [Checkpoint 2](../assignments/A2-types-strings-casting.ipynb)
  and [Checkpoint 3](../assignments/A3-operators-formatting.ipynb).
- **Mini projects:** a tip calculator, a unit converter, a "format my name" helper.
- **You are ready to move on when** you can store values in variables, slice a string, and print tidy output with f-strings.

## Stage 2: Decisions and loops

**Goal:** make your programs choose and repeat.

- Do: {span('17', '25')}.
- Test yourself: [Checkpoint 4](../assignments/A4-conditionals-loops.ipynb).
- **Mini projects:** a number-guessing game, a multiplication-table printer, a password-strength checker.
- **You are ready to move on when** you can read a loop and predict what it prints before running it.

## Stage 3: Data structures

**Goal:** organise information with lists, tuples, sets and dictionaries.

- Do: {span('26', '36')}.
- Test yourself: [Checkpoint 5](../assignments/A5-data-structures.ipynb).
- **Mini projects:** a contact book with a dictionary, a to-do list, a word-frequency counter.
- **You are ready to move on when** you can pick the right structure for a problem and explain why.

## Stage 4: Functions

**Goal:** package code so you can reuse it, and meet the functional tools used everywhere in Python.

- Do: {span('37', '44')}.
- Test yourself: [Checkpoint 6](../assignments/A6-functions.ipynb).
- When you want to write larger programs, continue with [exception handling]({lf('45')}) and [object-oriented programming]({lf('46')}).
- **Mini projects:** turn your earlier projects into functions, build a small text-cleaning toolkit with `map` and `filter`.
- **You are ready to move on when** you can write a function with default and keyword arguments and explain what it returns.

## Stage 5: Speak the language of AI

**Goal:** understand the 21 core terms well enough to explain them to a friend.

- Do: the [AI concepts guide]({ac}), one stage at a time, with the card images and the activity under each term.
- Try the tools: the [tokenizer, temperature visualizer and Transformer Explainer]({ac}#resources-explained).
- Test yourself: the [quiz]({ac}#quiz).
- **Mini project:** write a one-page glossary in your own words, then explain RAG to someone who has never heard of it.

## Stage 6: Use AI well

**Goal:** get reliably good answers instead of lucky ones.

- Practise **prompting**: compare a zero-shot prompt with a few-shot one on the same task.
- Practise **context**: give the model the background it needs, not just a question.
- Always **verify**: treat a confident answer as a draft, especially for facts, numbers and citations.
- **Mini project:** turn a task you do every week into a reusable prompt template.

## Stage 7: Build with AI

**Goal:** move from using AI to building with it, using the Python you now know.

1. **Call a model from code.** Use a provider's official documentation to send text to a model and print the reply.
2. **Give it your own documents (RAG).** Build a small "chat with my notes" script that retrieves the right passage first.
3. **Give it tools.** Let a model call a function you wrote, for example a calculator or a file reader. This is the idea behind MCP.
4. **Make it loop.** Combine tools and a goal into a tiny agent that perceives, reasons, acts and checks.

Keep each project small and finish it before starting the next.

## Stage 8: Keep growing

- Pick **one** project you care about and ship it, however small.
- Share it, write down what you learned, and ask for feedback.
- Return to the [lesson pages](../python/README.md) whenever a concept feels shaky.

## Habits that make this work

1. **Type the code yourself.** Pasting teaches far less than typing.
2. **Do the "Try it yourself" tasks** in every lesson before moving on.
3. **Break things on purpose** and read the error message slowly.
4. **Use an AI chatbot as a tutor, not an answer machine:** ask it to explain your error or quiz you before asking for a full solution.
5. **Study a little every day** rather than in rare marathons.
6. **Keep a notes file** of new terms and the one-line meaning you understood.

## Common mistakes

- Watching without coding along.
- Jumping to agents and frameworks before the Python basics feel comfortable.
- Trusting AI output without checking it.
- Waiting until you feel "ready" to build something.
- Skipping errors instead of reading them.

[Back to the course home](../README.md) · [Start with lesson 01]({lf('01')})
"""


# ------------------------------------------------------------------ verification
def verify_links(repo):
    broken, total = [], 0
    for md in repo.rglob("*.md"):
        if "scripts" in md.relative_to(repo).parts:
            continue
        text = md.read_text(encoding="utf-8")
        for m in re.finditer(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text):
            target = m.group(1)
            if re.match(r"(https?:|mailto:)", target):
                continue
            total += 1
            path_part, _, anchor = target.partition("#")
            dest = md if not path_part else (md.parent / unquote(path_part))
            if not dest.exists():
                broken.append((str(md.relative_to(repo)), target))
            elif anchor and dest.suffix == ".md":
                heads = re.findall(r"^#{1,6} (.+?)\s*$", dest.read_text(encoding="utf-8"), re.M)
                slugs = {gh_slug(re.sub(r"\[(.*?)\]\(.*?\)", r"\1", h)) for h in heads}
                if anchor not in slugs:
                    broken.append((str(md.relative_to(repo)), target))
    for nb_path in repo.rglob("*.ipynb"):
        nb = nbformat.read(nb_path, as_version=4)
        nbformat.validate(nb)
        for m in re.finditer(r"\]\(([^)\s]+)\)", nb.cells[0].source):
            t = m.group(1)
            if t.startswith("http"):
                continue
            total += 1
            if not (nb_path.parent / t).exists():
                broken.append((str(nb_path.relative_to(repo)), t))
    return total, broken


# ------------------------------------------------------------------ main
def build(a):
    src, repo = Path(a.src), Path(a.repo)
    repo.mkdir(parents=True, exist_ok=True)
    clean_dir(repo)
    chapters = parse_chapters(a.chapters)
    notes = []

    lessons = cur.PART1
    for i, l in enumerate(lessons):
        copy_lesson(l, src, repo, notes)
        page = lesson_page(l, lessons[i - 1] if i else None, lessons[i + 1] if i + 1 < len(lessons) else None)
        (repo / folder_of(l) / "README.md").write_text(page, encoding="utf-8")
    (repo / "python" / "README.md").write_text(part1_readme(), encoding="utf-8")

    (repo / "roadmap").mkdir(exist_ok=True)
    (repo / "roadmap" / "README.md").write_text(roadmap_readme(), encoding="utf-8")

    ai_dir = repo / "ai-concepts"
    ai_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(a.ai_pdf, ai_dir / "ai-terms-explained.pdf")
    names = write_ai_images(extract_ai_images(a.ai_pdf), ai_dir / "images")
    (ai_dir / "README.md").write_text(ai_readme(names), encoding="utf-8")

    n_problems = verify_assignments()
    build_assignments(repo)

    n_files = sum(1 for p in repo.rglob("*") if p.suffix in (".ipynb", ".py") and "scripts" not in p.relative_to(repo).parts)
    n_pdf = sum(1 for _ in repo.rglob("*.pdf"))
    (repo / "README.md").write_text(main_readme(chapters, n_files, n_pdf), encoding="utf-8")
    (repo / "INDEX.md").write_text(index_page(), encoding="utf-8")
    (repo / "LICENSE").write_text(LICENSE, encoding="utf-8")
    (repo / "CONTRIBUTING.md").write_text(CONTRIBUTING, encoding="utf-8")
    (repo / ".gitignore").write_text(
        ".ipynb_checkpoints/\n.DS_Store\nIcon?\n__pycache__/\n.venv/\nvenv/\n*.pyc\n", encoding="utf-8")
    (repo / "requirements.txt").write_text("jupyterlab>=4.0\n", encoding="utf-8")

    total, broken = verify_links(repo)
    print(f"chapters mapped: {len(chapters)}/{len(chapters)}")
    print(f"assignment problems verified (solutions pass, starters fail): {n_problems}")
    print(f"links checked: {total}, broken: {len(broken)}")
    for b in broken:
        print("  BROKEN:", b)
    for n in dict.fromkeys(notes):
        print(" -", n)
    print(f"notebooks and scripts: {n_files}, pdfs: {n_pdf}")
    if broken:
        raise SystemExit(1)


def cli():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--ai-pdf", required=True)
    ap.add_argument("--chapters", required=True)
    ap.add_argument("--repo", required=True)
    build(ap.parse_args())


if __name__ == "__main__":
    cli()
