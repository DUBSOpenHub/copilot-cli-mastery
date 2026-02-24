# 🎓 Copilot CLI Mastery — Interactive Training System

> **From Zero to CLI Wizard** — Master every feature of the GitHub Copilot CLI through interactive lessons, quizzes, scenarios, and challenges.

## 🚀 Quick Start

```bash
python3 mastery.py
```

No dependencies required — runs on Python 3.6+ with only standard library modules.

## 📚 What's Inside

### 8 Comprehensive Training Modules

| # | Module | Topics | Difficulty |
|---|--------|--------|------------|
| 1 | **Slash Commands** | All 35+ commands, organized by category | 🟢→🔴 |
| 2 | **Keyboard Shortcuts** | 20+ shortcuts with muscle-memory training | 🟢→🟡 |
| 3 | **Interaction Modes** | Interactive, Plan, Autopilot — when to use each | 🟢→🟡 |
| 4 | **Agent System** | Built-in agents, custom agents, orchestration | 🟡→🔴 |
| 5 | **Skills System** | What skills are, how to create and use them | 🟡→🔴 |
| 6 | **MCP Integration** | GitHub MCP server, custom servers, config | 🟡→💎 |
| 7 | **Advanced Techniques** | Context management, instructions, workflows | 🔴→💎 |
| 8 | **Configuration** | config.json, env vars, LSP, permissions | 🟡→💎 |

### Learning Activities

- **📖 Guided Lessons** — step-by-step walkthroughs with examples
- **🎯 Quizzes** — multiple choice, fill-in-the-blank, scenario-based
- **🧩 Scenario Challenges** — real-world workflow simulations
- **📋 Quick Reference** — comprehensive cheat sheets
- **🎓 Final Exam** — 20-question certification test

### Gamification

- **⭐ XP System** — earn experience points for every activity
- **📈 10 Levels** — Newcomer → Apprentice → ... → CLI Wizard
- **🏆 20+ Achievements** — unlock badges for milestones
- **🔥 Streak Tracking** — bonus rewards for consecutive correct answers
- **💾 Persistent Progress** — your progress saves automatically

## 🏗️ Architecture

```
mastery.py              # Main entry point & navigation
├── engine/
│   ├── ui.py           # Terminal UI (colors, boxes, menus, animations)
│   ├── progress.py     # XP, levels, achievements, persistence
│   └── quiz.py         # Quiz engine (multiple question types)
└── modules/
    ├── slash_commands.py      # Module 1: All slash commands
    ├── keyboard_shortcuts.py  # Module 2: All keyboard shortcuts
    ├── modes.py               # Module 3: Interaction modes
    ├── agents.py              # Module 4: Agent system
    ├── skills.py              # Module 5: Skills system
    ├── mcp.py                 # Module 6: MCP integration
    ├── advanced.py            # Module 7: Advanced techniques
    └── configuration.py       # Module 8: Configuration
```

### Design Principles

- **Zero dependencies** — Python standard library only
- **Modular** — each module is self-contained, easy to extend
- **Progressive** — beginner → intermediate → advanced → expert
- **Interactive** — no walls of text, everything is navigable
- **Persistent** — progress saves to `~/.copilot-mastery-progress.json`

## 📊 Coverage

### Slash Commands (35+)
`/init` `/agent` `/skills` `/mcp` `/plugin` `/model` `/fleet` `/tasks` `/ide` `/diff` `/review` `/lsp` `/terminal-setup` `/allow-all` `/add-dir` `/list-dirs` `/cwd` `/reset-allowed-tools` `/resume` `/rename` `/context` `/usage` `/session` `/compact` `/share` `/help` `/changelog` `/feedback` `/theme` `/update` `/experimental` `/clear` `/instructions` `/streamer-mode` `/exit` `/quit` `/login` `/logout` `/plan` `/user` `/delegate`

### Keyboard Shortcuts (20+)
`@` file mentions · `Ctrl+S` · `Shift+Tab` · `Ctrl+T` · `Ctrl+O` · `Ctrl+E` · `↑↓` history · `!` shell bypass · `Esc` · `Ctrl+C` · `Ctrl+D` · `Ctrl+L` · `Ctrl+X→Ctrl+E` · `Ctrl+A` · `Ctrl+H` · `Ctrl+W` · `Ctrl+U` · `Ctrl+K` · `Meta+←→`

### Modes
Interactive · Plan · Autopilot (experimental)

### Full Feature Coverage
Agents · Skills · MCP · Custom Instructions · LSP · Session Management · Context Management · Code Review · Permissions · Configuration

## 🎮 How to Use

1. **Run** `python3 mastery.py`
2. **Choose a module** from the main menu
3. **Pick an activity** — lesson, quiz, or scenario
4. **Earn XP** and unlock achievements as you learn
5. **Take the Final Exam** when you're ready for certification

## 💡 Tips

- Start with modules 1-3 if you're new
- Use the Quick Reference Card as a cheat sheet
- Take quizzes to reinforce what you've learned
- Scenarios simulate real-world workflows
- The Final Exam requires 80%+ to pass
- Your progress persists between sessions
