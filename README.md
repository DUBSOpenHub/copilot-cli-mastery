# 🎓 Copilot CLI Mastery

> **From Zero to CLI Wizard** — Learn the GitHub Copilot CLI at your own pace with interactive lessons, quizzes, and hands-on challenges.
>
> <img width="811" height="232" alt="Screenshot 2026-02-24 at 11 45 08 PM" src="https://github.com/user-attachments/assets/29d29246-5931-4218-9639-7d49e8bb064f" />

> ⚡ **Get started fast!** Install the skill and say "cliexpert":
> ```bash
> mkdir -p ~/.copilot/skills/cli-mastery/curriculum && \
>   curl -sSL https://raw.githubusercontent.com/DUBSOpenHub/copilot-cli-mastery/main/SKILL.md \
>     -o ~/.copilot/skills/cli-mastery/SKILL.md && \
>   for f in module-1-slash-commands module-2-keyboard-shortcuts module-3-modes module-4-agents module-5-skills module-6-mcp module-7-advanced module-8-configuration scenarios final-exam; do \
>     curl -sSL "https://raw.githubusercontent.com/DUBSOpenHub/copilot-cli-mastery/main/curriculum/${f}.md" \
>       -o ~/.copilot/skills/cli-mastery/curriculum/${f}.md; done
> ```

## ⚡ Install

```bash
mkdir -p ~/.copilot/skills/cli-mastery/curriculum
curl -sSL https://raw.githubusercontent.com/DUBSOpenHub/copilot-cli-mastery/main/SKILL.md \
  -o ~/.copilot/skills/cli-mastery/SKILL.md
for f in module-1-slash-commands module-2-keyboard-shortcuts module-3-modes module-4-agents module-5-skills module-6-mcp module-7-advanced module-8-configuration scenarios final-exam; do
  curl -sSL "https://raw.githubusercontent.com/DUBSOpenHub/copilot-cli-mastery/main/curriculum/${f}.md" \
    -o ~/.copilot/skills/cli-mastery/curriculum/${f}.md
done
```

Then open the Copilot CLI and say **"cliexpert"** to start training.

## 📚 8 Training Modules

| # | Module | Topics | Difficulty |
|---|--------|--------|------------|
| 1 | **Slash Commands** | All 42 commands across 8 categories | 🟢→🔴 |
| 2 | **Keyboard Shortcuts** | 19 shortcuts with muscle-memory training | 🟢→🟡 |
| 3 | **Interaction Modes** | Ask, Edit, Agent — when to use each | 🟢→🟡 |
| 4 | **Agent System** | Built-in agents, custom agents, orchestration | 🟡→🔴 |
| 5 | **Skills System** | What skills are, how to create and use them | 🟡→🔴 |
| 6 | **MCP Integration** | GitHub MCP server, custom servers, config | 🟡→💎 |
| 7 | **Advanced Techniques** | Context management, prompt engineering, CI/CD | 🔴→💎 |
| 8 | **Configuration** | Settings, themes, keybindings, permissions | 🟡→💎 |

Plus **8 scenario challenges** and a **final exam**.

## 🎮 Features

- **Guided Lessons** — step-by-step walkthroughs with examples
- **Quizzes** — test your knowledge after each module
- **Scenario Challenges** — real-world workflow simulations
- **XP & Leveling** — earn points and level up from Newcomer to CLI Wizard
- **Progress Tracking** — persistent progress via SQL across sessions

## 🏗️ Architecture

```
SKILL.md                 # Slim router (492 tokens) — drives the skill
curriculum/
├── module-1-slash-commands.md
├── module-2-keyboard-shortcuts.md
├── module-3-modes.md
├── module-4-agents.md
├── module-5-skills.md
├── module-6-mcp.md
├── module-7-advanced.md
├── module-8-configuration.md
├── scenarios.md
└── final-exam.md
```

SKILL.md stays under the 500-token budget. Curriculum files are loaded on demand via the `view` tool.

## 📄 License

MIT

---

## 🐙 Built with Love

Created with 💜 by [DUBSOpenHub](https://github.com/DUBSOpenHub) to help more people discover the joy of GitHub Copilot CLI.

Let's build! 🚀✨
