"""Part 2 (AI concepts) content: 21 terms in 5 stages.

Structure and card art come from "AI-Terms-Explained.pdf" (The Complete AI
Vocabulary, 21 terms). Timestamps come from the video chapter list.
`card` is the 2-digit index of the image extracted from the PDF (see build.py).
"""
from dataclasses import dataclass, field


@dataclass
class Term:
    key: str
    title: str
    stage: int
    ts: str                     # chapter timestamp
    tagline: str                # one-line analogy used in the diagram
    summary: str
    points: list = field(default_factory=list)
    cards: list = field(default_factory=list)       # [(index, alt text)]
    links: list = field(default_factory=list)       # [(label, url)]


STAGES = {
    1: ("What You Already Use", "The words you meet the moment you open a chat window."),
    2: ("Under the Hood", "What actually happens to your words inside the model."),
    3: ("How It Learns", "How a model goes from random numbers to something useful."),
    4: ("Getting Smarter Without Retraining", "Giving a model fresh knowledge and real tools at question time."),
    5: ("Beyond Chat", "Where AI is heading: agents, other senses, deeper thinking, and big ideas."),
}

# Resources shared with the video
R_AI_TERMS = ("AI Terms Explained (interactive site)", "https://ai-terms-explained.netlify.app")
R_TOKENIZER = ("OpenAI Tokenizer", "https://platform.openai.com/tokenizer")
R_TRANSFORMER = ("Transformer Explainer (Polo Club)", "https://poloclub.github.io/transformer-explainer/")
R_PROMPT_CTX = ("Prompt & Context Engineering (interactive)", "https://prompt-context-with-mayank.netlify.app/")
R_GPT56 = ("OpenAI: Previewing GPT-5.6", "https://openai.com/index/previewing-gpt-5-6-sol/")
R_TEMP = ("Temperature & Top-K Visualizer", "https://andreban.github.io/temperature-topk-visualizer/")
R_AIRCANADA = ("Ars Technica: Air Canada must honor refund policy invented by airline's chatbot",
               "https://arstechnica.com/tech-policy/2024/02/air-canada-must-honor-refund-policy-invented-by-airlines-chatbot/")

