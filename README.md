# Python AI Crash Course

[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch%20the%20course-red?logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=J9BI0jGOds8)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Learn Python from zero, then understand the AI vocabulary behind tools like ChatGPT and Claude.**
This repository holds every note, notebook and practice file for the 13-hour course.

> 🧭 **New to AI? [Follow the roadmap](roadmap/README.md)** for the best order to learn Python and AI from scratch.

[![Course video](https://img.youtube.com/vi/J9BI0jGOds8/maxresdefault.jpg)](https://www.youtube.com/watch?v=J9BI0jGOds8)

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

1. **Watch** the [course on YouTube](https://www.youtube.com/watch?v=J9BI0jGOds8). Use the chapter links below to jump to a topic.
2. **Get the files:** click *Code*, then *Download ZIP* (or use `git clone`).
3. **Set up** Python and Jupyter (below), then open the lesson folder that matches the chapter.
4. **Not sure where to begin?** Follow the [roadmap](roadmap/README.md).

### Set up in five minutes

You need Python 3.9 or newer.

```bash
git clone https://github.com/mayank953/python-ai-crash-course.git
cd python-ai-crash-course
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Prefer Anaconda? Install it (shown at [`20:31`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=1231s) in the video), run `jupyter notebook` in the repo folder and open any `.ipynb`.
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

| Topic | Video range |
|-------|-------------|
| Python setup & basics | 0:00 to 51:57 |
| Data types, strings & type casting | 51:57 to 2:15:50 |
| Operators & string formatting | 2:15:50 to 3:28:43 |
| Conditionals & loops | 3:28:43 to 5:33:56 |
| Data structures | 5:33:56 to 8:41:36 |
| Functions & functional programming | 8:41:36 to 10:47:48 |
| AI concepts explained (21 terms) | 10:47:48 to 13:01:38 |

## Chapter overview

All 96 chapters of the video, with the place in this repository that matches each one.

<details>
<summary><b>Show the full chapter table</b></summary>

| Time | Chapter | In this repo |
|------|---------|--------------|
| [`0:00`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=0s) | Intro: Master Python + AI | [Lesson 01](python/01-introduction-to-python/) |
| [`2:38`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=158s) | Why Do We Need Programming? | [Lesson 01](python/01-introduction-to-python/) |
| [`6:45`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=405s) | What Is Python & Where It's Used | [Lesson 01](python/01-introduction-to-python/) |
| [`11:10`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=670s) | Key Features of Python | [Lesson 01](python/01-introduction-to-python/) |
| [`14:22`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=862s) | Installing Python | [Lesson 02](python/02-installing-python/) |
| [`16:18`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=978s) | Running Python in Terminal & IDLE | [Lesson 02](python/02-installing-python/) |
| [`20:31`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=1231s) | Anaconda & Jupyter Notebook Setup | [Lesson 02](python/02-installing-python/) |
| [`29:18`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=1758s) | Built-in Functions & print() | [Lesson 03](python/03-print-input-modules/) |
| [`35:42`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=2142s) | Python Modules (math, import) | [Lesson 03](python/03-print-input-modules/) |
| [`38:20`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=2300s) | Errors: Syntax vs Runtime | [Lesson 03](python/03-print-input-modules/) |
| [`43:59`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=2639s) | Identifiers & Naming Rules | [Lesson 03](python/03-print-input-modules/) |
| [`51:57`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=3117s) | Data Types & Integers | [Lesson 04](python/04-data-types/) · [Lesson 05](python/05-numeric-data-types/) |
| [`1:00:14`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=3614s) | Float Data Type | [Lesson 05](python/05-numeric-data-types/) |
| [`1:03:13`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=3793s) | Complex Numbers | [Lesson 05](python/05-numeric-data-types/) |
| [`1:06:20`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=3980s) | Boolean Data Type | [Lesson 06](python/06-boolean/) |
| [`1:12:28`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=4348s) | Strings Basics | [Lesson 07](python/07-strings/) |
| [`1:19:04`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=4744s) | String Indexing | [Lesson 08](python/08-indexing/) |
| [`1:23:35`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=5015s) | Negative Indexing | [Lesson 08](python/08-indexing/) |
| [`1:27:35`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=5255s) | String Concatenation & Repetition | [Lesson 09](python/09-concatenation-slicing/) |
| [`1:33:40`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=5620s) | String Slicing | [Lesson 09](python/09-concatenation-slicing/) |
| [`1:50:14`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=6614s) | Slicing with Step Value | [Lesson 09](python/09-concatenation-slicing/) |
| [`2:01:13`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=7273s) | Type Conversion: Implicit | [Lesson 10](python/10-type-casting/) |
| [`2:07:12`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=7632s) | Explicit Type Casting | [Lesson 10](python/10-type-casting/) |
| [`2:15:50`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=8150s) | Operators in Python: Overview | [Lesson 11](python/11-arithmetic-operators/) |
| [`2:17:59`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=8279s) | Arithmetic Operators | [Lesson 11](python/11-arithmetic-operators/) |
| [`2:26:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=8768s) | Relational Operators | [Lesson 12](python/12-relational-operators/) |
| [`2:43:46`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=9826s) | Logical Operators | [Lesson 13](python/13-logical-assignment-identity/) |
| [`2:53:03`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=10383s) | Assignment Operators | [Lesson 13](python/13-logical-assignment-identity/) |
| [`2:58:11`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=10691s) | Identity Operators (is vs ==) | [Lesson 13](python/13-logical-assignment-identity/) |
| [`3:06:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=11168s) | Operator Precedence & Associativity | [Lesson 15](python/15-precedence-associativity/) |
| [`3:13:46`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=11626s) | String Formatting | [Lesson 16](python/16-string-formatting/) |
| [`3:25:07`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=12307s) | Python f-Strings | [Lesson 16](python/16-string-formatting/) |
| [`3:28:43`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=12523s) | Decision Control & if Statement | [Lesson 17](python/17-conditionals-if/) |
| [`3:41:17`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=13277s) | if-else Statement | [Lesson 18](python/18-if-else-elif/) |
| [`3:47:03`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=13623s) | elif Ladder | [Lesson 18](python/18-if-else-elif/) |
| [`3:56:24`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=14184s) | Nested if Statements | [Lesson 19](python/19-nested-if/) |
| [`4:04:18`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=14658s) | Conditionals: Practice Questions | [Lesson 20](python/20-conditionals-practice/) |
| [`4:19:50`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=15590s) | while Loop | [Lesson 21](python/21-while-loop/) |
| [`4:30:49`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=16249s) | break Statement | [Lesson 22](python/22-break-continue-pass/) |
| [`4:37:52`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=16672s) | continue Statement | [Lesson 22](python/22-break-continue-pass/) |
| [`4:45:36`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=17136s) | pass Statement | [Lesson 22](python/22-break-continue-pass/) |
| [`4:48:36`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=17316s) | for Loop | [Lesson 23](python/23-for-loop/) |
| [`5:00:29`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=18029s) | range() Function | [Lesson 24](python/24-range-function/) |
| [`5:15:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=18908s) | for Loop with range() | [Lesson 24](python/24-range-function/) |
| [`5:20:55`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=19255s) | Nested Loops | [Lesson 25](python/25-nested-loops/) |
| [`5:33:56`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=20036s) | Intro to Data Structures | [Lesson 26](python/26-intro-data-structures/) |
| [`5:43:37`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=20617s) | Lists in Python | [Lesson 27](python/27-lists/) |
| [`5:54:24`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=21264s) | List Operations | [Lesson 27](python/27-lists/) |
| [`6:01:49`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=21709s) | Built-in List Functions | [Lesson 28](python/28-list-functions-methods/) |
| [`6:14:35`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=22475s) | List Methods | [Lesson 28](python/28-list-functions-methods/) |
| [`6:28:20`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=23300s) | Copying Lists | [Lesson 28](python/28-list-functions-methods/) |
| [`6:33:38`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=23618s) | List Comprehension | [Lesson 29](python/29-list-comprehension/) |
| [`6:48:42`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=24522s) | Tuples | [Lesson 30](python/30-tuples/) · [Lesson 31](python/31-tuple-functions-methods/) |
| [`7:18:01`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=26281s) | Sets | [Lesson 32](python/32-sets/) |
| [`7:28:17`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=26897s) | Set Operations | [Lesson 33](python/33-set-operations/) |
| [`7:48:58`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=28138s) | Dictionaries | [Lesson 34](python/34-dictionaries/) |
| [`8:02:44`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=28964s) | Dictionary Operations & Methods | [Lesson 35](python/35-dictionary-functions-methods/) |
| [`8:19:30`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=29970s) | Strings Revisited: ord() & chr() | [Lesson 36](python/36-string-methods/) |
| [`8:26:41`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=30401s) | String Methods | [Lesson 36](python/36-string-methods/) |
| [`8:41:36`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=31296s) | Defining Your Own Function | [Lesson 37](python/37-intro-to-functions/) · [Lesson 38](python/38-defining-functions/) |
| [`8:48:01`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=31681s) | Return vs Void Functions | [Lesson 37](python/37-intro-to-functions/) · [Lesson 38](python/38-defining-functions/) |
| [`8:59:32`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=32372s) | Functions: Core Concepts | [Lesson 37](python/37-intro-to-functions/) · [Lesson 38](python/38-defining-functions/) |
| [`9:10:11`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=33011s) | Positional Arguments | [Lesson 39](python/39-argument-types/) |
| [`9:13:32`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=33212s) | Default Arguments | [Lesson 39](python/39-argument-types/) |
| [`9:28:51`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=34131s) | Variable-Length Arguments (*args) | [Lesson 40](python/40-args-kwargs/) |
| [`9:33:05`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=34385s) | Keyword Arguments (**kwargs) | [Lesson 40](python/40-args-kwargs/) |
| [`9:40:20`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=34820s) | Variable Scope: Local vs Global | [Lesson 41](python/41-variable-scope/) |
| [`9:56:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=35768s) | Functions as First-Class Citizens | [Lesson 42](python/42-first-class-functions/) |
| [`10:22:04`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=37324s) | Lambda Functions | [Lesson 43](python/43-lambda-functions/) |
| [`10:32:38`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=37958s) | map() Function | [Lesson 44](python/44-map-filter-reduce/) |
| [`10:37:07`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=38227s) | filter() Function | [Lesson 44](python/44-map-filter-reduce/) |
| [`10:43:06`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=38586s) | reduce() Function | [Lesson 44](python/44-map-filter-reduce/) |
| [`10:47:48`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=38868s) | Python Wrap-Up & AI Section Intro | [AI concepts overview](ai-concepts/README.md) |
| [`10:52:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=39128s) | Large Language Models (LLMs) | [Large Language Model (LLM)](ai-concepts/README.md#large-language-model-llm) |
| [`10:58:07`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=39487s) | Prompting | [Prompting](ai-concepts/README.md#prompting) |
| [`11:01:57`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=39717s) | Temperature | [Temperature](ai-concepts/README.md#temperature) |
| [`11:07:43`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=40063s) | AI Hallucination | [Hallucination](ai-concepts/README.md#hallucination) |
| [`11:12:19`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=40339s) | Context Engineering | [Context Engineering](ai-concepts/README.md#context-engineering) |
| [`11:17:22`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=40642s) | Tokens & Token Costs | [Tokens](ai-concepts/README.md#tokens) |
| [`11:26:22`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=41182s) | Vectors & Embeddings | [Vectors & Embeddings](ai-concepts/README.md#vectors--embeddings) |
| [`11:31:37`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=41497s) | Context Window | [Context Window](ai-concepts/README.md#context-window) |
| [`11:39:49`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=41989s) | Model Parameters | [Model Parameters](ai-concepts/README.md#model-parameters) |
| [`11:46:56`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=42416s) | Attention Mechanism | [Attention Mechanism](ai-concepts/README.md#attention-mechanism) |
| [`11:52:46`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=42766s) | Transformers | [Transformer](ai-concepts/README.md#transformer) |
| [`12:04:37`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=43477s) | How LLMs Learn: Pretraining | [Pretraining](ai-concepts/README.md#pretraining) |
| [`12:08:10`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=43690s) | Fine-Tuning | [Fine-Tuning](ai-concepts/README.md#fine-tuning) |
| [`12:11:31`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=43891s) | RLHF | [RLHF](ai-concepts/README.md#rlhf) |
| [`12:16:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=44168s) | RAG (Retrieval-Augmented Generation) | [RAG: Retrieval-Augmented Generation](ai-concepts/README.md#rag-retrieval-augmented-generation) |
| [`12:26:47`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=44807s) | MCP (Model Context Protocol) | [MCP: Model Context Protocol](ai-concepts/README.md#mcp-model-context-protocol) |
| [`12:38:47`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=45527s) | AI Agents | [AI Agents](ai-concepts/README.md#ai-agents) |
| [`12:45:49`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=45949s) | Multimodal AI | [Multimodal AI](ai-concepts/README.md#multimodal-ai) |
| [`12:48:15`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=46095s) | Reasoning Models | [Reasoning Models](ai-concepts/README.md#reasoning-models) |
| [`12:52:07`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=46327s) | Small Language Models | [Small Language Models](ai-concepts/README.md#small-language-models) |
| [`12:54:10`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=46450s) | AGI vs ASI | [AGI vs ASI](ai-concepts/README.md#agi-vs-asi) |
| [`12:56:47`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=46607s) | Recap: How It All Connects | [Recap](ai-concepts/README.md#recap-how-it-all-connects) |
| [`12:59:03`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=46743s) | Final Thoughts | [Final thoughts](ai-concepts/README.md#final-thoughts) |

</details>

## Python: Complete All Resources

📄 whiteboard notes (PDF) · 📘 theory notebook · 💻 code notebook · ✏️ exercises

Hover over an icon to see what it is. Each lesson title opens its own page with timestamps and tasks.

### Setup & Basics

| # | Lesson | Video | Files |
|---|--------|-------|-------|
| 01 | [Introduction to Python](python/01-introduction-to-python/) | [`0:00`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=0s) | [📄](python/01-introduction-to-python/whiteboard-notes.pdf "Whiteboard notes (PDF)") |
| 02 | [Installing Python & Setting Up Jupyter](python/02-installing-python/) | [`14:22`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=862s) | [📄](python/02-installing-python/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/02-installing-python/code.ipynb "Code notebook") |
| 03 | [Built-in Functions, print(), Modules, Errors & Identifiers](python/03-print-input-modules/) | [`29:18`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=1758s) | [📘](python/03-print-input-modules/theory.ipynb "Theory notebook") [💻](python/03-print-input-modules/code.ipynb "Code notebook") |

### Data Types, Strings & Type Casting

| # | Lesson | Video | Files |
|---|--------|-------|-------|
| 04 | [Data Types](python/04-data-types/) | [`51:57`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=3117s) | [📄](python/04-data-types/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/04-data-types/theory.ipynb "Theory notebook") [💻](python/04-data-types/code.ipynb "Code notebook") |
| 05 | [Numeric Types: int, float, complex](python/05-numeric-data-types/) | [`51:57`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=3117s) | [📄](python/05-numeric-data-types/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/05-numeric-data-types/theory.ipynb "Theory notebook") [💻](python/05-numeric-data-types/code.ipynb "Code notebook") |
| 06 | [Boolean Data Type](python/06-boolean/) | [`1:06:20`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=3980s) | [📄](python/06-boolean/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/06-boolean/theory.ipynb "Theory notebook") [💻](python/06-boolean/code.ipynb "Code notebook") |
| 07 | [Strings Basics](python/07-strings/) | [`1:12:28`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=4348s) | [📄](python/07-strings/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/07-strings/theory.ipynb "Theory notebook") [💻](python/07-strings/code.ipynb "Code notebook") |
| 08 | [String Indexing (Positive & Negative)](python/08-indexing/) | [`1:19:04`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=4744s) | [📄](python/08-indexing/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/08-indexing/theory.ipynb "Theory notebook") [💻](python/08-indexing/code.ipynb "Code notebook") |
| 09 | [Concatenation, Repetition & Slicing](python/09-concatenation-slicing/) | [`1:27:35`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=5255s) | [📄](python/09-concatenation-slicing/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/09-concatenation-slicing/code.ipynb "Code notebook") [💻](python/09-concatenation-slicing/code-step-in-slicing.ipynb "Code notebook") |
| 10 | [Type Conversion & Type Casting](python/10-type-casting/) | [`2:01:13`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=7273s) | [📄](python/10-type-casting/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/10-type-casting/theory.ipynb "Theory notebook") [💻](python/10-type-casting/code.ipynb "Code notebook") |

### Operators & String Formatting

| # | Lesson | Video | Files |
|---|--------|-------|-------|
| 11 | [Operators Overview & Arithmetic Operators](python/11-arithmetic-operators/) | [`2:15:50`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=8150s) | [📄](python/11-arithmetic-operators/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/11-arithmetic-operators/theory.ipynb "Theory notebook") [💻](python/11-arithmetic-operators/code.ipynb "Code notebook") |
| 12 | [Relational Operators](python/12-relational-operators/) | [`2:26:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=8768s) | [📄](python/12-relational-operators/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/12-relational-operators/theory.ipynb "Theory notebook") [💻](python/12-relational-operators/code.ipynb "Code notebook") |
| 13 | [Logical, Assignment & Identity Operators](python/13-logical-assignment-identity/) | [`2:43:46`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=9826s) | [📄](python/13-logical-assignment-identity/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/13-logical-assignment-identity/theory.ipynb "Theory notebook") [💻](python/13-logical-assignment-identity/code.ipynb "Code notebook") |
| 14 | [Membership & Binary (Bitwise) Operators](python/14-membership-binary/) | — | [📄](python/14-membership-binary/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/14-membership-binary/theory.ipynb "Theory notebook") [💻](python/14-membership-binary/code.ipynb "Code notebook") |
| 15 | [Operator Precedence & Associativity](python/15-precedence-associativity/) | [`3:06:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=11168s) | [📄](python/15-precedence-associativity/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/15-precedence-associativity/code.ipynb "Code notebook") |
| 16 | [String Formatting & f-Strings](python/16-string-formatting/) | [`3:13:46`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=11626s) | [📄](python/16-string-formatting/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/16-string-formatting/theory.ipynb "Theory notebook") [💻](python/16-string-formatting/code.ipynb "Code notebook") |

### Conditionals & Loops

| # | Lesson | Video | Files |
|---|--------|-------|-------|
| 17 | [Decision Control & the if Statement](python/17-conditionals-if/) | [`3:28:43`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=12523s) | [📄](python/17-conditionals-if/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/17-conditionals-if/theory.ipynb "Theory notebook") [💻](python/17-conditionals-if/code.ipynb "Code notebook") |
| 18 | [if-else & the elif Ladder](python/18-if-else-elif/) | [`3:41:17`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=13277s) | [📄](python/18-if-else-elif/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/18-if-else-elif/code.ipynb "Code notebook") |
| 19 | [Nested if Statements](python/19-nested-if/) | [`3:56:24`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=14184s) | [📄](python/19-nested-if/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/19-nested-if/theory.ipynb "Theory notebook") [💻](python/19-nested-if/code.ipynb "Code notebook") |
| 20 | [Conditionals: Practice Questions](python/20-conditionals-practice/) | [`4:04:18`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=14658s) | [📄](python/20-conditionals-practice/whiteboard-notes.pdf "Whiteboard notes (PDF)") [✏️](python/20-conditionals-practice/exercises-questions.ipynb "Exercises") [✏️](python/20-conditionals-practice/exercises-assignment.ipynb "Exercises") |
| 21 | [Introduction to Loops & the while Loop](python/21-while-loop/) | [`4:19:50`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=15590s) | [📘](python/21-while-loop/theory.ipynb "Theory notebook") [💻](python/21-while-loop/code.ipynb "Code notebook") |
| 22 | [break, continue & pass](python/22-break-continue-pass/) | [`4:30:49`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=16249s) | [📘](python/22-break-continue-pass/theory.ipynb "Theory notebook") [💻](python/22-break-continue-pass/code.ipynb "Code notebook") |
| 23 | [The for Loop](python/23-for-loop/) | [`4:48:36`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=17316s) | [💻](python/23-for-loop/code.ipynb "Code notebook") |
| 24 | [The range() Function](python/24-range-function/) | [`5:00:29`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=18029s) | [💻](python/24-range-function/code.ipynb "Code notebook") |
| 25 | [Nested Loops](python/25-nested-loops/) | [`5:20:55`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=19255s) | [💻](python/25-nested-loops/code.ipynb "Code notebook") |

### Data Structures

| # | Lesson | Video | Files |
|---|--------|-------|-------|
| 26 | [Introduction to Data Structures](python/26-intro-data-structures/) | [`5:33:56`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=20036s) | [📄](python/26-intro-data-structures/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/26-intro-data-structures/theory.ipynb "Theory notebook") |
| 27 | [Lists: Basics & Operations](python/27-lists/) | [`5:43:37`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=20617s) | [📄](python/27-lists/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/27-lists/code.ipynb "Code notebook") |
| 28 | [List Functions, Methods & Copying](python/28-list-functions-methods/) | [`6:01:49`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=21709s) | [📄](python/28-list-functions-methods/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/28-list-functions-methods/theory.ipynb "Theory notebook") [💻](python/28-list-functions-methods/code.ipynb "Code notebook") |
| 29 | [List Comprehension](python/29-list-comprehension/) | [`6:33:38`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=23618s) | [📄](python/29-list-comprehension/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/29-list-comprehension/theory.ipynb "Theory notebook") [💻](python/29-list-comprehension/code.ipynb "Code notebook") |
| 30 | [Tuples](python/30-tuples/) | [`6:48:42`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=24522s) | [📄](python/30-tuples/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/30-tuples/code.ipynb "Code notebook") |
| 31 | [Tuple Functions & Methods](python/31-tuple-functions-methods/) | [`6:48:42`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=24522s) | [📄](python/31-tuple-functions-methods/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/31-tuple-functions-methods/code.ipynb "Code notebook") |
| 32 | [Sets](python/32-sets/) | [`7:18:01`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=26281s) | [📄](python/32-sets/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/32-sets/code.ipynb "Code notebook") |
| 33 | [Set Operations, Functions & Methods](python/33-set-operations/) | [`7:28:17`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=26897s) | [📄](python/33-set-operations/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/33-set-operations/code.ipynb "Code notebook") |
| 34 | [Dictionaries](python/34-dictionaries/) | [`7:48:58`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=28138s) | [📄](python/34-dictionaries/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/34-dictionaries/code.ipynb "Code notebook") |
| 35 | [Dictionary Operations & Methods](python/35-dictionary-functions-methods/) | [`8:02:44`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=28964s) | [📄](python/35-dictionary-functions-methods/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/35-dictionary-functions-methods/code.ipynb "Code notebook") |
| 36 | [Strings Revisited: ord(), chr() & String Methods](python/36-string-methods/) | [`8:19:30`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=29970s) | [📄](python/36-string-methods/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/36-string-methods/code.ipynb "Code notebook") |

### Functions & Functional Programming

| # | Lesson | Video | Files |
|---|--------|-------|-------|
| 37 | [Introduction to Functions](python/37-intro-to-functions/) | [`8:41:36`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=31296s) | [📄](python/37-intro-to-functions/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/37-intro-to-functions/code.ipynb "Code notebook") |
| 38 | [Defining Your Own Functions](python/38-defining-functions/) | [`8:41:36`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=31296s) | [📄](python/38-defining-functions/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/38-defining-functions/code.ipynb "Code notebook") |
| 39 | [Types of Arguments: Positional & Default](python/39-argument-types/) | [`9:10:11`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=33011s) | [📄](python/39-argument-types/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/39-argument-types/theory.ipynb "Theory notebook") [💻](python/39-argument-types/code.ipynb "Code notebook") |
| 40 | [*args and **kwargs](python/40-args-kwargs/) | [`9:28:51`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=34131s) | [📄](python/40-args-kwargs/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/40-args-kwargs/code.ipynb "Code notebook") |
| 41 | [Variable Scope: Local vs Global](python/41-variable-scope/) | [`9:40:20`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=34820s) | [📄](python/41-variable-scope/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/41-variable-scope/code.ipynb "Code notebook") |
| 42 | [Functions as First-Class Citizens](python/42-first-class-functions/) | [`9:56:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=35768s) | [📄](python/42-first-class-functions/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/42-first-class-functions/code.ipynb "Code notebook") |
| 43 | [Lambda Functions](python/43-lambda-functions/) | [`10:22:04`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=37324s) | [📄](python/43-lambda-functions/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/43-lambda-functions/theory.ipynb "Theory notebook") [💻](python/43-lambda-functions/code.ipynb "Code notebook") |
| 44 | [map(), filter() & reduce()](python/44-map-filter-reduce/) | [`10:32:38`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=37958s) | [📄](python/44-map-filter-reduce/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/44-map-filter-reduce/code.ipynb "Code notebook") |

### Error Handling & OOP

| # | Lesson | Video | Files |
|---|--------|-------|-------|
| 45 | [Exception Handling](python/45-exception-handling/) | — | [📄](python/45-exception-handling/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](python/45-exception-handling/theory.ipynb "Theory notebook") [💻](python/45-exception-handling/code.ipynb "Code notebook") [💻](python/45-exception-handling/code-types-of-exception.ipynb "Code notebook") [✏️](python/45-exception-handling/exercises.ipynb "Exercises") |
| 46 | [Object-Oriented Programming](python/46-object-oriented-programming/) | — | [📄](python/46-object-oriented-programming/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](python/46-object-oriented-programming/01-classes-and-objects.ipynb "Code notebook") [💻](python/46-object-oriented-programming/02-encapsulation.ipynb "Code notebook") [💻](python/46-object-oriented-programming/03-abstraction.ipynb "Code notebook") [💻](python/46-object-oriented-programming/04-inheritance.ipynb "Code notebook") [📘](python/46-object-oriented-programming/05-types-of-inheritance-theory.ipynb "Theory notebook") [💻](python/46-object-oriented-programming/05-types-of-inheritance.ipynb "Code notebook") [💻](python/46-object-oriented-programming/06-polymorphism-operator-overloading.ipynb "Code notebook") [✏️](python/46-object-oriented-programming/exercise-complex-number-class.ipynb "Exercises") [✏️](python/46-object-oriented-programming/exercise-inheritance.ipynb "Exercises") |

### Checkpoint assignments

Test yourself at the end of every section. Each problem has a check cell that tells you instantly whether you got it right.

| Checkpoint | After lessons | Problems | Starter | Solutions |
|---|---|---|---|---|
| Setup & Basics | Lessons 01 to 03 | 5 | [notebook](assignments/A1-setup-and-basics.ipynb) | [solutions](assignments/solutions/A1-setup-and-basics.ipynb) |
| Data Types, Strings & Type Casting | Lessons 04 to 10 | 5 | [notebook](assignments/A2-types-strings-casting.ipynb) | [solutions](assignments/solutions/A2-types-strings-casting.ipynb) |
| Operators & String Formatting | Lessons 11 to 16 | 5 | [notebook](assignments/A3-operators-formatting.ipynb) | [solutions](assignments/solutions/A3-operators-formatting.ipynb) |
| Conditionals & Loops | Lessons 17 to 25 | 5 | [notebook](assignments/A4-conditionals-loops.ipynb) | [solutions](assignments/solutions/A4-conditionals-loops.ipynb) |
| Data Structures | Lessons 26 to 36 | 6 | [notebook](assignments/A5-data-structures.ipynb) | [solutions](assignments/solutions/A5-data-structures.ipynb) |
| Functions & Functional Programming | Lessons 37 to 44 | 6 | [notebook](assignments/A6-functions.ipynb) | [solutions](assignments/solutions/A6-functions.ipynb) |

## AI Concepts

The second half of the course explains **21 AI terms in 5 stages**. There is no code; the goal is to understand the language
of AI. Everything lives in [`ai-concepts/`](ai-concepts/README.md): one card per term from the course diagram, a short
explanation, a hands-on activity, a quiz, and the full diagram as a [PDF](ai-concepts/ai-terms-explained.pdf).

![The Complete AI Vocabulary map](ai-concepts/images/vocabulary-map.jpg)

| Stage | Terms |
|---|---|
| 1. What You Already Use | [Large Language Model (LLM)](ai-concepts/README.md#large-language-model-llm), [Prompting](ai-concepts/README.md#prompting), [Temperature](ai-concepts/README.md#temperature), [Hallucination](ai-concepts/README.md#hallucination), [Context Engineering](ai-concepts/README.md#context-engineering) |
| 2. Under the Hood | [Tokens](ai-concepts/README.md#tokens), [Vectors & Embeddings](ai-concepts/README.md#vectors--embeddings), [Context Window](ai-concepts/README.md#context-window), [Model Parameters](ai-concepts/README.md#model-parameters), [Attention Mechanism](ai-concepts/README.md#attention-mechanism), [Transformer](ai-concepts/README.md#transformer) |
| 3. How It Learns | [Pretraining](ai-concepts/README.md#pretraining), [Fine-Tuning](ai-concepts/README.md#fine-tuning), [RLHF](ai-concepts/README.md#rlhf) |
| 4. Getting Smarter Without Retraining | [RAG: Retrieval-Augmented Generation](ai-concepts/README.md#rag-retrieval-augmented-generation), [MCP: Model Context Protocol](ai-concepts/README.md#mcp-model-context-protocol) |
| 5. Beyond Chat | [AI Agents](ai-concepts/README.md#ai-agents), [Multimodal AI](ai-concepts/README.md#multimodal-ai), [Reasoning Models](ai-concepts/README.md#reasoning-models), [Small Language Models](ai-concepts/README.md#small-language-models), [AGI vs ASI](ai-concepts/README.md#agi-vs-asi), [Recap: How It All Connects](ai-concepts/README.md#recap-how-it-all-connects) |

### Resources explained

The video uses a handful of tools and articles. Here is what each one is and when to use it
(step-by-step guides are in the [AI section](ai-concepts/README.md#resources-explained)).

| Resource | What it is | Use it for | Chapter |
|---|---|---|---|
| [AI Terms Explained (interactive site)](https://ai-terms-explained.netlify.app) | A glossary site that explains the AI terms from this course in everyday language. | All 21 terms | [`10:47:48`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=38868s) |
| [OpenAI Tokenizer](https://platform.openai.com/tokenizer) | A tool from OpenAI that shows exactly how a piece of text is cut into tokens and how many there are. | Tokens | [`11:17:22`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=40642s) |
| [Temperature & Top-K Visualizer](https://andreban.github.io/temperature-topk-visualizer/) | A visualizer built on real next-word probabilities from a small open model (Gemma 3 1B). It shows the ten most likely next tokens as a chart. | Temperature | [`11:01:57`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=39717s) |
| [Ars Technica: Air Canada must honor refund policy invented by airline's chatbot](https://arstechnica.com/tech-policy/2024/02/air-canada-must-honor-refund-policy-invented-by-airlines-chatbot/) | A news report on a 2024 case where an airline was held to a refund policy that its own chatbot had invented. A real example of why hallucinations matter. | Hallucination | [`11:07:43`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=40063s) |
| [Prompt & Context Engineering (interactive)](https://prompt-context-with-mayank.netlify.app/) | Your own companion site, the Prompt Engineering Masterclass: a place to go deeper on writing prompts and building context. | Prompting, Context Engineering | [`10:58:07`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=39487s) |
| [Transformer Explainer (Polo Club)](https://poloclub.github.io/transformer-explainer/) | An interactive tool that runs a small GPT-2 model right in your browser so you can watch embeddings, attention and next-word probabilities happen live. | Attention, Transformer | [`11:52:46`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=42766s) |
| [OpenAI: Previewing GPT-5.6](https://openai.com/index/previewing-gpt-5-6-sol/) | An OpenAI announcement page linked in the video, useful as an example of how a lab presents a new model. | LLMs | [`10:52:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=39128s) |

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
The repo holds 93 notebooks and scripts and 41 PDFs.

## FAQ

**A notebook looks odd on GitHub.** Download the repo and open it locally with Jupyter for the best experience.

**`python` is not found.** On macOS and Linux use `python3`. On Windows try `py`.

**Which file do I open first in a lesson?** Watch the video, then `theory.ipynb`, then `code.ipynb`.

**Do I need an AI account for the AI concepts?** No. The activities work with any free chatbot, and the tools are free websites.

**I got stuck or found a mistake.** Open an [issue](https://github.com/mayank953/python-ai-crash-course/issues) with the lesson number and what happened.

## Contributing

Corrections and clearer explanations are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the [MIT License](LICENSE). Created by **Mayank Aggarwal**. If this helped you, star the repo and
share the [video](https://www.youtube.com/watch?v=J9BI0jGOds8) with a friend who is starting out.
