---
id: "01"
title: "AI as Your Tutor"
summary: "Learn any new concept by rebuilding the problem it solves, then let the AI test you."
time: "1 hour"
output: "Three concepts learned the reconstruct way, each with a self-test"
---

# Module 1 · AI as Your Tutor

## Why this module

You will meet a new AI term almost every day: RAG, MCP, harness, context engineering, whatever arrives next month. Memorizing definitions does not hold up. A definition tells you what something is called. It does not tell you why it exists, so the next variant with a new name looks like a new thing to learn from scratch.

The fastest learning partner you have is the AI itself. Most people use it as a search engine that answers questions. Used well, it is a tutor that explains, checks your understanding and points out where you are wrong.

## The method: reconstruct, then get tested

**Step 1. Go back to the world before the concept existed.** Ask: what were people trying to do, what went wrong, and what constraints made the obvious fixes fail? Then derive the concept as if it had not been invented yet.

Example with RAG:

- Before: a language model only knows what was in its training data, which stops at some date and never includes your company's documents.
- Obvious fix 1: retrain the model on your documents. Too slow and too expensive to repeat every time a document changes.
- Obvious fix 2: paste every document into the prompt. The prompt has a size limit, and long prompts get slow, costly and less accurate.
- So you need a way to find only the few passages relevant to this question, and put just those into the prompt. That is retrieval-augmented generation.

Once you have rebuilt it this way, follow-up ideas stop being new vocabulary. "Hybrid retrieval", "reranking" and "chunking strategy" are all answers to "the retrieval step finds the wrong passages", a problem you already understand.

**Step 2. Ask the AI to explain it this way.** A prompt that works:

> Teach me [concept] the reconstruct way. Start from the world before it existed. What problem were people facing, what did they try first, and why did that fail? Then derive [concept] step by step. Use one concrete example. Keep it under 400 words.

**Step 3. Have it test you.** Right after, ask for a short quiz: two multiple-choice questions, one short-answer question, and one question that applies the concept to a product you know. Answer without looking back. The questions you miss are the ones to revisit.

**Step 4. Put it in your own words.** Add one line to your glossary in plain language, as you would explain it to a friend. If you cannot, you have not finished.

## Habits that make the AI a better tutor

- **Tell it who you are.** "I am a product manager with no engineering background" changes the explanation a lot.
- **Ask for one example, not five.** One worked example teaches more than a list.
- **Push back.** If an explanation feels too smooth, ask "what is the strongest argument that this approach is wrong?" or "where does this break in practice?"
- **Ask what changed recently.** Models do not know everything that happened after their training. For anything current, ask the AI to search, or check a recent source yourself.

## Exercise

1. Pick three terms you have seen but could not explain. If you have none, use: context window, function calling, evals.
2. For each one, ask Claude to teach it the reconstruct way (Claude in this course does this by default).
3. Take the quiz Claude gives you after each one. Write your answers before asking for the correct ones.
4. Add each term to `my-journey/glossary.md` in one or two plain sentences, with the date.
5. Log the session in your learning log.

## Check yourself

- For one of your three terms, can you name the problem it solves without using the term itself?
- Which quiz question did you miss, and why?
- What would make one of your three concepts obsolete? (If you can answer this, you understand it.)

## From my journey

Early on I learned terms by watching plain-language explainer videos and copying definitions into a document. It helped me read reports, but I forgot most of it within weeks. The concepts that stayed were the ones I had to use in a project or rebuild from the problem. Later I made "teach me the reconstruct way" my default way of asking about anything new.