TERMS = [
    # ---------------------------------------------------------- Stage 1
    Term("llm", "Large Language Model (LLM)", 1, "10:52:08",
         "A next-word predictor wearing the costume of understanding.",
         "An LLM is trained on enormous amounts of text to predict the most likely next word (strictly, the next "
         "token), one step at a time. It does not look facts up in a dictionary: it has absorbed statistical patterns "
         "of language so well that its output reads like understanding.",
         ["Learns patterns from massive reading: books, websites, articles.",
          "\"Thank you for ...\" is followed by \"your business\" because it has seen that pattern millions of times.",
          "Models come in sizes: small and fast and cheap, balanced, or large and capable but costly. "
          "Pick the right brain for the job: small for extraction, big for reasoning."],
         [("03", "LLM card: massive reading, pattern memory, next word"),
          ("04", "Models equal capabilities: cheap and fast, balanced, capable and costly")],
         [R_GPT56, R_AI_TERMS]),
    Term("prompting", "Prompting", 1, "10:58:07",
         "A couple of examples beats a paragraph of instructions.",
         "A prompt is the input you give the model. Zero-shot prompting gives only an instruction. Few-shot "
         "prompting adds a handful of worked examples, which anchors the model to the pattern and format you want.",
         ["Zero-shot: instruction only, the model guesses your intent.",
          "Few-shot: instruction plus 2-3 examples gives more consistent results.",
          "Adding examples is the cheapest upgrade to almost any prompt."],
         [("05", "Zero-shot vs few-shot prompting")],
         [R_PROMPT_CTX]),
    Term("temperature", "Temperature", 1, "11:01:57",
         "Safe dish or something new?",
         "Temperature controls how adventurous the next-word choice is. Low values pick the most probable word "
         "almost every time; high values sample more widely, giving variety (and more risk).",
         ["Low (near 0): reliable, repeatable. Best for facts, extraction and code.",
          "Medium: a little variety, still mostly consistent.",
          "High: creative and surprising, sometimes off the rails. Best for brainstorming."],
         [("06", "Temperature dial from safe to adventurous")],
         [R_TEMP]),
    Term("hallucination", "Hallucination", 1, "11:07:43",
         "A guess wearing a fact's costume.",
         "When a model has no real answer (an obscure question, missing knowledge) it still produces fluent text, "
         "because its job is to continue the pattern, not to say \"I don't know\". The result can be confidently wrong "
         "and hard to tell apart from a correct answer.",
         ["Confidence is not accuracy: citations, dates and figures can all be invented.",
          "Mitigate with grounding (RAG), asking for sources, lower temperature, and always verifying.",
          "Real-world case: an airline was held responsible for a refund policy its chatbot invented."],
         [("07", "Hallucination: obscure question leads to confident fabrication")],
         [R_AIRCANADA]),
    Term("context-engineering", "Context Engineering", 1, "11:12:19",
         "Everything on the table before you open your mouth.",
         "Prompting is what you type. Context engineering is everything already in front of the model when it "
         "answers: chat history, your preferences, retrieved documents and tool results, assembled and trimmed "
         "deliberately.",
         ["Chat history (summarised, not forgotten), preferences, retrieved docs.",
          "Prompt: one instruction. Context: the whole setup around it.",
          "Why the same question can get very different answers in different apps."],
         [("08", "Context engineering: assembled context sent to the model")],
         [R_PROMPT_CTX]),
    # ---------------------------------------------------------- Stage 2
    Term("tokens", "Tokens", 2, "11:17:22",
         "Puzzle pieces of words.",
         "Models do not read letters or whole words; they read tokens, the chunks a tokenizer splits text into. "
         "Common words are often one token, rare or long words become several. Pricing, speed and limits are all "
         "counted in tokens.",
         ["\"unbelievable\" might split into un + believe + able.",
          "API cost = tokens in + tokens out.",
          "Try it: paste any text into the tokenizer and watch it split."],
         [("09", "Tokens: a word broken into puzzle pieces")],
         [R_TOKENIZER]),
    Term("vectors", "Vectors & Embeddings", 2, "11:26:22",
         "A GPS coordinate for meaning.",
         "Each token is converted into a vector (a long list of numbers) called an embedding. Words with similar "
         "meaning end up close together, so meaning becomes measurable distance. This is why \"apple\" the fruit "
         "and \"Apple\" the company land in different neighbourhoods depending on context.",
         ["dog and puppy sit next to each other; laptop and spreadsheet cluster together.",
          "Similarity search over embeddings powers RAG and semantic search."],
         [("11", "Vectors: words as coordinates on a map of meaning")],
         []),
    Term("context-window", "Context Window", 2, "11:31:37",
         "A whiteboard with limited space.",
         "The context window is the maximum number of tokens a model can consider at once: your prompt, the chat so "
         "far, documents and its own reply. When it is full, the oldest content is dropped.",
         ["Every message adds up; the model has no memory beyond what fits on the board.",
          "Bigger windows allow longer documents but cost more and can dilute focus."],
         [("12", "Context window: a whiteboard that fills up and erases the oldest")],
         []),
    Term("parameters", "Model Parameters", 2, "11:39:49",
         "Billions of tiny sliders.",
         "Parameters (weights) are the numbers inside the network that training adjusts. No single one means "
         "anything; together they encode everything the model has learned. \"70B\" means seventy billion of them.",
         ["More parameters usually means more capacity, not automatically more intelligence.",
          "Training nudges every slider a tiny bit, millions of times."],
         [("13", "Parameters: billions of tiny sliders")],
         []),
    Term("attention", "Attention Mechanism", 2, "11:46:56",
         "Leaning on neighbouring words.",
         "To interpret a word, the model weighs how much each other word in the sentence matters to it. \"Bank\" "
         "next to \"deposited\" and \"paycheck\" means money; next to \"river\" it means a riverbank.",
         ["Same spelling, different meaning, decided by the neighbours.",
          "Every token looks at every other token and decides what to focus on."],
         [("17", "Attention: leaning on neighbouring words"),
          ("18", "Same word, two meanings: bank (money) vs bank (river)")],
         [R_TRANSFORMER]),
    Term("transformer", "Transformer", 2, "11:52:46",
         "The engine, not the car.",
         "The Transformer is the neural-network architecture (introduced in 2017) that stacks attention layers. "
         "The LLM is the car; the Transformer is the engine under the hood. Other architectures can generate text "
         "too, but nearly every major model today uses a variant of this one.",
         ["Tokens in, many attention layers, next-word prediction out.",
          "LLM generates the next word; the Transformer is one way (not the only way) to do it."],
         [("19", "Transformer: the engine, not the car")],
         [R_TRANSFORMER]),
    # ---------------------------------------------------------- Stage 3
    Term("pretraining", "Pretraining", 3, "12:04:37",
         "Millions of fill-in-the-blank quizzes.",
         "Pretraining hides a word in real text, asks the model to guess it, then compares with the truth and adjusts "
         "the parameters. Because the text supplies its own answer key, no human has to grade anything, which is why "
         "it scales to internet-sized data.",
         ["Hide a word, guess, compare, adjust, repeat billions of times.",
          "Produces a base model that is knowledgeable but not yet a helpful assistant."],
         [("20", "Pretraining: fill-in-the-blank at massive scale")],
         []),
    Term("fine-tuning", "Fine-Tuning", 3, "12:08:10",
         "A residency after a general degree.",
         "Fine-tuning continues training a base model on a smaller, focused set of examples so it specialises: "
         "medical Q&A, legal drafting, a company's support style. One base model can have many fine-tuned variants.",
         ["Base model + focused practice = domain expert.",
          "Teaches style and behaviour; it is not the best way to add fresh facts (see RAG)."],
         [("21", "Fine-tuning: general degree then specialised residency"),
          ("22", "Pretraining on a huge dataset, then supervised fine-tuning on a private knowledge base")],
         []),
    Term("rlhf", "RLHF", 3, "12:11:31",
         "Training a puppy, at model scale.",
         "Reinforcement Learning from Human Feedback: the model produces two drafts, a person picks the better one, "
         "and the model is nudged toward preferred answers. Repeated at scale, it makes assistants more helpful, "
         "polite and safe.",
         ["Humans express preference, not corrections.",
          "Makes answers pleasant, which is not the same as always correct."],
         [("23", "RLHF: two drafts, a human picks, the model is nudged")],
         []),
    # ---------------------------------------------------------- Stage 4
    Term("rag", "RAG: Retrieval-Augmented Generation", 4, "12:16:08",
         "Closed-book exam vs open-book exam.",
         "Instead of answering from memory, the system first retrieves relevant documents (company docs, HR "
         "policies) and hands them to the model with the question, so the answer is grounded in real text. "
         "Retrieval typically uses embeddings stored in a vector database.",
         ["Pipeline: prepare data (extract, chunk, embed) then embed the query, retrieve, generate.",
          "Only as good as what is retrieved: wrong document in, wrong answer out.",
          "Reduces hallucination and works with private, up-to-date data without retraining."],
         [("25", "RAG: closed-book vs open-book"),
          ("28", "RAG pipeline: data preparation, vector database, retrieval, LLM")],
         []),
    Term("mcp", "MCP: Model Context Protocol", 4, "12:26:47",
         "One universal port, like USB-C for AI.",
         "MCP is an open standard for connecting AI applications to external tools and data. Instead of every app "
         "writing custom glue for every service (Gmail, calendar, database), a service exposes an MCP server once "
         "and any MCP-capable client can use its tools, resources and prompts.",
         ["Before MCP: custom wiring per app per tool. After: one standard connection.",
          "Example: a Gmail MCP server offers send, draft and read email tools to Claude, Cursor, VS Code and others.",
          "MCP servers expose three things: tools, resources and prompts."],
         [("31", "MCP: one universal port instead of a drawer of cables")],
         []),
    # ---------------------------------------------------------- Stage 5
    Term("agents", "AI Agents", 5, "12:38:47",
         "Perceive, reason, act, observe.",
         "A chatbot answers and waits. An agent is handed a goal and works toward it in a loop: understand the "
         "situation, plan, use tools to act, check the result, and continue until done. Model plus memory plus tools.",
         ["Loop: perceive, reason, act, observe.",
          "\"Book the cheapest flight\": chatbot explains how; agent actually books it.",
          "The difference is hands, not intelligence."],
         [("44", "AI agents: perceive, reason, act, observe loop"),
          ("49", "Chatbot vs agent: answers only vs acts and completes")],
         []),
    Term("multimodal", "Multimodal AI", 5, "12:45:49",
         "More than one sense.",
         "A multimodal model handles several kinds of input and sometimes output (text, images, audio, video) in "
         "one system, so you can show it a photo, speak to it, or have it watch a clip.",
         ["One brain, many senses.", "Not a party trick: a genuinely different kind of input."],
         [("50", "Multimodal: text, image, audio and video into one model")],
         []),
    Term("reasoning", "Reasoning Models", 5, "12:48:15",
         "Thinking it through first.",
         "Reasoning models spend extra computation working through a problem step by step (break it down, work each "
         "step, check themselves) before giving a final answer. Slower and costlier, but better at multi-step "
         "maths, logic and planning.",
         ["Regular model answers instantly; reasoning model pauses and works it out.",
          "Use for hard multi-step problems, not for simple lookups."],
         [("51", "Reasoning models: tricky question, staged thinking, final answer")],
         []),
    Term("slm", "Small Language Models", 5, "12:52:07",
         "A private tutor for a handful of subjects.",
         "Small language models trade breadth for speed and cost. They are often created by distillation: a large "
         "teacher model trains a smaller student on specific tasks. Great for narrow, repeated work, on-device or "
         "on a budget.",
         ["Broad task: large model. Narrow, repeated task: small model.",
          "Distillation: teacher trains student."],
         [("52", "Small language models: large teacher, distillation, small student")],
         []),
    Term("agi-asi", "AGI vs ASI", 5, "12:54:10",
         "Narrow today, theoretical tomorrow.",
         "Today's AI is narrow: very good at what it was trained for. AGI (artificial general intelligence) would "
         "match a skilled human at virtually any task; ASI (artificial superintelligence) would exceed human ability "
         "broadly. Neither exists today, and nobody knows if or when they will.",
         ["AI: exists, used today.", "AGI and ASI: theoretical. Worth knowing the difference."],
         [("53", "Today's AI vs AGI vs ASI")],
         []),
]

