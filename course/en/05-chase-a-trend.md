---
id: "05"
title: "Chase a Trend Without Drowning"
summary: "Decide in ten minutes whether a hot new thing deserves your time, then learn it in two hours and write it up."
time: "Ongoing, about 3 hours per trend"
output: "A trend triage note and one product teardown"
---

# Module 5 · Chase a Trend Without Drowning

## Why this module

Something new goes viral in AI almost every month. If you chase all of it, you learn a little about everything and finish nothing. If you ignore all of it, you sound out of date in interviews, because interviewers love to ask "have you tried X?"

The skill is not keeping up with everything. It is deciding quickly what deserves your time, learning those few things fast, and turning each one into something you can show.

## The method

### Step 1. Triage in ten minutes

Ask four questions:

1. **What problem does it solve that was not solved before?** If you cannot find one, it is probably packaging.
2. **Does it change a product decision?** Would a PM design something differently because this exists? (New interaction pattern, new distribution channel, new cost structure, new capability.)
3. **Who is behind it, and is it still moving?** Check recent releases or commits. A trend with no updates in two months has usually peaked.
4. **Can I try it in two hours?** If setup alone takes a day, read a good write-up instead of installing it.

Write the answers in `my-journey/trends.md` with today's date. Most trends stop here, and that is fine: you now know enough to talk about them.

### Step 2. Two hours hands-on

For the trends that pass, set a two-hour limit. Install it, or use it, and do one real task with it. Keep notes on what surprised you and where it broke. Stop at two hours, even if it is going well.

### Step 3. Write a teardown

Use five questions to analyze it as a product:

1. **What problem does it solve?** How did people do this before, and what does AI replace or improve?
2. **What is the human-AI relationship?** Is the AI deciding or suggesting? Where does the user keep control, and when does a person take over?
3. **How does it earn trust?** Transparency, a track record of accuracy, or low stakes when it is wrong?
4. **Cold start and data flywheel.** What happens with no data on day one, and how does usage make it better?
5. **Business model.** How does the capability turn into value: lower cost, higher conversion, a new thing people pay for?

One page is enough. A teardown turns "I tried it" into "here is what I think about it", which is what interviews and colleagues actually want.

### Step 4. Put an expiry date on it

At the bottom of each note, write: "Likely to be out of date by: ___." It keeps you honest about what you learned (the reasoning, which lasts) and what you only observed (the tool, which will change).

## Keep your sources few

You do not need fifty newsletters. A small, steady set beats an endless feed:

- One or two primary sources from AI labs (their engineering blogs and release notes).
- One practitioner who writes carefully about what works in practice.
- One podcast for commute time.
- One source covering your local market.
- A monthly scan of trending open-source projects.
- A daily habit of one new term plus one review of an old one. A scheduled task can do this for you.

## Exercise

1. Ask your tutor what is currently trending in AI products. Your tutor will search, since this changes too fast to answer from memory.
2. Triage three of them with the four questions. Save to `my-journey/trends.md`.
3. Pick the one that best passes triage. Spend two hours on it and log what happened.
4. Write a teardown with the five questions, using `templates/teardown.md`. Add an expiry line.
5. Ask your tutor to challenge your teardown: what would someone who disagrees say?

## Check yourself

- Which of your three trends did you decide not to pursue, and why?
- What in your teardown will still be true in a year, even if the product is gone?
- Did you stop at two hours?

## From my journey (dated examples)

**March to April 2026: OpenClaw.** An open-source personal AI assistant framework that connected agents to chat apps was everywhere that spring. I installed it, connected it to a DeepSeek model and studied its design for an interview. I also installed another agent framework that would not run on Windows, so I set up a virtual machine for it, then found I could not reach it remotely. In the end, Claude Code covered what I needed. The lesson I kept: the two-hour limit exists for a reason, and the teardown was worth more than the installation.

By the autumn, OpenClaw was still releasing updates but was no longer the center of attention.

**September to November 2026: personal agents and bots.** Over a few weeks, large companies launched personal assistants and bots one after another, including Meta's Muse, OpenAI's Dots, Alibaba's Qwen moving toward a personal agent, and xAI's Grok Bot. The product question shifted from "can an agent do tasks" to "who owns the always-on assistant that lives where users already are". If you are reading this later, there is probably a newer wave. Run the same four questions on it.
