[English](README.md) | **简体中文**

# zero2aipm · 从 0 到 AI 产品经理

一门互动课程：让 AI Agent 当你的导师，边做边学，转型做 AI 产品经理。Claude Code、Codex、Gemini CLI、Cursor 等编程 Agent 都能用；只有聊天 App 的话，也可以用一段提示词来学。

它来自一条真实的路径：2026 年 3 月，一个有空窗期的金融科技产品经理不再只是读 AI 文章，而是用几周时间做出并上线了三个小 AI 产品，六周后拿到了 AI 产品经理的 offer。这门课就是那条路，整理过后让你走得更快。

**课程网站：** <https://lucyli-lpl.github.io/zero2aipm/>

## 它有什么不同

- **教路径和方法，不堆知识。** AI 工具和热词每隔几个月就换一轮。课程里提到的每个工具、模型和趋势都标了日期，作为方法的例子。学到那里时，AI 导师会帮你确认现在的情况。
- **边做边学。** 每个模块都以一个在你自己文件上完成的练习结束：一个上线的产品、一套评测集、一份拆解、一页行业简报。AI 导师负责讲解、提问和点评，但不会替你做。
- **为转行的人设计。** 它覆盖了大多数 AI 课程跳过的部分：怎么选能变成面试故事的项目、面试前怎么速成一个行业、怎么把笔记变成简历。

## 课程模块

| # | 模块 | 学完你会有 |
|---|---|---|
| 0 | 从这里开始 | 一份学习日志 |
| 1 | 把 AI 当导师 | 20 分钟学会任何新概念的方法 |
| 2 | 建立地图 | 个人名词库和一张领域全景图 |
| 3 | 第一周就上线 | 三个上线的小 AI 产品 |
| 4 | 带着项目学方法论 | 自己产品的评测集和错误分析 |
| 5 | 追热点不被淹没 | 判断热点的习惯和一份产品拆解 |
| 6 | 行业速成 | 一页能带进面试的行业简报 |
| 7 | 记录与沉淀 | 心得、公开作品和可复用的资产 |
| 8 | 进入求职 | 用你的证据写出的简历和面试准备 |

## 怎么开始

你需要一个能在文件夹里读写文件的 AI 编程 Agent，下面任何一个都行：

| Agent | 怎么读取课程说明 |
|---|---|
| Claude Code | 读 `CLAUDE.md`，它会加载 `AGENTS.md` |
| OpenAI Codex | 读 `AGENTS.md` |
| Cursor | 读 `AGENTS.md` |
| Gemini CLI | `.gemini/settings.json` 让它读 `AGENTS.md`，`GEMINI.md` 作为备用 |
| 其他 | 大多数 Agent 都读 `AGENTS.md`。如果你的不读，就对它说：「读取 AGENTS.md 并照着做。」 |

1. Fork 这个仓库（这样你的学习成果能保存在自己的仓库里），再克隆你 fork 出来的仓库：
   ```bash
   git clone https://github.com/<你的用户名>/zero2aipm.git
   cd zero2aipm
   ```
2. 在这个文件夹里打开你的 Agent，比如 `claude`、`codex` 或 `gemini`。
3. 输入「开始课程」。

Agent 会读取 `AGENTS.md` 里的导师说明，问问你的背景，然后一次带你学一个模块。你的成果都放在 `my-journey/` 里。下次想接着学，输入「继续」就行。

**只有聊天 App**（ChatGPT、Gemini、Claude、豆包、千问）？用 [`TUTOR_PROMPT.md`](TUTOR_PROMPT.md) 里的提示词，一次粘贴一个模块来学。也可以直接在网站上或 `course/zh/` 里阅读所有模块。

## 仓库结构

```
course/en/      九个模块，英文版
course/zh/      九个模块，中文版
templates/      学习日志、名词库、决策记录、评测集、拆解和行业简报的模板
AGENTS.md       给任何编程 Agent 的导师说明（CLAUDE.md 和 GEMINI.md 都指向它）
TUTOR_PROMPT.md 聊天 App 用的提示词
site/           网站源码（运行：python3 site/build.py）
docs/           生成的网站，由 GitHub Pages 发布
skills/         简历和面试的配套 skill（即将加入）
```

## 保持更新

方法过时得慢，工具和趋势过时得快。发现过时的内容，欢迎提 issue 或 pull request。

## 作者

Lucy Li（[@lucyli-lpl](https://github.com/lucyli-lpl)），AI 产品经理。相关作品：[ai-pm-fieldbook](https://github.com/lucyli-lpl/ai-pm-fieldbook)、[ai-design-patterns](https://github.com/lucyli-lpl/ai-design-patterns)。