RECAP = Term("recap", "Recap: How It All Connects", 5, "12:56:47",
             "One message, the whole machine.",
             "Walk one customer message through every term: \"I was charged twice, can you refund it?\" The text is "
             "broken into tokens and vectors, attention finds the meaning, context and RAG pull in the refund policy "
             "and chat history, an agent uses MCP tools to act on the payment system, a reasoning model works through "
             "the details, and RLHF-shaped training gives a warm, helpful reply.",
             [], [("54", "One message through the whole machine")], [])

FINAL_TS = ("12:59:03", "Final Thoughts")
INTRO_TS = ("10:47:48", "Python Wrap-Up & AI Section Intro")

# Card images that are not tied to a single term
COVER_CARDS = [("01", "cover.jpg", "The Complete AI Vocabulary: 21 terms"),
               ("02", "vocabulary-map.jpg", "The Complete AI Vocabulary map: 5 stages")]


# ---------------------------------------------------------------------------
# Hands-on activity per term (shown under each term in part-2-ai/README.md)
ACTIVITIES = {
    "llm": "Start a new chat and type \"Thank you for\". Ask the model to continue it five times. Note how often you get the same ending, then think about why.",
    "prompting": "Ask a chatbot to sort five made-up emails by urgency using only an instruction. Then add two worked examples to the same prompt and compare how consistent the answers are.",
    "temperature": "Open the visualizer, set temperature low and then high, and watch how the bar for the top word changes. Which setting would you pick for a tax calculation, and which for a poem?",
    "hallucination": "Ask a chatbot to summarise a book or paper you invented. Then ask for sources and try to verify one. What gave the fabrication away?",
    "context-engineering": "List five things a model would need to know to \"plan my week\" well (calendar, priorities, preferences...). Run the request once with none of them and once with all five.",
    "tokens": "Paste a long word, an English sentence and the same sentence in another language into the tokenizer. Compare the token counts and think about what that means for cost.",
    "vectors": "On paper, place these words on a map so related ones sit close together: dog, puppy, laptop, spreadsheet, pizza, pasta, apple, iPhone. Where does \"apple\" end up, and why is that hard?",
    "context-window": "A page of English text is roughly 400 to 500 tokens. Estimate whether a 30-page report would fit in an 8,000-token window.",
    "parameters": "Look up the parameter counts of three open models. Rank them, then check whether the biggest is also the best at your task.",
    "attention": "In Transformer Explainer type `The bank of the river` and then `The bank approved my loan`. Hover over `bank` each time and compare which words get the most attention.",
    "transformer": "In Transformer Explainer, find the three stages (embedding, transformer blocks, output probabilities) and point to where the next word is chosen.",
    "pretraining": "Take five sentences from a book, hide one word in each and ask a friend to guess. You have just done pretraining by hand.",
    "fine-tuning": "Write five question and answer pairs you would use to turn a general model into a support agent for a product you know.",
    "rlhf": "Ask a chatbot the same question twice with different wording, pick the better answer, and write down your criteria. Those criteria are what RLHF tries to learn.",
    "rag": "Pick a policy document. Write three questions about it and underline the sentence that answers each one. Finding that sentence is the retrieval step.",
    "mcp": "Choose three apps you use daily (email, calendar, notes). For each, list the tools an MCP server would expose, such as \"read\", \"create\" and \"search\".",
    "agents": "Pick the goal \"tidy my inbox\". Write two turns of the loop: what the agent perceives, what it reasons, which tool it acts with and how it checks the result.",
    "multimodal": "Take a photo of your fridge or desk, send it to a multimodal model and ask for a recipe or a cleanup plan. Which parts did it get right?",
    "reasoning": "Give the same multi-step maths puzzle to a standard model and a reasoning model. Compare the time taken and the quality of the answer.",
    "slm": "Write three tasks that need a large model and three that a small model could handle. What separates the two lists?",
    "agi-asi": "Write three things humans do easily that today's AI still struggles with. Would solving them require \"general\" intelligence?",
    "recap": "Trace a different message through the same machine, for example \"Book me the cheapest train to Delhi tomorrow\". Which of the 21 terms appear, and in what order?",
}

