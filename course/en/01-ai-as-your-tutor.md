---
id: "01"
title: "The AI Knowledge Map"
summary: "Watch three starter videos, then walk a 12-node route through the core terms of AI applications."
time: "3 to 5 hours, over a few days"
output: "Starter videos watched, the map walked once, and the first entries in your glossary"
---

# Module 1 · The AI Knowledge Map

## Why this module

The hardest part of starting from zero is not that any one idea is difficult. It is not knowing which ideas exist, which to learn first, and how they relate. This module gives you two things directly: the videos I recommend most from my own learning, and a route that strings the core terms of AI applications together in the order they appeared. You do not need to come up with the terms yourself. Just follow along.

## Step 1: Watch these first

Watch them in order. The first two are essential. Most are in Chinese; if you need English, ask your tutor for an equivalent and check that it is recent.

| Video | What you get |
|---|---|
| [Andrew Ng, "AI for Everyone"](https://www.bilibili.com/video/BV1yC4y127uj) | What AI can and cannot do; the big picture |
| [Bilibili @唐吉坷德拉曼查的英豪](https://search.bilibili.com/upuser?keyword=%E5%94%90%E5%90%89%E5%9D%B7%E5%BE%B7%E6%8B%89%E6%9B%BC%E6%9F%A5%E7%9A%84%E8%8B%B1%E8%B1%AA), starting with his explainer on "Attention Is All You Need" | How large models came about. All his videos are worth watching |
| [AI terms in plain words](https://www.bilibili.com/video/BV1ojfDBSEPv) | A first look at MCP, tools, skills and other common terms |
| [Mu Li: close reading of the Transformer paper](https://www.bilibili.com/video/BV1pu411o7BE) (optional) | For going one level deeper |

No need to take notes or understand everything. The goal is to have heard these terms, so the map in the next step feels familiar.

## Step 2: Walk the map

<!-- knowledge-map -->

The map has 12 core nodes in four stages, in the order they appeared. Each node exists to solve a problem the previous one left open:

| Stage | Nodes | What this stage solves |
|---|---|---|
| The model itself (2017–2022) | LLMs and the Transformer, prompt engineering | What a large model is and how to talk to it |
| Teaching the model your data (2020–2023) | Fine-tuning, RAG | A general model knows nothing about your company |
| Letting the model act (2022–2025) | Function calling, MCP, agents, multi-agent systems | From only talking to using tools and finishing tasks |
| Making agents reliable (2025–2026) | Context engineering, agent skills, personal agents, harness engineering | Keeping agents steady over long, real work |

Each node has four parts: a one-line explanation, why it appeared, branch terms, and recommended resources. On the website you can open each node. In an agent, the full content is in [`knowledge-map.yaml`](knowledge-map.yaml) and your tutor walks you through it stage by stage.

**How to walk it:** at first, read only each node's one-liner and "why it appeared", and string the 12 nodes together from start to finish. Come back for the branches and resources when a project needs them. At the end there is a "good to know" shelf of research-heavy topics; recognising the names is enough.

## Step 3: When you get stuck, ask from the problem

The "why it appeared" part of each node uses this course's core learning method: do not memorise the definition. Go back to the world before the idea existed, see what problem people had and why the obvious fixes failed, then derive the idea.

When a node or branch does not make sense, tell your tutor:

> Teach me [term] by reconstructing it. Start from the world before it existed: what problem did people have, what did they try first, and why did that fail? Then derive [term]. Use one concrete example, under 300 words.

Tutors in this course explain this way by default. When you meet a new term that is not on the map, ask the same way, then hang it on the right stage.

## Exercise

1. Watch the first three videos from Step 1 and add an entry to your learning log.
2. Tell your tutor "walk me through the map". It explains one stage at a time and reconstructs each node. You only need to say "got it" or "explain that one again".
3. When you are done, add the five nodes you think matter most to `my-journey/glossary.md`. Your tutor can draft them first; rewrite them in your own plain words.

## Quick quiz

```quiz
- q: "A company wants an AI assistant that answers staff questions about the expense policy. The policy changes every month. What is the best approach?"
  options:
    - "Fine-tune a model on the company policy"
    - "RAG: put the policy documents in a knowledge base and retrieve before answering"
    - "Write every rule into one very long prompt"
    - "Build a multi-agent system"
  answer: 1
  explain: "Knowledge that changes often and must be quoted accurately is exactly what RAG is for. Fine-tuning teaches how to answer, not frequently updated facts, and a giant prompt is too long and too expensive."
- q: "What problem does MCP mainly solve?"
  options:
    - "Making the model itself smarter"
    - "Giving AI apps one standard way to connect to tools, so a tool written once works everywhere"
    - "Reducing hallucination"
    - "Lowering training costs"
  answer: 1
  explain: "With function calling, every app had to build its own connection to every tool. MCP is like a USB port for AI: one standard way to connect."
- q: "An agent drifts after running for several hours and forgets rules set at the start. Which area deals most directly with this?"
  options:
    - "Pre-training"
    - "Context engineering and harness engineering"
    - "Diffusion models"
    - "Few-shot prompting"
  answer: 1
  explain: "The longer an agent runs, the messier its context. Context engineering decides what it sees at each step; harness engineering adds constraints, feedback and evaluation to keep it steady."
- q: "You want the model to always write support replies in your company's tone and format. No new knowledge is involved. What do you try first?"
  options:
    - "Continued pre-training"
    - "Improve the prompt first, and fine-tune only if results stay inconsistent"
    - "Build a knowledge graph"
    - "Use multiple agents"
  answer: 1
  explain: "Tone and format are about how to answer. Start with the cheapest lever, the prompt, and fine-tune if it is not stable. Continued pre-training is for new knowledge."
```

## From my journey

At first I learned terms by watching plain-language explainer videos and copying definitions into a document. That helped me read industry reports, but I forgot most of it within weeks. What stayed were the ideas I actually used in a project, or rebuilt from the problem they solve. This map is what came out of later reorganising my scattered notes around one question: what problem was each technique solving?
