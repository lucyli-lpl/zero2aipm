#!/usr/bin/env python3
"""Build the zero2aipm course website into docs/.

English is the default at the site root; Chinese lives under /zh/.
Usage: python3 site/build.py   (needs: pip install markdown pyyaml)
"""
import html
import re
import shutil
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = ROOT / "docs"
REPO = "https://github.com/lucyli-lpl/zero2aipm"

UI = {
    "en": {
        "lang_attr": "en",
        "title": "From Zero to AI Product Manager",
        "brand": "zero2aipm",
        "switch_label": "中文",
        "tagline": "An interactive course with an AI agent as your tutor. Learn by shipping, not by reading.",
        "hero_note": "Built from a real path: a fintech PM with a career gap shipped three small AI products in a few weeks and had an AI PM offer six weeks later.",
        "cta_start": "How to start",
        "cta_read": "Read Module 0",
        "cta_github": "View on GitHub",
        "how_title": "How it works",
        "how": [
            ("Fork and open", "Fork the repository and open it in an AI coding agent: Claude Code, Codex, Gemini CLI, Cursor or similar."),
            ("Type start the course", "Your tutor reads the course, asks about your background and teaches one module at a time."),
            ("Do the work yourself", "Each module ends with an exercise on your own files. Your tutor explains, quizzes and reviews. It does not do it for you."),
        ],
        "path_title": "The path",
        "path_sub": "Nine modules. Each one leaves you with something you can show.",
        "you_leave": "You leave with",
        "time": "Time",
        "dated_title": "Why everything has a date",
        "dated_body": "AI tools and buzzwords change every few months. This course teaches the path and the methods. Every tool, model or trend it mentions is dated and used as an example. When you reach it, your tutor checks what is current.",
        "start_title": "Start in three steps",
        "start_steps": [
            "Fork <a href=\"{repo}\">the repository</a>, then clone your fork.",
            "Open the folder in your agent, for example <code>claude</code>, <code>codex</code> or <code>gemini</code>.",
            "Type <code>start the course</code>. Next time, type <code>continue</code>.",
        ],
        "start_note": "Only have a chat app such as ChatGPT or Gemini? Use the paste-in prompt in <a href='{repo}/blob/main/TUTOR_PROMPT.md'>TUTOR_PROMPT.md</a> and paste one module at a time.",
        "footer": "By Lucy Li, AI product manager.",
        "modules": "Modules",
        "prev": "Previous",
        "next": "Next",
        "do_with_claude": "Do this module with your AI tutor: open the repository in your coding agent and type <code>start the course</code> or <code>continue</code>.",
        "home": "Home",
        "terminal": (
            '<div class="you">&gt; start the course</div>'
            '<p class="claude">Welcome. Before Module 0, tell me in two or three sentences: what do you do today, and why AI product work?</p>'
            '<div class="you">&gt; Fintech PM, 6 years. I keep reading about AI but have built nothing.</div>'
            '<p class="claude">Then Module 3 is where you will grow fastest. First, let\'s set up your learning log. <span class="dim">Step 1 of 3 ...</span></p>'
        ),
    },
    "zh": {
        "lang_attr": "zh-CN",
        "title": "从 0 到 AI 产品经理",
        "brand": "zero2aipm",
        "switch_label": "English",
        "tagline": "一门让 AI Agent 当导师的互动课程。靠上线产品来学，而不是靠读。",
        "hero_note": "来自一条真实的路径：一个有空窗期的金融科技产品经理，几周内做出并上线了三个小 AI 产品，六周后拿到 AI 产品经理 offer。",
        "cta_start": "怎么开始",
        "cta_read": "阅读模块 0",
        "cta_github": "在 GitHub 查看",
        "how_title": "怎么学",
        "how": [
            ("Fork 并打开", "Fork 这个仓库，在一个 AI 编程 Agent 里打开：Claude Code、Codex、Gemini CLI、Cursor 等都可以。"),
            ("输入「开始课程」", "AI 导师会读取课程，问问你的背景，然后一次带你学一个模块。"),
            ("自己动手做", "每个模块都以一个在你自己文件上完成的练习结束。AI 导师讲解、出题、点评，但不替你做。"),
        ],
        "path_title": "学习路径",
        "path_sub": "九个模块，每个都让你带走一样能拿出来的东西。",
        "you_leave": "学完你会有",
        "time": "时间",
        "dated_title": "为什么处处标着日期",
        "dated_body": "AI 工具和热词每隔几个月就换一轮。这门课教的是路径和方法。课程里提到的每个工具、模型和趋势都标了日期，作为例子使用。学到那里时，AI 导师会帮你确认现在的情况。",
        "start_title": "三步开始",
        "start_steps": [
            "Fork <a href=\"{repo}\">这个仓库</a>，再克隆你 fork 出来的仓库。",
            "在文件夹里打开你的 Agent，比如 <code>claude</code>、<code>codex</code> 或 <code>gemini</code>。",
            "输入<code>开始课程</code>。下次接着学，输入<code>继续</code>。",
        ],
        "start_note": "只有 ChatGPT、Gemini 这类聊天 App？用 <a href='{repo}/blob/main/TUTOR_PROMPT.md'>TUTOR_PROMPT.md</a> 里的提示词，一次粘贴一个模块来学。",
        "footer": "作者 Lucy Li，AI 产品经理。",
        "modules": "模块",
        "prev": "上一个",
        "next": "下一个",
        "do_with_claude": "和 AI 导师一起学这个模块：在你的编程 Agent 里打开仓库，输入<code>开始课程</code>或<code>继续</code>。",
        "home": "首页",
        "terminal": (
            '<div class="you">&gt; 开始课程</div>'
            '<p class="claude">欢迎。开始模块 0 之前，用两三句话告诉我：你现在做什么，为什么想做 AI 产品？</p>'
            '<div class="you">&gt; 做了 6 年金融科技产品，AI 文章看了很多，但一个东西都没做过。</div>'
            '<p class="claude">那模块 3 会是你成长最快的地方。我们先把学习日志建起来。<span class="dim">第 1 步，共 3 步……</span></p>'
        ),
    },
}


