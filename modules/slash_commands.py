"""Module 1: All Slash Commands — comprehensive training."""

from engine.ui import (
    C, hr_fancy, print_command, print_tip, print_warning, pause,
    info_box, box, menu, hr, print_difficulty, type_text
)
from engine.quiz import Question, FillInQuestion, ScenarioQuestion, run_quiz, run_scenario


COMMAND_CATEGORIES = {
    "🚀 Getting Started": [
        ("/help", "Show all available commands and keyboard shortcuts"),
        ("/init", "Initialize Copilot CLI in a new project — generates AGENTS.md, context files"),
        ("/clear", "Clear the terminal screen"),
        ("/exit or /quit", "Exit the Copilot CLI session"),
        ("/login", "Log in to your GitHub account"),
        ("/logout", "Log out of your GitHub account"),
    ],
    "🤖 Agent & AI Control": [
        ("/agent", "List, select, or manage agents — built-in and custom"),
        ("/skills", "Browse and manage available skills — your AI's capabilities"),
        ("/model", "Switch between AI models (Sonnet, Haiku, Opus, GPT, Gemini)"),
        ("/plan", "Enter Plan mode — AI generates a plan, you approve before execution"),
        ("/delegate", "Hand off complex tasks to a dedicated coding agent"),
        ("/fleet", "Manage fleet of background agents (list, status, results)"),
        ("/tasks", "View and manage background tasks and their statuses"),
    ],
    "🔌 Extensions & Integration": [
        ("/mcp", "Manage Model Context Protocol servers — add, remove, list"),
        ("/plugin", "Manage CLI plugins"),
        ("/ide", "Connect to your IDE for enhanced integration"),
        ("/lsp", "Configure Language Server Protocol for code intelligence"),
        ("/terminal-setup", "Configure shell integration (hooks, keybindings)"),
    ],
    "📝 Code Review & Diff": [
        ("/review", "Review code changes with AI — staged, unstaged, or branch diffs"),
        ("/diff", "Show diffs of current changes for review"),
    ],
    "📂 Context & Navigation": [
        ("/context", "Visualize token usage and context window — see what AI knows"),
        ("/compact", "Compress conversation context to free up token space"),
        ("/add-dir", "Add additional directories to the AI's context"),
        ("/list-dirs", "List all directories currently in context"),
        ("/cwd", "Show or change the current working directory"),
    ],
    "🔒 Permissions & Safety": [
        ("/allow-all", "Allow all tool calls without confirmation for this session"),
        ("/reset-allowed-tools", "Reset all tool permissions — re-enable confirmation prompts"),
    ],
    "💾 Session Management": [
        ("/session", "View session info, history, or switch sessions"),
        ("/resume", "Resume a previous session — continue where you left off"),
        ("/rename", "Rename the current session for easier identification"),
        ("/share", "Share your session (generates a shareable link)"),
    ],
    "⚙️ Configuration": [
        ("/instructions", "View or manage custom instruction files"),
        ("/experimental", "Toggle experimental features on or off"),
        ("/theme", "Change the CLI color theme"),
        ("/streamer-mode", "Toggle streamer mode — hides sensitive information"),
        ("/update", "Check for and install CLI updates"),
        ("/user", "View current user information and authentication status"),
    ],
    "📊 Information": [
        ("/usage", "Show API usage statistics and rate limits"),
        ("/changelog", "View recent changes and updates to the CLI"),
        ("/feedback", "Submit feedback about the CLI to the team"),
    ],
}


def run_lesson(progress):
    """Run the slash commands training module."""
    progress.visit_section("slash_commands")

    while True:
        hr_fancy("📖 Module 1: Slash Commands", C.BRIGHT_CYAN)
        print(f"\n  {C.WHITE}Master every slash command in the Copilot CLI.{C.RESET}")
        print(f"  {C.DIM}There are 35+ commands organized into categories.{C.RESET}\n")

        result = menu([
            ("📚 Browse All Commands (Reference)", "browse"),
            ("🎓 Guided Lesson: Essential Commands", "lesson_essential"),
            ("🎓 Guided Lesson: Power User Commands", "lesson_power"),
            ("🎓 Guided Lesson: Session & Context", "lesson_session"),
            ("🎯 Quiz: Test Your Knowledge", "quiz"),
            ("🧩 Scenario Challenge", "scenario"),
        ], "Choose activity")

        if result is None or result == "quit":
            return
        elif result == "browse":
            _browse_commands(progress)
        elif result == "lesson_essential":
            _lesson_essential(progress)
        elif result == "lesson_power":
            _lesson_power(progress)
        elif result == "lesson_session":
            _lesson_session(progress)
        elif result == "quiz":
            _run_quiz(progress)
        elif result == "scenario":
            _run_scenario(progress)


