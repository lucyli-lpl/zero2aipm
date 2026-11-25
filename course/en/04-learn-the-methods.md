---
id: "04"
title: "Learn the Methods Through Your Project"
summary: "Study evals, error analysis, capability boundaries, context and agent design, always against a product you built."
time: "1 to 3 weeks"
output: "A capability boundary map, an eval set and an error analysis for your own product"
---

# Module 4 · Learn the Methods Through Your Project

## Why this module

After Module 3 you have products that sometimes work and sometimes do strange things. That is the right moment to study methods. Every concept now has a place to land: "evals" is no longer an abstract word, it is how you find out whether your agent got better or worse after you changed the prompt.

The methods in this module change much more slowly than the tools. They are what separate someone who built a demo from someone who can run an AI product.

## How to study: a five-day block

When I wanted to go deep, I ran a five-day block with a fixed shape for each day:

- **1 hour of close reading**, with a reading map written first: what is this text about, how does it relate to my project, which parts to read closely.
- **2 hours of extension**: related reading, or applying the idea at work.
- **One hands-on task**: something that produces a file you can show.
- **A self-test at the end**: the AI writes multiple-choice, short-answer and application questions. You answer, then it marks you.

Two lessons from running it: commute time is good for podcasts, as long as you do not try to take notes, and you mostly do not need paid courses. The best authors in this space publish their core material for free.

## The methods

### 1. Capability boundaries: decide where AI should and should not act

For each scenario in your product, place it in one of three zones:

- **Core zone**: the AI handles it reliably. This is where you test hardest and promise quality.
- **Edge zone**: in scope, but the AI sometimes falls short (weak knowledge, unclear user input, flawed workflow). You design fallbacks and improve over time.
- **Out-of-scope zone**: the AI should not try. The right behavior is to hand off to another mode, ask a clarifying question, refuse politely, or pass to a person.

This one map drives your test plan, your prompt rules and your support plan.

### 2. Evals: how you know it got better

- Build a set of real inputs with the expected behavior for each. Twenty to fifty is enough to start.
- Prefer pass/fail judgments over 1-to-10 scores. They are faster to agree on and easier to act on.
- Run the whole set before and after every change to prompts, knowledge or models.
- The eval set is your acceptance standard. Write it before you ask anyone to build.

### 3. Error analysis: let real failures tell you what to fix

- Collect real conversations or traces, including the failures.
- Read them and write a short free-form note on each failure.
- Group the notes into categories (a failure taxonomy), count each category, and fix the biggest one first.
- Generic metrics such as "hallucination score" are less useful than categories that come from your own data.

### 4. Context engineering: what the model sees decides what it does

- Choose how knowledge reaches the model by the shape of the document. Long prose suits retrieval (RAG). Structured tables often work better with structured lookup. Small, stable rules can sit in the system prompt.
- Split stable global rules (system prompt) from scenario-specific procedures loaded only when needed (skills).
- Prefer positive instructions ("do this") over long lists of things not to do. Negative examples tend to leak into behavior.
- Add boundary knowledge: what the product covers, which brands or departments, what is out of scope. Without it, the model improvises at the edges.

### 5. Agents and multi-agent: only as complex as needed

Start with the simplest structure that works: one model call, then a fixed workflow, then an agent. Reach for multiple agents only when at least one of these is true:

- **Context pollution**: a subtask generates lots of information the main task does not need.
- **Parallel exploration**: the task benefits from searching many directions at once.
- **Specialization**: different parts need different tools or conflicting instructions, or one agent would carry too many tools.

Expect multi-agent systems to use several times more tokens, and often more total time, than a single agent on the same task.

### 6. Designing from the business goal, not from the architecture

When asked to design an agent system (a common interview question), work in this order:

1. The business goal.
2. The key business flow: how people do it today.
3. Where it breaks: the decisions, delays and errors that cost the most.
4. Agent roles and the human-in-the-loop points: which steps need a person, and why.
5. How you will verify it works: the eval set and the metrics.

This turns "build an agent" into "solve a business problem", which is what interviewers and stakeholders care about.

## Reading list (checked November 2026)

Start with the first two. Add the rest when your project needs them.

- Anthropic, Building effective agents: <https://www.anthropic.com/research/building-effective-agents>
- Hamel Husain, Your AI Product Needs Evals: <https://hamel.dev/blog/posts/evals/>
- Hamel Husain, on error analysis: <https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html>
- Anthropic, When to use multi-agent systems: <https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them>
- Anthropic engineering blog (context engineering, harness design, agent skills): <https://www.anthropic.com/engineering>
- Chip Huyen, *AI Engineering* (O'Reilly, 2024)

## Exercise

1. Pick the product from Module 3 you care most about.
2. With Claude, list 10 to 20 scenarios a user might bring to it. Place each in a zone. Save as `my-journey/projects/<name>-boundaries.md`.
3. Turn the scenarios into an eval set (`templates/eval-set.csv`): input, expected behavior, pass/fail rule.
4. Run your product against it. Record results honestly.
5. For every failure, write one line on what went wrong. Ask Claude to help you group them into categories. Fix the largest category and run the set again.
6. Take Claude's quiz on this module.

## Check yourself

- Which scenarios in your product belong in the out-of-scope zone, and what does the product do with them?
- Did your fix improve the eval results, or only the example you were looking at?
- Could your product be simpler, with fewer agents or fewer steps, and still pass?

## From my journey

During the five-day block I wrote a capability boundary methodology and kept revising it as I applied it at work. One honest lesson: evaluation has well-written public methods, but AI product data operations (how to define a bad case, how to design labeling, how to connect user feedback to fixes) did not yet have a classic reference. I marked what had a source and what was my own working hypothesis. In areas without a textbook, your own practice is how the method gets written.
