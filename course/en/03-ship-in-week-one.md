---
id: "03"
title: "Ship in Week One"
summary: "Stop preparing. Build three small, complementary AI products and put them online."
time: "2 to 6 weeks"
output: "Three live products, each with a decision record"
---

# Module 3 · Ship in Week One

## Why this module

This is the module the whole course is built around. My biggest regret is how long I spent "learning AI" before building anything. Months of reading produced almost nothing I could show. The first weekend of building produced a live product, a working understanding of RAG and prompts, and a story I told in every interview afterwards.

Building does three things reading cannot:

- It forces you to learn the concepts you actually need, in the order you need them.
- It gives you failures. Failures are where product judgment comes from.
- It gives you evidence. "I built and shipped this" beats "I have studied this" in every interview.

## The method

### Choose with three questions

For each project idea, answer:

1. **Whose real problem is this?** Best of all: your own, or one you know closely. You will understand the user and you will tell the story honestly.
2. **What does AI do here, and does it need AI?** If a form or a spreadsheet solves it, choose something else.
3. **Can a first version be live within two weeks?** If not, cut scope until it can.

### Make the three projects complementary

Each project should train a different muscle:

| Project | Trains | Example |
|---|---|---|
| An agent with knowledge and a persona | AI design: prompts, knowledge base, boundaries, what the agent refuses to do | A customer service agent for a restaurant, built on a no-code agent platform |
| A full-stack app | Shipping: UI, backend, database, deployment | A small web app or game that calls a model API |
| A product with a real form-factor decision | Product judgment: why this form, for whom | A tool delivered where the user already is (a mini program, a bot, an email) |

### Start easy, then go deeper

Start the first project on a no-code agent platform. You can focus on the prompt, the knowledge and the workflow without fighting code. For the second and third projects, move to AI coding tools and real deployment. By the end you should have done every step once: describe the product, design the screens, generate the code, connect a database, deploy, share a link.

### Ship means a link someone else can open

Working on your laptop is not shipped. If someone cannot open it from a link, it does not count yet.

### Write a decision record for each project

One page, five headings:

1. The problem and the user
2. What the AI does, and what it deliberately does not do
3. One decision and its trade-off ("I chose X over Y because...")
4. What broke, and how I fixed it
5. If I built it again today, what I would change

Interviewers ask about decisions more than features. This record is what you will talk about.

### No AI project yet? Build one, do not invent one

Many people moving into AI product work are tempted to "package" an AI project on their resume. It does not work. Interviewers always dig into AI projects: "Why did you design it this way?" "How did you evaluate it?" "What went wrong?" An invented project falls apart within two or three questions.

What works is running the method above: pick a real problem, ship a first version someone can open within two weeks, and write the decision record. Then you can explain the "why" behind every line on your resume.

When you pick a project, check that it will hold up in an interview:

- **A trade-off to discuss**: you made at least one "X instead of Y" decision.
- **An evaluation to discuss**: you know how to tell whether it works, even if it is just 20 test questions.
- **A failure to discuss**: you know where it breaks and what you did about it.

This is also the line between polishing and inventing. Describing what you really did more clearly and with more weight is polishing. Describing what you did not do is inventing.

## Tool snapshot (March 2026, check what is current)

This is what I used. Expect several of these to have changed by the time you read this. Ask your tutor to check what is current before you pick.

| Step | What I used then |
|---|---|
| Chat model for thinking and writing | Claude (Sonnet 4.6 or later) |
| No-code agent platform | Coze |
| UI and interaction design | Stitch with Google AI Studio, or v0 |
| Coding | Claude Code, Cursor |
| Cheaper model API inside China | SiliconFlow (GLM or DeepSeek models) |
| Version control | GitHub |
| Free database | Supabase |
| Free hosting and a domain | Vercel |

## Exercise

1. Tell your tutor about yourself and three possible project ideas. Your tutor will run each through the three questions and help you pick a complementary set.
2. For the first project, write a one-paragraph spec with your tutor's help, then build it. Your tutor helps when you are stuck, but you make the decisions.
3. Put it online and paste the link into your learning log.
4. Write the decision record in `my-journey/projects/<project-name>.md` using `templates/decision-record.md`.
5. Repeat for the second and third projects. Before each one, ask your tutor: "What did the last project not train?"

## Check yourself

- Can a stranger open all three of your products from a link?
- For each project, can you state one decision and its trade-off in one sentence?
- Which project taught you the most, and was it the one you expected?

## From my journey

In mid-March 2026 I paused applying and built, over one weekend, a customer service agent for a crab restaurant on a no-code platform. My family runs restaurants, so I knew the user well. I gave it a playful cartoon persona because I imagined children as its customers. Two days later I shipped a lore website and game built with Claude, v0 and Cursor. Then I built a mini program that pushes one AI news item a day, because I wanted something that came to me instead of a feed I had to visit. That form-factor decision became one of my best interview answers.

The mini program is a good example of how fast solutions date. In early 2026 a mini program with push was a reasonable choice. By late 2026, a personal bot or a scheduled task does the same job with far less work. Keep the reasoning; expect the solution to change.