def _browse_commands(progress):
    """Browse all commands by category."""
    while True:
        hr_fancy("📚 Command Reference", C.BRIGHT_BLUE)
        categories = list(COMMAND_CATEGORIES.keys())
        result = menu(
            [(cat, cat) for cat in categories] + [("🔍 Search commands", "search")],
            "Select category"
        )

        if result is None:
            return
        if result == "search":
            try:
                query = input(f"\n  {C.BRIGHT_WHITE}Search ▸ {C.RESET}").strip().lower()
            except EOFError:
                continue
            print()
            found = 0
            for cat, cmds in COMMAND_CATEGORIES.items():
                for cmd, desc in cmds:
                    if query in cmd.lower() or query in desc.lower():
                        print_command(cmd, desc)
                        found += 1
            if found == 0:
                print(f"  {C.DIM}No commands matching '{query}'{C.RESET}")
            pause()
            continue

        print()
        hr_fancy(result, C.BRIGHT_BLUE)
        print()
        for cmd, desc in COMMAND_CATEGORIES[result]:
            print_command(cmd, desc)
        print()
        pause()


def _lesson_essential(progress):
    """Guided lesson: essential commands."""
    hr_fancy("🎓 Essential Commands", C.BRIGHT_GREEN)
    print_difficulty("beginner")

    type_text("\n  Let's learn the commands you'll use every single day.", color=C.WHITE)
    pause()

    # Lesson 1: Help & Navigation
    info_box("1️⃣  /help — Your Lifeline", f"""The /help command shows ALL available commands and shortcuts.

{C.GREEN}Usage:{C.RESET}  Just type /help and press Enter.

{C.YELLOW}Pro tip:{C.RESET} When you're lost, /help is always your first stop.
It shows commands, keyboard shortcuts, and available modes.""")
    pause()

    info_box("2️⃣  /model — Choose Your AI", f"""Switch between AI models depending on your task.

{C.GREEN}Usage:{C.RESET}  /model
  Then select from available models:
  • Claude Sonnet — fast, great for most tasks
  • Claude Haiku — fastest, good for simple queries
  • Claude Opus — most capable, best for complex reasoning
  • GPT models — alternative AI providers
  • Gemini — Google's AI model

{C.YELLOW}Pro tip:{C.RESET} Use Haiku for quick questions, Opus for architecture decisions.""")
    pause()

    info_box("3️⃣  /plan — Think Before Acting", f"""Enter Plan mode where the AI creates a plan before executing.

{C.GREEN}Usage:{C.RESET}  /plan
  Or press Shift+Tab to cycle through modes.

{C.YELLOW}When to use:{C.RESET}
  • Complex refactoring that touches many files
  • When you want to review changes before they happen
  • Architecture decisions that need careful thought

The AI will outline steps and wait for your approval.""")
    pause()

    info_box("4️⃣  /review — AI Code Review", f"""Get an AI-powered code review of your changes.

{C.GREEN}Usage:{C.RESET}
  /review              — review staged changes
  /review --diff main  — review against a branch

{C.YELLOW}What it checks:{C.RESET}
  • Bugs and logic errors
  • Security vulnerabilities
  • Performance issues
  • Only flags things that MATTER (no style nits!)""")
    pause()

    info_box("5️⃣  /clear, /exit, /quit", f"""{C.GREEN}/clear{C.RESET} — Clears the terminal screen (like Ctrl+L)
{C.GREEN}/exit{C.RESET}  — Exit the CLI session
{C.GREEN}/quit{C.RESET}  — Same as /exit

{C.YELLOW}Note:{C.RESET} Your session is automatically saved.
Use /resume next time to pick up where you left off.""")
    pause()

    progress.complete_lesson("slash_essential")
    progress.complete_lesson("slash_1")
    progress.complete_lesson("slash_2")
    progress.complete_lesson("slash_3")
    progress.complete_lesson("slash_4")
    progress.complete_lesson("slash_5")
    progress.check_module_achievements()


