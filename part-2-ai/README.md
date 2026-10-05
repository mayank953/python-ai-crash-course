# Part 2: AI Concepts Explained

Video: `10:47:48` to `13:01:38` - **21 AI terms in 5 stages**, from the chat window you already use to the frontier of what's next.

![The Complete AI Vocabulary: 21 terms](images/cover.jpg)

There is no code in this part. The goal is a working vocabulary: when someone says *context window*, *RAG* or *MCP* you know exactly what they mean and why it matters.

**Study materials**

- [`ai-terms-explained.pdf`](ai-terms-explained.pdf): the full visual diagram used in the video
- [AI Terms Explained](https://ai-terms-explained.netlify.app): interactive version of the glossary

![The Complete AI Vocabulary map: 5 stages](images/vocabulary-map.jpg)

## Contents

**Stage 1: What You Already Use**  
[Large Language Model (LLM)](#large-language-model-llm) · [Prompting](#prompting) · [Temperature](#temperature) · [Hallucination](#hallucination) · [Context Engineering](#context-engineering)

**Stage 2: Under the Hood**  
[Tokens](#tokens) · [Vectors & Embeddings](#vectors-embeddings) · [Context Window](#context-window) · [Model Parameters](#model-parameters) · [Attention Mechanism](#attention-mechanism) · [Transformer](#transformer)

**Stage 3: How It Learns**  
[Pretraining](#pretraining) · [Fine-Tuning](#fine-tuning) · [RLHF](#rlhf)

**Stage 4: Getting Smarter Without Retraining**  
[RAG: Retrieval-Augmented Generation](#rag-retrieval-augmented-generation) · [MCP: Model Context Protocol](#mcp-model-context-protocol)

**Stage 5: Beyond Chat**  
[AI Agents](#ai-agents) · [Multimodal AI](#multimodal-ai) · [Reasoning Models](#reasoning-models) · [Small Language Models](#small-language-models) · [AGI vs ASI](#agi-vs-asi)

---

## Stage 1: What You Already Use

*The words you meet the moment you open a chat window.*

### Large Language Model (LLM)

`10:52:08` &nbsp; *A next-word predictor wearing the costume of understanding.*

![LLM card: massive reading, pattern memory, next word](images/llm.jpg)

![Models equal capabilities: cheap and fast, balanced, capable and costly](images/llm-2.jpg)

An LLM is trained on enormous amounts of text to predict the most likely next word (strictly, the next token), one step at a time. It does not look facts up in a dictionary: it has absorbed statistical patterns of language so well that its output reads like understanding.

- Learns patterns from massive reading: books, websites, articles.
- "Thank you for ..." is followed by "your business" because it has seen that pattern millions of times.
- Models come in sizes: small and fast and cheap, balanced, or large and capable but costly. Pick the right brain for the job: small for extraction, big for reasoning.

**Try / read:** [OpenAI: Previewing GPT-5.6](https://openai.com/index/previewing-gpt-5-6-sol/) · [AI Terms Explained (interactive site)](https://ai-terms-explained.netlify.app)

### Prompting

`10:58:07` &nbsp; *A couple of examples beats a paragraph of instructions.*

![Zero-shot vs few-shot prompting](images/prompting.jpg)

A prompt is the input you give the model. Zero-shot prompting gives only an instruction. Few-shot prompting adds a handful of worked examples, which anchors the model to the pattern and format you want.

- Zero-shot: instruction only, the model guesses your intent.
- Few-shot: instruction plus 2-3 examples gives more consistent results.
- Adding examples is the cheapest upgrade to almost any prompt.

**Try / read:** [Prompt & Context Engineering (interactive)](https://prompt-context-with-mayank.netlify.app/)

### Temperature

`11:01:57` &nbsp; *Safe dish or something new?*

![Temperature dial from safe to adventurous](images/temperature.jpg)

Temperature controls how adventurous the next-word choice is. Low values pick the most probable word almost every time; high values sample more widely, giving variety (and more risk).

- Low (near 0): reliable, repeatable. Best for facts, extraction and code.
- Medium: a little variety, still mostly consistent.
- High: creative and surprising, sometimes off the rails. Best for brainstorming.

**Try / read:** [Temperature & Top-K Visualizer](https://andreban.github.io/temperature-topk-visualizer/)

### Hallucination

`11:07:43` &nbsp; *A guess wearing a fact's costume.*

![Hallucination: obscure question leads to confident fabrication](images/hallucination.jpg)

When a model has no real answer (an obscure question, missing knowledge) it still produces fluent text, because its job is to continue the pattern, not to say "I don't know". The result can be confidently wrong and hard to tell apart from a correct answer.

- Confidence is not accuracy: citations, dates and figures can all be invented.
- Mitigate with grounding (RAG), asking for sources, lower temperature, and always verifying.
- Real-world case: an airline was held responsible for a refund policy its chatbot invented.

**Try / read:** [Ars Technica: Air Canada must honor refund policy invented by airline's chatbot](https://arstechnica.com/tech-policy/2024/02/air-canada-must-honor-refund-policy-invented-by-airlines-chatbot/)

### Context Engineering

`11:12:19` &nbsp; *Everything on the table before you open your mouth.*

![Context engineering: assembled context sent to the model](images/context-engineering.jpg)

Prompting is what you type. Context engineering is everything already in front of the model when it answers: chat history, your preferences, retrieved documents and tool results, assembled and trimmed deliberately.

- Chat history (summarised, not forgotten), preferences, retrieved docs.
- Prompt: one instruction. Context: the whole setup around it.
- Why the same question can get very different answers in different apps.

**Try / read:** [Prompt & Context Engineering (interactive)](https://prompt-context-with-mayank.netlify.app/)

---

## Stage 2: Under the Hood

*What actually happens to your words inside the model.*

### Tokens

`11:17:22` &nbsp; *Puzzle pieces of words.*

![Tokens: a word broken into puzzle pieces](images/tokens.jpg)

Models do not read letters or whole words; they read tokens, the chunks a tokenizer splits text into. Common words are often one token, rare or long words become several. Pricing, speed and limits are all counted in tokens.

- "unbelievable" might split into un + believe + able.
- API cost = tokens in + tokens out.
- Try it: paste any text into the tokenizer and watch it split.

**Try / read:** [OpenAI Tokenizer](https://platform.openai.com/tokenizer)

### Vectors & Embeddings

`11:26:22` &nbsp; *A GPS coordinate for meaning.*

![Vectors: words as coordinates on a map of meaning](images/vectors.jpg)

Each token is converted into a vector (a long list of numbers) called an embedding. Words with similar meaning end up close together, so meaning becomes measurable distance. This is why "apple" the fruit and "Apple" the company land in different neighbourhoods depending on context.

- dog and puppy sit next to each other; laptop and spreadsheet cluster together.
- Similarity search over embeddings powers RAG and semantic search.

### Context Window

`11:31:37` &nbsp; *A whiteboard with limited space.*

![Context window: a whiteboard that fills up and erases the oldest](images/context-window.jpg)

The context window is the maximum number of tokens a model can consider at once: your prompt, the chat so far, documents and its own reply. When it is full, the oldest content is dropped.

- Every message adds up; the model has no memory beyond what fits on the board.
- Bigger windows allow longer documents but cost more and can dilute focus.

### Model Parameters

`11:39:49` &nbsp; *Billions of tiny sliders.*

![Parameters: billions of tiny sliders](images/parameters.jpg)

Parameters (weights) are the numbers inside the network that training adjusts. No single one means anything; together they encode everything the model has learned. "70B" means seventy billion of them.

- More parameters usually means more capacity, not automatically more intelligence.
- Training nudges every slider a tiny bit, millions of times.

### Attention Mechanism

`11:46:56` &nbsp; *Leaning on neighbouring words.*

![Attention: leaning on neighbouring words](images/attention.jpg)

![Same word, two meanings: bank (money) vs bank (river)](images/attention-2.jpg)

To interpret a word, the model weighs how much each other word in the sentence matters to it. "Bank" next to "deposited" and "paycheck" means money; next to "river" it means a riverbank.

- Same spelling, different meaning, decided by the neighbours.
- Every token looks at every other token and decides what to focus on.

**Try / read:** [Transformer Explainer (Polo Club)](https://poloclub.github.io/transformer-explainer/)

### Transformer

`11:52:46` &nbsp; *The engine, not the car.*

![Transformer: the engine, not the car](images/transformer.jpg)

The Transformer is the neural-network architecture (introduced in 2017) that stacks attention layers. The LLM is the car; the Transformer is the engine under the hood. Other architectures can generate text too, but nearly every major model today uses a variant of this one.

- Tokens in, many attention layers, next-word prediction out.
- LLM generates the next word; the Transformer is one way (not the only way) to do it.

**Try / read:** [Transformer Explainer (Polo Club)](https://poloclub.github.io/transformer-explainer/)

---

## Stage 3: How It Learns

*How a model goes from random numbers to something useful.*

### Pretraining

`12:04:37` &nbsp; *Millions of fill-in-the-blank quizzes.*

![Pretraining: fill-in-the-blank at massive scale](images/pretraining.jpg)

Pretraining hides a word in real text, asks the model to guess it, then compares with the truth and adjusts the parameters. Because the text supplies its own answer key, no human has to grade anything, which is why it scales to internet-sized data.

- Hide a word, guess, compare, adjust, repeat billions of times.
- Produces a base model that is knowledgeable but not yet a helpful assistant.

### Fine-Tuning

`12:08:10` &nbsp; *A residency after a general degree.*

![Fine-tuning: general degree then specialised residency](images/fine-tuning.jpg)

![Pretraining on a huge dataset, then supervised fine-tuning on a private knowledge base](images/fine-tuning-2.jpg)

Fine-tuning continues training a base model on a smaller, focused set of examples so it specialises: medical Q&A, legal drafting, a company's support style. One base model can have many fine-tuned variants.

- Base model + focused practice = domain expert.
- Teaches style and behaviour; it is not the best way to add fresh facts (see RAG).

### RLHF

`12:11:31` &nbsp; *Training a puppy, at model scale.*

![RLHF: two drafts, a human picks, the model is nudged](images/rlhf.jpg)

Reinforcement Learning from Human Feedback: the model produces two drafts, a person picks the better one, and the model is nudged toward preferred answers. Repeated at scale, it makes assistants more helpful, polite and safe.

- Humans express preference, not corrections.
- Makes answers pleasant, which is not the same as always correct.

---

## Stage 4: Getting Smarter Without Retraining

*Giving a model fresh knowledge and real tools at question time.*

### RAG: Retrieval-Augmented Generation

`12:16:08` &nbsp; *Closed-book exam vs open-book exam.*

![RAG: closed-book vs open-book](images/rag.jpg)

![RAG pipeline: data preparation, vector database, retrieval, LLM](images/rag-2.jpg)

Instead of answering from memory, the system first retrieves relevant documents (company docs, HR policies) and hands them to the model with the question, so the answer is grounded in real text. Retrieval typically uses embeddings stored in a vector database.

- Pipeline: prepare data (extract, chunk, embed) then embed the query, retrieve, generate.
- Only as good as what is retrieved: wrong document in, wrong answer out.
- Reduces hallucination and works with private, up-to-date data without retraining.

### MCP: Model Context Protocol

`12:26:47` &nbsp; *One universal port, like USB-C for AI.*

![MCP: one universal port instead of a drawer of cables](images/mcp.jpg)

MCP is an open standard for connecting AI applications to external tools and data. Instead of every app writing custom glue for every service (Gmail, calendar, database), a service exposes an MCP server once and any MCP-capable client can use its tools, resources and prompts.

- Before MCP: custom wiring per app per tool. After: one standard connection.
- Example: a Gmail MCP server offers send, draft and read email tools to Claude, Cursor, VS Code and others.
- MCP servers expose three things: tools, resources and prompts.

---

## Stage 5: Beyond Chat

*Where AI is heading: agents, other senses, deeper thinking, and big ideas.*

### AI Agents

`12:38:47` &nbsp; *Perceive, reason, act, observe.*

![AI agents: perceive, reason, act, observe loop](images/agents.jpg)

![Chatbot vs agent: answers only vs acts and completes](images/agents-2.jpg)

A chatbot answers and waits. An agent is handed a goal and works toward it in a loop: understand the situation, plan, use tools to act, check the result, and continue until done. Model plus memory plus tools.

- Loop: perceive, reason, act, observe.
- "Book the cheapest flight": chatbot explains how; agent actually books it.
- The difference is hands, not intelligence.

### Multimodal AI

`12:45:49` &nbsp; *More than one sense.*

![Multimodal: text, image, audio and video into one model](images/multimodal.jpg)

A multimodal model handles several kinds of input and sometimes output (text, images, audio, video) in one system, so you can show it a photo, speak to it, or have it watch a clip.

- One brain, many senses.
- Not a party trick: a genuinely different kind of input.

### Reasoning Models

`12:48:15` &nbsp; *Thinking it through first.*

![Reasoning models: tricky question, staged thinking, final answer](images/reasoning.jpg)

Reasoning models spend extra computation working through a problem step by step (break it down, work each step, check themselves) before giving a final answer. Slower and costlier, but better at multi-step maths, logic and planning.

- Regular model answers instantly; reasoning model pauses and works it out.
- Use for hard multi-step problems, not for simple lookups.

### Small Language Models

`12:52:07` &nbsp; *A private tutor for a handful of subjects.*

![Small language models: large teacher, distillation, small student](images/slm.jpg)

Small language models trade breadth for speed and cost. They are often created by distillation: a large teacher model trains a smaller student on specific tasks. Great for narrow, repeated work, on-device or on a budget.

- Broad task: large model. Narrow, repeated task: small model.
- Distillation: teacher trains student.

### AGI vs ASI

`12:54:10` &nbsp; *Narrow today, theoretical tomorrow.*

![Today's AI vs AGI vs ASI](images/agi-asi.jpg)

Today's AI is narrow: very good at what it was trained for. AGI (artificial general intelligence) would match a skilled human at virtually any task; ASI (artificial superintelligence) would exceed human ability broadly. Neither exists today, and nobody knows if or when they will.

- AI: exists, used today.
- AGI and ASI: theoretical. Worth knowing the difference.

### Recap: How It All Connects

`12:56:47` &nbsp; *One message, the whole machine.*

![One message through the whole machine](images/recap.jpg)

Walk one customer message through every term: "I was charged twice, can you refund it?" The text is broken into tokens and vectors, attention finds the meaning, context and RAG pull in the refund policy and chat history, an agent uses MCP tools to act on the payment system, a reasoning model works through the details, and RLHF-shaped training gives a warm, helpful reply.

---

## Final thoughts

`12:59:03` Final Thoughts: close the loop and decide where to go next.

## All resources from the video

| Resource | Link | Related term |
|---|---|---|
| OpenAI: Previewing GPT-5.6 | <https://openai.com/index/previewing-gpt-5-6-sol/> | Large Language Model (LLM) |
| AI Terms Explained (interactive site) | <https://ai-terms-explained.netlify.app> | Large Language Model (LLM) |
| Prompt & Context Engineering (interactive) | <https://prompt-context-with-mayank.netlify.app/> | Prompting, Context Engineering |
| Temperature & Top-K Visualizer | <https://andreban.github.io/temperature-topk-visualizer/> | Temperature |
| Ars Technica: Air Canada must honor refund policy invented by airline's chatbot | <https://arstechnica.com/tech-policy/2024/02/air-canada-must-honor-refund-policy-invented-by-airlines-chatbot/> | Hallucination |
| OpenAI Tokenizer | <https://platform.openai.com/tokenizer> | Tokens |
| Transformer Explainer (Polo Club) | <https://poloclub.github.io/transformer-explainer/> | Attention Mechanism, Transformer |
| AI Terms Explained (interactive site) | <https://ai-terms-explained.netlify.app> | all terms |

> Some of these sites block automated checkers, so if a link does not open for you, search for its title.
