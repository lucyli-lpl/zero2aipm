---
id: "06"
title: "Industry Crash Course"
summary: "AI is general, but AI products live inside industries. Learn a new industry well enough for an interview in one or two days."
time: "1 to 2 days per industry"
output: "A one-page industry brief with three AI opportunities"
---

# Module 6 · Industry Crash Course

## Why this module

When I interviewed for AI product roles, almost every company was in a different industry: fast-moving consumer goods, B2B sales software, food delivery, restaurants, financial technology. AI techniques are general. AI products are not. An interviewer will not ask "what is RAG?" nearly as often as "where would you use AI in our business?"

You cannot become an expert in every industry before an interview. You can learn enough, in a day or two, to talk about the business the way the people inside it do.

## The method: a six-part brief

For each industry, fill in these six parts:

1. **The core business flow.** Who does what, in what order, from the first step to money coming in. Draw it as a chain of five to eight steps.
2. **The key metrics.** The three to five numbers the business lives by.
3. **The decision pain points.** Where people make costly decisions by gut feel, with missing data, or too slowly. This is where AI usually fits.
4. **Where AI fits.** Two or three concrete scenarios tied to specific steps and pain points. For each, say what the AI does and what a person still decides.
5. **What a PM must understand.** Constraints that change the design: regulation, data access, who the real user is, how the product is sold.
6. **Five questions before recommending AI.** Does this need AI, or would a simpler tool work? What is the human-AI relationship? Is there data, and can a data flywheel form? How will users come to trust it? How does it turn into value: lower cost or new growth?

Then add one line on the company itself: where it sits in this industry, and what its leaders have said publicly about AI.

## Worked examples (from my 2026 interview prep, simplified)

**Fast-moving consumer goods, route to market.** Flow: manufacturer, distributors, sales reps visiting stores, store shelves, consumers. Metrics: distribution coverage, shelf share, out-of-stock rate, rep productivity. Pain points: deciding which stores to visit and what to push, checking shelf compliance by hand. AI fits: computer vision on shelf photos for compliance and stock, demand forecasting per store, suggested visit routes and orders. PM must understand: reps are the real users, and if the tool slows their visits they will not use it.

**B2B sales, go to market.** Flow: lead, qualification, meetings, proposal, negotiation, close, renewal. Metrics: pipeline value, conversion by stage, sales cycle length. Pain points: reps spend time on the wrong leads and on admin. AI fits: lead scoring and account research, meeting preparation and follow-up drafts, pipeline risk alerts. PM must understand: data lives in the CRM, and reps distrust scores they cannot explain.

**Food delivery, merchant side.** Flow: merchant onboarding, menu and store setup, promotions, orders, delivery, ratings. Metrics: merchant activation, order volume, rating, retention. Pain points: new stores do not know how to set up menus and images or which promotions to join. Account managers cover too many merchants. AI fits: generating and scoring menu images, explaining platform rules in plain language, prioritizing which merchants an account manager should help this week. PM must understand: margins are thin, and merchants judge any tool by whether orders go up.

## Exercise

1. Pick a company you would like to interview with, or one in the industry you know least.
2. Ask Claude to research the industry and company with you. Claude will search for current information and show sources. Fill in the six parts yourself, using what you find.
3. Save it as `my-journey/industries/<industry>.md` using `templates/industry-brief.md`.
4. Practice: ask Claude to play the interviewer and ask, "Where would you use AI in our business?" Answer out loud or in writing in under two minutes.
5. Ask Claude to point out where your answer sounded like an outsider.

## Check yourself

- Can you draw the industry's core flow from memory?
- Is each of your AI scenarios tied to a specific step and a specific metric?
- Did you say what a person still decides in each scenario?

## From my journey

I used the same structure for every new industry. The brief for consumer goods route to market took most of a day. By the fourth industry, a brief took a few hours, because the six parts made me ask the right questions instead of reading everything. In interviews, being able to say "your reps are the real users, so the AI has to save them time on each visit" did more than any technical answer.