def _lesson_power(progress):
    """Guided lesson: power user commands."""
    hr_fancy("🎓 Power User Commands", C.BRIGHT_GREEN)
    print_difficulty("intermediate")

    type_text("\n  Level up with commands that 10x your productivity.", color=C.WHITE)
    pause()

    info_box("1️⃣  /agent — Summon Specialists", f"""Agents are specialized AI workers with different capabilities.

{C.GREEN}Usage:{C.RESET}
  /agent              — list available agents
  /agent explore      — use the fast code exploration agent
  /agent task         — use the task execution agent

{C.YELLOW}Built-in agents:{C.RESET}
  • explore       — fast codebase Q&A (uses Haiku)
  • task          — run commands, tests, builds
  • general-purpose — full capability agent (uses Sonnet)
  • code-review   — focused code review agent

{C.CYAN}Custom agents:{C.RESET} defined in ~/.copilot/agents/ or .github/agents/""")
    pause()

    info_box("2️⃣  /mcp — Extend AI Powers", f"""MCP (Model Context Protocol) connects AI to external tools.

{C.GREEN}Usage:{C.RESET}
  /mcp                     — list connected MCP servers
  /mcp add <name> <cmd>    — add a new MCP server

{C.YELLOW}Default:{C.RESET} GitHub MCP server is built-in (search, PRs, issues)

{C.CYAN}Examples:{C.RESET}
  /mcp add db sqlite3 mydb.sqlite
  /mcp add api node my-api-server.js

MCP servers are configured in mcp-config.json""")
    pause()

    info_box("3️⃣  /delegate — Hand Off Complex Tasks", f"""Spawn a dedicated coding agent for complex, multi-step tasks.

{C.GREEN}Usage:{C.RESET}  /delegate "refactor the auth module to use JWT"

{C.YELLOW}When to use:{C.RESET}
  • Large refactoring that needs many file changes
  • Tasks that require focused, uninterrupted work
  • When you want the AI to work independently

The agent works in the background while you continue.""")
    pause()

    info_box("4️⃣  /skills — AI Capabilities", f"""Skills are specialized capabilities available to the AI.

{C.GREEN}Usage:{C.RESET}
  /skills              — list all available skills
  /skills <name>       — invoke a specific skill

{C.YELLOW}Skills can:{C.RESET}
  • Process specific file types (PDF, XLSX)
  • Run specialized analysis workflows
  • Connect to external services

Custom skills defined in agent config files.""")
    pause()

    info_box("5️⃣  /fleet & /tasks — Parallel Power", f"""Manage multiple background agents and tasks.

{C.GREEN}/fleet{C.RESET}  — manage fleet of background agents
{C.GREEN}/tasks{C.RESET}  — view and manage background tasks

{C.YELLOW}Use cases:{C.RESET}
  • Run multiple analyses in parallel
  • Monitor long-running tasks
  • Check results of delegated work""")
    pause()

    progress.complete_lesson("slash_power")
    progress.complete_lesson("slash_6")
    progress.complete_lesson("slash_7")
    progress.complete_lesson("slash_8")
    progress.complete_lesson("slash_9")
    progress.complete_lesson("slash_10")
    progress.check_module_achievements()