def load_modules(lang):
    mods = []
    for f in sorted((ROOT / "course" / lang).glob("*.md")):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        meta = yaml.safe_load(m.group(1))
        body = m.group(2)
        # drop the first H1; the page template renders the title
        body = re.sub(r"^\s*# .*\n", "", body, count=1)
        content = markdown.markdown(body, extensions=["tables", "fenced_code", "sane_lists"])
        content = content.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
        meta["html"] = content
        meta["slug"] = f.stem
        mods.append(meta)
    return mods


def page(lang, title, body, rel, counterpart, description):
    t = UI[lang]
    other = "zh" if lang == "en" else "en"
    return f"""<!DOCTYPE html>
<html lang="{t['lang_attr']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Noto+Serif+SC:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}assets/style.css">
</head>
<body>
<header class="topbar">
  <a class="brand" href="{rel}{'' if lang == 'en' else 'zh/'}index.html">{t['brand']}</a>
  <nav class="topnav">
    <a href="{REPO}" class="ghost">GitHub</a>
    <a href="{counterpart}" class="lang-switch" data-lang="{other}">{t['switch_label']}</a>
  </nav>
</header>
{body}
<footer class="footer">
  <p>{t['footer']} <a href="https://github.com/lucyli-lpl">@lucyli-lpl</a> · <a href="{REPO}">{REPO.replace('https://', '')}</a></p>
</footer>
<script>
document.querySelectorAll('.lang-switch').forEach(function (a) {{
  a.addEventListener('click', function () {{
    try {{ localStorage.setItem('z2a-lang', a.dataset.lang); }} catch (e) {{}}
  }});
}});
</script>
</body>
</html>
"""


