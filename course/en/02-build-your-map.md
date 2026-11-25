---
id: "02"
title: "Build Your Map"
summary: "Read one serious industry report, look up every unfamiliar term, and come out with a glossary and a picture of the field."
time: "1 to 2 weeks, alongside Module 3"
output: "A glossary of 30+ terms and a one-page map of the field"
---

# Module 2 · Build Your Map

## Why this module

When you start, everything looks equally important: model releases, funding rounds, new frameworks, viral demos. You need a rough map first, so you can tell which things are foundations and which are this month's news.

You do not need depth yet. You need to recognize the main concepts, know how they relate, and know where to look when you need more.

## The method: one report, every unknown word

1. **Pick one serious industry report.** Look for an annual AI report from a large tech company, research institute, consulting firm or business school. It should be from the last 12 months and cover both technology and applications.
2. **Read it with a glossary open.** Every time you hit a term you cannot explain, stop, learn it the reconstruct way (Module 1), and add it to your glossary. The first report is slow. That is the point: the report is a list of what you need to learn, in roughly the order people use it.
3. **Sort what you learn into layers.** After the report, organize your glossary into the map below.
4. **Read a second report only after you start building** (Module 3). Most people read too much before they build anything.

## A map of the field

These layers change slowly, even when the tools inside them change fast. Use them as shelves for your glossary.

| Layer | What it covers | Examples of terms (as of 2026) |
|---|---|---|
| How models are made | Training stages and what each one changes | pre-training, post-training, fine-tuning (SFT, LoRA), RLHF, reasoning models |
| What models can and cannot do | Capabilities, limits, how they are measured | context window, hallucination, benchmarks, multimodal, tokens and rate limits |
| Getting the model the right information | Everything around the prompt | prompt engineering, context engineering, RAG, knowledge graphs, memory |
| Letting the model act | Tools and autonomy | function calling, MCP, agents, multi-agent, skills |
| Making it reliable | Quality and control | evals, error analysis, guardrails, human in the loop, harness engineering |
| Turning it into a product | Product and business decisions | capability boundaries, cost and latency, trust, data flywheel, pricing |

Two notes from my own notes, because beginners mix them up:

- **Fine-tuning teaches a model how to answer** (format, style, following instructions). It does not reliably teach new facts. For new facts, you retrieve them (RAG) or, at much higher cost, continue pre-training.
- **Most product work happens in the middle three layers.** You will rarely train a model as a PM. You will constantly decide what information the model gets, what it is allowed to do, and how you know it worked.

Research-heavy topics such as diffusion models, GANs, liquid neural networks or object detection are worth recognizing, but they are optional for most AI PM roles. Put them on a "good to know" shelf and move on.

## Exercise

1. Ask your tutor to help you choose one report. Tell it which industry you are most interested in. Your tutor will suggest a few recent ones and check that they are publicly available.
2. Read it over several days. Every unknown term goes into `my-journey/glossary.md` with a date and a one-line plain explanation.
3. When you reach 30 terms, ask your tutor to sort your glossary into the six layers above. Look at which layer is thinnest.
4. Draw your map: a single page (a list, a table or a sketch) of the six layers with your terms on them. Save it as `my-journey/map.md`.
5. Ask your tutor to quiz you on ten random glossary terms. Re-learn the ones you miss.

## Check yourself

- Which layer is the thinnest on your map, and does that matter for the roles you want?
- Can you explain the difference between fine-tuning and RAG to a non-technical friend?
- Which three terms in your glossary do you expect to be renamed or replaced within a year?

## From my journey

My first report was a 2025 annual AI report from a large tech company. I paused at every unknown word and built a glossary as I read. It took most of a week, and I logged it every day. My glossary later covered training stages, model architectures, benchmarks, RAG with knowledge graphs, model selection and more. Looking back, about half of it was essential for product work and half was curiosity. That ratio is fine, as long as the curiosity half does not delay Module 3.