def _lesson_session(progress):
    """Guided lesson: session & context commands."""
    hr_fancy("🎓 Session & Context Mastery", C.BRIGHT_GREEN)
    print_difficulty("advanced")

    type_text("\n  Master context management — the key to expert-level usage.", color=C.WHITE)
    pause()

    info_box("1️⃣  /context — See What AI Knows", f"""Visualize exactly what's in the AI's context window.

{C.GREEN}Usage:{C.RESET}  /context

{C.YELLOW}Shows:{C.RESET}
  • Token count and percentage used
  • Files currently in context
  • Conversation history size
  • System instructions size

{C.RED}Why it matters:{C.RESET} When context fills up, AI loses
earlier information. Monitor this to stay effective.""")
    pause()

    info_box("2️⃣  /compact — Context Compression", f"""Summarize the conversation to free up context space.

{C.GREEN}Usage:{C.RESET}  /compact

{C.YELLOW}What happens:{C.RESET}
  1. AI summarizes the conversation so far
  2. Old messages are replaced with the summary
  3. You regain context space for new work

{C.RED}When to use:{C.RESET}
  • Getting "context window full" warnings
  • After completing a subtask, before starting another
  • Long sessions with lots of file exploration""")
    pause()

    info_box("3️⃣  /session & /resume — Continuity", f"""{C.GREEN}/session{C.RESET}  — view current session info and history
{C.GREEN}/resume{C.RESET}   — resume a previous session

{C.YELLOW}Session features:{C.RESET}
  • Sessions auto-save on exit
  • Resume with /resume or --continue flag
  • Each session has an ID and optional name

{C.CYAN}CLI flag:{C.RESET}  copilot --continue  (resumes last session)""")
    pause()

    info_box("4️⃣  /share & /rename", f"""{C.GREEN}/share{C.RESET}   — generate a shareable link for your session
{C.GREEN}/rename{C.RESET}  — give your session a descriptive name

{C.YELLOW}Tips:{C.RESET}
  • Name sessions for easy identification: /rename "auth refactor"
  • Share sessions for collaboration or debugging""")
    pause()

    info_box("5️⃣  /instructions & /experimental", f"""{C.GREEN}/instructions{C.RESET}   — view/manage custom instruction files
{C.GREEN}/experimental{C.RESET}   — toggle experimental features

{C.YELLOW}Instruction files (loaded automatically):{C.RESET}
  • CLAUDE.md, GEMINI.md, AGENTS.md (repo root)
  • .github/copilot-instructions.md
  • .github/instructions/*.instructions.md
  • ~/.copilot/copilot-instructions.md (global)

{C.CYAN}Experimental features:{C.RESET} Autopilot mode, new tools, etc.""")
    pause()

    info_box("6️⃣  More Useful Commands", f"""{C.GREEN}/usage{C.RESET}           — API usage stats and rate limits
{C.GREEN}/changelog{C.RESET}       — see what's new in the CLI
{C.GREEN}/feedback{C.RESET}        — submit feedback to the team
{C.GREEN}/theme{C.RESET}           — change color theme
{C.GREEN}/streamer-mode{C.RESET}   — hide sensitive info for streaming
{C.GREEN}/update{C.RESET}          — check for CLI updates
{C.GREEN}/user{C.RESET}            — view auth status
{C.GREEN}/login /logout{C.RESET}   — manage authentication
{C.GREEN}/allow-all{C.RESET}       — skip confirmation for tool calls
{C.GREEN}/reset-allowed-tools{C.RESET} — re-enable confirmations
{C.GREEN}/add-dir{C.RESET}         — add directories to context
{C.GREEN}/list-dirs{C.RESET}       — see directories in context
{C.GREEN}/cwd{C.RESET}             — show/change working directory
{C.GREEN}/lsp{C.RESET}             — configure language server
{C.GREEN}/ide{C.RESET}             — connect to IDE
{C.GREEN}/plugin{C.RESET}          — manage plugins
{C.GREEN}/diff{C.RESET}            — show current diffs
{C.GREEN}/terminal-setup{C.RESET}  — configure shell integration""")
    pause()

    progress.complete_lesson("slash_session")
    progress.complete_lesson("slash_commands")
    progress.complete_lesson("slash_11")
    progress.complete_lesson("slash_12")
    progress.complete_lesson("slash_13")
    progress.complete_lesson("slash_14")
    progress.complete_lesson("slash_15")
    progress.check_module_achievements()