# ---------------------------------------------------------------------------
# Plain-language guide to every external resource
# (label, url, what it is, how to use it, timestamp of the related chapter, related term title)
RESOURCE_GUIDE = [
    (R_AI_TERMS[0], R_AI_TERMS[1],
     "A glossary site that explains the AI terms from this course in everyday language.",
     ["Open the site and pick any term.", "Read the short explanation first, then compare it with the card in this repo."],
     "10:47:48", "All 21 terms"),
    (R_TOKENIZER[0], R_TOKENIZER[1],
     "A tool from OpenAI that shows exactly how a piece of text is cut into tokens and how many there are.",
     ["Paste any text into the box.", "Look at the coloured chunks: each colour is one token.",
      "Try a long word, an emoji and a non-English sentence and compare the counts."],
     "11:17:22", "Tokens"),
    (R_TEMP[0], R_TEMP[1],
     "A visualizer built on real next-word probabilities from a small open model (Gemma 3 1B). It shows the ten most likely next tokens as a chart.",
     ["Move the temperature slider and watch the bars flatten or sharpen.",
      "Set top-k to 1 and see that only the best token survives.",
      "Try top-p to keep the smallest group of tokens whose probabilities add up to p."],
     "11:01:57", "Temperature"),
    (R_AIRCANADA[0], R_AIRCANADA[1],
     "A news report on a 2024 case where an airline was held to a refund policy that its own chatbot had invented. A real example of why hallucinations matter.",
     ["Read the article.", "Ask yourself which of the three fixes (grounding, verification, human review) would have stopped it."],
     "11:07:43", "Hallucination"),
    (R_PROMPT_CTX[0], R_PROMPT_CTX[1],
     "Your own companion site, the Prompt Engineering Masterclass: a place to go deeper on writing prompts and building context.",
     ["Use it after the Prompting and Context Engineering chapters.", "Apply one idea to a real task you do this week."],
     "10:58:07", "Prompting, Context Engineering"),
    (R_TRANSFORMER[0], R_TRANSFORMER[1],
     "An interactive tool that runs a small GPT-2 model right in your browser so you can watch embeddings, attention and next-word probabilities happen live.",
     ["Type a short sentence and press the generate button.", "Hover over a token to see which other tokens it pays attention to.",
      "Change temperature, top-k and top-p and watch the output probabilities move."],
     "11:52:46", "Attention, Transformer"),
    (R_GPT56[0], R_GPT56[1],
     "An OpenAI announcement page linked in the video, useful as an example of how a lab presents a new model.",
     ["Read how the model is described.", "Spot the terms from Stage 1 and 2 in the announcement (parameters, context window, reasoning)."],
     "10:52:08", "LLMs"),
]

# ---------------------------------------------------------------------------
QUIZ = [
    ("What does an LLM actually do at each step?", "It predicts the next token based on patterns learned during training."),
    ("Which setting would you lower to get more predictable answers?", "Temperature."),
    ("Why can a confident answer still be wrong?", "The model is trained to continue plausible text, not to check facts, so it can hallucinate."),
    ("What is the difference between a prompt and context?", "A prompt is what you type; context is everything the model sees (history, preferences, documents, tool results)."),
    ("Why are tokens important for cost?", "Providers price usage per token, both input and output."),
    ("What does an embedding represent?", "A word or token as a list of numbers where similar meanings sit close together."),
    ("What happens when the context window is full?", "The oldest content is dropped (or must be summarised) to make room."),
    ("Which stage of training uses human preferences?", "RLHF."),
    ("How does RAG reduce hallucination?", "It retrieves real documents first and has the model answer from them."),
    ("What problem does MCP solve?", "It gives AI apps one standard way to connect to tools and data, instead of custom wiring for each."),
    ("What turns a chatbot into an agent?", "The ability to act: it loops through perceive, reason, act and observe using tools."),
    ("Does AGI exist today?", "No. Today's AI is narrow; AGI and ASI are still theoretical."),
]
