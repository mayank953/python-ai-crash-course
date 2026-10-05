# AI Roadmap for Beginners

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
| 1 | Python basics | [lessons 01 to 16](../python/01-introduction-to-python/) | 1 to 2 weeks |
| 2 | Decisions and loops | [lessons 17 to 25](../python/17-conditionals-if/) | about 1 week |
| 3 | Data structures | [lessons 26 to 36](../python/26-intro-data-structures/) | 1 to 2 weeks |
| 4 | Functions | [lessons 37 to 44](../python/37-intro-to-functions/) | about 1 week |
| 5 | Speak the language of AI | [AI concepts](../ai-concepts/README.md) | 3 to 5 days |
| 6 | Use AI well | [Prompting and context](../ai-concepts/README.md#prompting) | ongoing |
| 7 | Build with AI | Mini projects below | 2 to 4 weeks |
| 8 | Keep growing | Pick one project and ship it | ongoing |

\*A suggestion for about an hour of study a day. Go faster or slower; finishing matters more than speed.

---

## Stage 1: Python basics

**Goal:** install Python, run code, and work with numbers, text and operators.

- Do: [lessons 01 to 16](../python/01-introduction-to-python/). Start with [installing Python](../python/02-installing-python/).
- Test yourself: [Checkpoint 1](../assignments/A1-setup-and-basics.ipynb), [Checkpoint 2](../assignments/A2-types-strings-casting.ipynb)
  and [Checkpoint 3](../assignments/A3-operators-formatting.ipynb).
- **Mini projects:** a tip calculator, a unit converter, a "format my name" helper.
- **You are ready to move on when** you can store values in variables, slice a string, and print tidy output with f-strings.

## Stage 2: Decisions and loops

**Goal:** make your programs choose and repeat.

- Do: [lessons 17 to 25](../python/17-conditionals-if/).
- Test yourself: [Checkpoint 4](../assignments/A4-conditionals-loops.ipynb).
- **Mini projects:** a number-guessing game, a multiplication-table printer, a password-strength checker.
- **You are ready to move on when** you can read a loop and predict what it prints before running it.

## Stage 3: Data structures

**Goal:** organise information with lists, tuples, sets and dictionaries.

- Do: [lessons 26 to 36](../python/26-intro-data-structures/).
- Test yourself: [Checkpoint 5](../assignments/A5-data-structures.ipynb).
- **Mini projects:** a contact book with a dictionary, a to-do list, a word-frequency counter.
- **You are ready to move on when** you can pick the right structure for a problem and explain why.

## Stage 4: Functions

**Goal:** package code so you can reuse it, and meet the functional tools used everywhere in Python.

- Do: [lessons 37 to 44](../python/37-intro-to-functions/).
- Test yourself: [Checkpoint 6](../assignments/A6-functions.ipynb).
- When you want to write larger programs, continue with [exception handling](../python/45-exception-handling/) and [object-oriented programming](../python/46-object-oriented-programming/).
- **Mini projects:** turn your earlier projects into functions, build a small text-cleaning toolkit with `map` and `filter`.
- **You are ready to move on when** you can write a function with default and keyword arguments and explain what it returns.

## Stage 5: Speak the language of AI

**Goal:** understand the 21 core terms well enough to explain them to a friend.

- Do: the [AI concepts guide](../ai-concepts/README.md), one stage at a time, with the card images and the activity under each term.
- Try the tools: the [tokenizer, temperature visualizer and Transformer Explainer](../ai-concepts/README.md#resources-explained).
- Test yourself: the [quiz](../ai-concepts/README.md#quiz).
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

[Back to the course home](../README.md) · [Start with lesson 01](../python/01-introduction-to-python/)