def _run_quiz(progress):
    questions = [
        Question(
            "Which command shows all available commands and shortcuts?",
            ["/list", "/help", "/commands", "/info"],
            1,
            "/help is always your first stop when lost.",
            "beginner", "It's the most universal command in any CLI."
        ),
        Question(
            "What does /compact do?",
            ["Minifies your code", "Compresses the conversation to free context space",
             "Reduces file sizes", "Enables compact display mode"],
            1,
            "/compact summarizes conversation history to reclaim context tokens.",
            "intermediate", "Think about what fills up during a long AI conversation."
        ),
        Question(
            "Which command lets you resume a previous session?",
            ["/continue", "/resume", "/restore", "/reload"],
            1,
            "/resume lets you pick up where you left off. Also: copilot --continue",
            "beginner", "The name is intuitive — you want to continue working."
        ),
        Question(
            "What does /delegate do?",
            ["Assigns permissions to another user", "Spawns a coding agent for complex tasks",
             "Forwards your query to support", "Delegates to a different AI model"],
            1,
            "/delegate creates a focused agent that works independently on your task.",
            "intermediate", "Think of handing work to a specialized team member."
        ),
        Question(
            "How do you add a custom MCP server?",
            ["/mcp install <server>", "/mcp add <name> <command>",
             "/add-mcp <url>", "/plugin add-mcp <name>"],
            1,
            "MCP servers are added with /mcp add, providing a name and command.",
            "advanced", "The command follows the pattern: /mcp add <name> <cmd>"
        ),
        Question(
            "Which command visualizes your token usage?",
            ["/tokens", "/usage", "/context", "/stats"],
            2,
            "/context shows exactly what's in the AI's context window.",
            "intermediate", "It shows the context WINDOW, not API usage stats."
        ),
        Question(
            "What does /allow-all do?",
            ["Allows all users to access the CLI", "Permits all file operations",
             "Skips confirmation prompts for tool calls", "Enables all experimental features"],
            2,
            "Also known as --yolo mode. Use with caution!",
            "intermediate", "Think about what normally requires confirmation."
        ),
        Question(
            "Which command enters Plan mode?",
            ["/think", "/plan", "/strategy", "/outline"],
            1,
            "In Plan mode, AI creates a plan and waits for approval before executing.",
            "beginner", "The mode where AI plans before acting."
        ),
        FillInQuestion(
            "Type the command to switch AI models:",
            ["/model"],
            "Just type /model to see available models and switch.",
            "beginner", "It directly names what you're changing."
        ),
        Question(
            "What are the built-in agents?",
            ["explore, task, general-purpose, code-review",
             "search, build, test, deploy",
             "read, write, execute, review",
             "fast, standard, premium, expert"],
            0,
            "explore (fast Q&A), task (commands), general-purpose (full), code-review (reviews).",
            "intermediate", "Think about different types of coding activities."
        ),
        ScenarioQuestion(
            "You've been working for 2 hours. The AI starts forgetting context from earlier "
            "in the conversation and gives inconsistent answers.",
            "What command should you use?",
            ["/reset", "/compact", "/clear", "/restart"],
            1,
            "/compact summarizes the conversation, freeing space while preserving key context.",
            "intermediate"
        ),
        ScenarioQuestion(
            "You need to review a large PR that modifies 50 files across your codebase. "
            "You want the AI to focus only on real issues, not style.",
            "Which command is best?",
            ["/diff --all", "/review", "/agent code-review", "/delegate 'review PR'"],
            1,
            "/review analyzes changes focusing on bugs, security, and logic — not style.",
            "advanced"
        ),
    ]

    run_quiz(questions, progress, "slash_commands", "Slash Commands Quiz")


def _run_scenario(progress):
    scenario = {
        "id": "slash_workflow",
        "title": "New Project Setup Workflow",
        "description": "You just cloned a new repository and need to set up\n"
                       "Copilot CLI for maximum productivity. Walk through\n"
                       "the ideal setup sequence.",
        "difficulty": "intermediate",
        "steps": [
            {
                "prompt": "First, what's the best command to initialize Copilot in this project?",
                "options": ["/help", "/init", "/setup", "/start"],
                "correct": 1,
                "success_msg": "✓ /init sets up project-specific config and context!",
                "fail_msg": "/init is the right choice — it generates AGENTS.md and context files.",
                "explanation": "/init analyzes your project and creates helpful configuration files."
            },
            {
                "prompt": "You want to see what AI model you're using and maybe switch. What command?",
                "options": ["/ai", "/model", "/config model", "/settings"],
                "correct": 1,
                "success_msg": "✓ /model shows and lets you switch between available models!",
                "fail_msg": "Use /model to see and switch AI models.",
                "explanation": "Different models have different strengths. Opus for complex tasks, Haiku for speed."
            },
            {
                "prompt": "You have a project-specific MCP server to add. What command?",
                "options": ["/plugin add mcp", "/mcp add myserver ./server.js", "/add-mcp", "/config mcp"],
                "correct": 1,
                "success_msg": "✓ /mcp add with name and command is the right syntax!",
                "fail_msg": "The pattern is /mcp add <name> <command>.",
                "explanation": "MCP servers extend the AI's capabilities with custom tools."
            },
            {
                "prompt": "Before making changes, you want the AI to plan first. What do you do?",
                "options": ["Ask it to plan", "/plan", "/mode planning", "/think first"],
                "correct": 1,
                "success_msg": "✓ /plan enters Plan mode — AI proposes, you approve!",
                "fail_msg": "/plan is the command for Plan mode.",
                "explanation": "Plan mode adds a safety layer — the AI won't execute until you approve."
            },
            {
                "prompt": "After a long session, you want to save context for tomorrow. What do you do?",
                "options": ["/save", "/export", "Just exit — sessions auto-save, use /resume tomorrow", "/backup"],
                "correct": 2,
                "success_msg": "✓ Sessions auto-save! Use /resume or --continue to pick up later.",
                "fail_msg": "Sessions are automatically saved. Use /resume next time.",
                "explanation": "You can also /rename the session for easy identification."
            },
        ]
    }
    run_scenario(scenario, progress)
