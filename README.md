**English** | [简体中文](README.zh-CN.md)

# zero2aipm · From Zero to AI Product Manager

An interactive course that teaches you to move into AI product management by doing, with Claude as your tutor.

It is built from a real path: in March 2026 a fintech product manager with a career gap stopped reading about AI, shipped three small AI products in a few weeks, and had an AI product manager offer six weeks later. This course is that path, cleaned up so you can walk it faster.

**Website:** <https://lucyli-lpl.github.io/zero2aipm/>

## What makes it different

- **A path and methods, not a pile of knowledge.** AI tools and buzzwords change every few months. Every tool, model or trend named in the course carries a date and is used as an example of a method. Claude checks what is current when you get there.
- **You learn by doing.** Every module ends with an exercise on your own files: a live product, an eval set, a teardown, an industry brief. Claude explains, asks and reviews. It does not do the work for you.
- **Built for career switchers.** It covers the parts most AI courses skip: choosing projects that become interview stories, learning a new industry before an interview, and turning your notes into a resume.

## The modules

| # | Module | What you leave with |
|---|---|---|
| 0 | Start Here | A learning log |
| 1 | AI as Your Tutor | A way to learn any new concept in 20 minutes |
| 2 | Build Your Map | A personal glossary and a picture of the field |
| 3 | Ship in Week One | Three small, live AI products |
| 4 | Learn the Methods Through Your Project | An eval set and an error analysis for your own product |
| 5 | Chase a Trend Without Drowning | A trend triage habit and one product teardown |
| 6 | Industry Crash Course | A one-page industry brief for interviews |
| 7 | Record and Distill | Lessons, published work and reusable assets |
| 8 | Into the Job Hunt | A resume and interview prep built on your evidence |

## How to start

You need [Claude Code](https://claude.com/claude-code), or the Code tab in the Claude desktop app.

1. Fork this repository (so you can keep your own work), then clone your fork:
   ```bash
   git clone https://github.com/<your-username>/zero2aipm.git
   cd zero2aipm
   ```
2. Open Claude Code in the folder:
   ```bash
   claude
   ```
3. Type `start the course`.

Claude reads the course instructions in `CLAUDE.md`, asks about your background and takes you through one module at a time. Your work goes into `my-journey/`. To pick up later, type `continue`.

You can also read every module on the website or in `course/en/` without Claude, but the exercises are designed to be done with it.

## Repository layout

```
course/en/      the nine modules in English
course/zh/      the nine modules in Chinese
templates/      starter files for your learning log, glossary, decision records, evals, teardowns and industry briefs
CLAUDE.md       instructions that make Claude your tutor
site/           website source (run: python3 site/build.py)
docs/           built website, served by GitHub Pages
skills/         companion skills for resumes and interviews (coming)
```

## Keeping it current

Methods age slowly; tools and trends age fast. If you find something out of date, open an issue or a pull request.

## Author

Lucy Li ([@lucyli-lpl](https://github.com/lucyli-lpl)), AI product manager. Related work: [ai-pm-fieldbook](https://github.com/lucyli-lpl/ai-pm-fieldbook), [ai-design-patterns](https://github.com/lucyli-lpl/ai-design-patterns).