def home(lang, mods):
    t = UI[lang]
    pre = "" if lang == "en" else "zh/"
    rel = "" if lang == "en" else "../"
    how = "".join(
        f'<li><span class="step-no">{i + 1}</span><h3>{h}</h3><p>{p}</p></li>' for i, (h, p) in enumerate(t["how"])
    )
    cards = "".join(
        f"""<a class="card" href="modules/{m['slug']}.html">
  <span class="card-no">{m['id']}</span>
  <h3>{html.escape(m['title'])}</h3>
  <p>{html.escape(m['summary'])}</p>
  <dl><dt>{t['you_leave']}</dt><dd>{html.escape(m['output'])}</dd><dt>{t['time']}</dt><dd>{html.escape(m['time'])}</dd></dl>
</a>"""
        for m in mods
    )
    steps = "".join(f"<li>{s.format(repo=REPO)}</li>" for s in t["start_steps"])
    redirect = ""
    if lang == "en":
        redirect = """<script>
try { if (localStorage.getItem('z2a-lang') === 'zh' && !location.hash) { location.replace('zh/index.html'); } } catch (e) {}
</script>"""
    body = f"""{redirect}
<main>
<div class="hero-wrap">
<section class="hero">
  <p class="eyebrow">zero2aipm</p>
  <h1>{t['title']}</h1>
  <p class="tagline">{t['tagline']}</p>
  <p class="hero-note">{t['hero_note']}</p>
  <div class="cta">
    <a class="btn primary" href="#start">{t['cta_start']}</a>
    <a class="btn" href="modules/00-start-here.html">{t['cta_read']}</a>
    <a class="btn" href="{REPO}">{t['cta_github']}</a>
  </div>
</section>
<div class="terminal" aria-hidden="true">
  <div class="bar"><i></i><i></i><i></i></div>
  <div class="body">{t['terminal']}</div>
</div>
</div>
<section class="block">
  <h2>{t['how_title']}</h2>
  <ol class="how">{how}</ol>
</section>
<section class="block">
  <h2>{t['path_title']}</h2>
  <p class="sub">{t['path_sub']}</p>
  <div class="cards">{cards}</div>
</section>
<section class="block callout">
  <h2>{t['dated_title']}</h2>
  <p>{t['dated_body']}</p>
</section>
<section class="block" id="start">
  <h2>{t['start_title']}</h2>
  <ol class="start">{steps}</ol>
  <p class="sub">{t['start_note'].format(repo=REPO)}</p>
</section>
</main>"""
    counterpart = "zh/index.html" if lang == "en" else "../index.html"
    return page(lang, f"{t['title']} · zero2aipm", body, rel, counterpart, t["tagline"])


def module_page(lang, mods, i):
    t = UI[lang]
    m = mods[i]
    rel = "../" if lang == "en" else "../../"
    side = "".join(
        f'<li{" class=\"active\"" if j == i else ""}><a href="{x["slug"]}.html"><span>{x["id"]}</span><em>{html.escape(x["title"])}</em></a></li>'
        for j, x in enumerate(mods)
    )
    prev_link = f'<a class="pn prev" href="{mods[i - 1]["slug"]}.html"><small>{t["prev"]}</small>{html.escape(mods[i - 1]["title"])}</a>' if i > 0 else "<span></span>"
    next_link = f'<a class="pn next" href="{mods[i + 1]["slug"]}.html"><small>{t["next"]}</small>{html.escape(mods[i + 1]["title"])}</a>' if i < len(mods) - 1 else "<span></span>"
    body = f"""<main class="module-layout">
<aside class="sidebar">
  <a class="back" href="../index.html">{t['home']}</a>
  <p class="side-title">{t['modules']}</p>
  <ol>{side}</ol>
</aside>
<article class="lesson">
  <p class="eyebrow">{t['modules'][:-1] if lang == 'en' else '模块'} {m['id']}</p>
  <h1>{html.escape(m['title'])}</h1>
  <p class="lede">{html.escape(m['summary'])}</p>
  <dl class="meta"><dt>{t['time']}</dt><dd>{html.escape(m['time'])}</dd><dt>{t['you_leave']}</dt><dd>{html.escape(m['output'])}</dd></dl>
  <div class="claude-note">{t['do_with_claude']}</div>
  {m['html']}
  <nav class="prevnext">{prev_link}{next_link}</nav>
</article>
</main>"""
    counterpart = f"../../zh/modules/{m['slug']}.html" if lang == "en" else f"../../modules/{m['slug']}.html"
    return page(lang, f"{m['id']} · {m['title']} · zero2aipm", body, rel, counterpart, m["summary"])


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    shutil.copy(SITE / "style.css", OUT / "assets" / "style.css")
    (OUT / ".nojekyll").write_text("")
    for lang in ("en", "zh"):
        mods = load_modules(lang)
        base = OUT if lang == "en" else OUT / "zh"
        (base / "modules").mkdir(parents=True, exist_ok=True)
        (base / "index.html").write_text(home(lang, mods), encoding="utf-8")
        for i in range(len(mods)):
            (base / "modules" / f"{mods[i]['slug']}.html").write_text(module_page(lang, mods, i), encoding="utf-8")
    print("built", sum(1 for _ in OUT.rglob("*.html")), "pages into", OUT)


if __name__ == "__main__":
    main()
