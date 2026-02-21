"""Module 8: Configuration — config files, env vars, permissions."""

from engine.ui import (
    C, hr_fancy, print_tip, pause, info_box, menu, print_difficulty, type_text,
    print_command, print_success, confirm
)
from engine.quiz import Question, ScenarioQuestion, run_quiz, run_scenario


def run_lesson(progress):
    """Run the configuration training module."""
    progress.visit_section("configuration")

    while True:
        hr_fancy("⚙️  Module 8: Configuration", C.BRIGHT_CYAN)
        print(f"\n  {C.WHITE}Configure every aspect of the Copilot CLI.{C.RESET}\n")

        result = menu([
            ("🎓 Guided Lesson: Core Configuration", "lesson_core"),
            ("🎓 Guided Lesson: Permissions & Safety", "lesson_perms"),
            ("🎓 Guided Lesson: LSP & IDE Integration", "lesson_lsp"),
            ("📦 Generate Config Templates", "templates"),
            ("🎯 Quiz: Configuration Knowledge", "quiz"),
            ("🧩 Scenario: Setup Challenge", "scenario"),
        ], "Choose activity")

        if result is None or result == "quit":
            return
        elif result == "lesson_core":
            _lesson_core(progress)
        elif result == "lesson_perms":
            _lesson_perms(progress)
        elif result == "lesson_lsp":
            _lesson_lsp(progress)
        elif result == "templates":
            _generate_templates(progress)
        elif result == "quiz":
            _run_quiz(progress)
        elif result == "scenario":
            _run_scenario(progress)


def _lesson_core(progress):
    hr_fancy("🎓 Core Configuration", C.BRIGHT_GREEN)
    print_difficulty("intermediate")

    type_text("\n  Understand the configuration system top to bottom.", color=C.WHITE)
    pause()

    info_box("config.json", f"""The main configuration file for the Copilot CLI.

{C.GREEN}Location:{C.RESET} ~/.copilot/config.json

{C.YELLOW}Common settings:{C.RESET}
  • Default model selection
  • Theme preferences
  • Logging level
  • Experimental feature flags
  • Default mode (interactive/plan)

{C.CYAN}Tip:{C.RESET} Changes take effect on next CLI start.
Use slash commands for runtime changes.""")
    pause()

    info_box("Environment Variables", f"""Override configuration via environment variables.

{C.GREEN}Key variables:{C.RESET}
  EDITOR              — text editor for Ctrl+X→Ctrl+E
  COPILOT_LOG_LEVEL   — logging verbosity
  GH_TOKEN            — GitHub authentication token
  COPILOT_MODEL       — default AI model

{C.YELLOW}Setting them:{C.RESET}
  export EDITOR=vim
  export COPILOT_LOG_LEVEL=debug

{C.CYAN}In .bashrc/.zshrc:{C.RESET}
  Add export lines to make them permanent.""")
    pause()

    info_box("Logging Levels", f"""Control how much the CLI logs for debugging.

{C.GREEN}Levels:{C.RESET}
  error    — only errors
  warn     — errors + warnings
  info     — normal operation (default)
  debug    — detailed debugging info
  trace    — everything (verbose!)

{C.YELLOW}Setting:{C.RESET}
  COPILOT_LOG_LEVEL=debug copilot

{C.CYAN}When to use debug/trace:{C.RESET}
  • MCP server connection issues
  • Tool execution failures
  • Unexpected AI behavior
  • Filing bug reports""")
    pause()

    progress.complete_lesson("config_core")


def _lesson_perms(progress):
    hr_fancy("🎓 Permissions & Safety", C.BRIGHT_GREEN)
    print_difficulty("advanced")

    type_text("\n  Understand the permission system that keeps you safe.", color=C.WHITE)
    pause()

    info_box("Tool Permission System", f"""By default, the CLI asks for confirmation before risky operations.

{C.GREEN}Confirmation required for:{C.RESET}
  • Editing files
  • Creating files
  • Running shell commands
  • Deleting files

{C.GREEN}No confirmation needed for:{C.RESET}
  • Reading files (view)
  • Searching code (grep, glob)
  • Web searches

{C.YELLOW}Permission commands:{C.RESET}
  /allow-all          — skip all confirmations this session
  /reset-allowed-tools — re-enable confirmations

{C.RED}CLI flags:{C.RESET}
  --allow-all / --yolo — skip confirmations from start""")
    pause()

    info_box("Safety Best Practices", f"""{C.GREEN}1. Start with defaults{C.RESET}
   Leave confirmations ON while learning.

{C.GREEN}2. Use Plan mode for risky changes{C.RESET}
   Review the plan before execution.

{C.GREEN}3. Version control is your safety net{C.RESET}
   Always work in a git repo.
   git stash / git checkout . to undo.

{C.GREEN}4. Use /allow-all only when safe{C.RESET}
   • In containers or sandboxes
   • On throwaway branches
   • With good git history

{C.GREEN}5. /reset-allowed-tools to re-secure{C.RESET}
   If you've been using /allow-all, reset when
   switching to sensitive work.""")
    pause()

    progress.complete_lesson("config_perms")


def _lesson_lsp(progress):
    hr_fancy("🎓 LSP & IDE Integration", C.BRIGHT_GREEN)
    print_difficulty("expert")

    type_text("\n  Connect the CLI to language servers and your IDE.", color=C.WHITE)
    pause()

    info_box("LSP Configuration", f"""Language Server Protocol gives the AI code intelligence.

{C.GREEN}Configuration files:{C.RESET}
  lsp-config.json        — user-level config
  .github/lsp.json       — project-level config

{C.YELLOW}What LSP enables:{C.RESET}
  • Accurate go-to-definition (not just grep)
  • Find all references to a symbol
  • Type information and inference
  • Compile-time error detection
  • Smart symbol search

{C.CYAN}/lsp command:{C.RESET}
  • View current LSP configuration
  • Check which language servers are active
  • Verify connectivity""")
    pause()

    info_box("IDE Integration", f"""{C.GREEN}/ide command:{C.RESET}
  Connect the CLI to your IDE (VS Code, etc.)

{C.YELLOW}Benefits:{C.RESET}
  • Shared context between CLI and IDE
  • Open files from CLI in IDE
  • Use IDE's language server from CLI

{C.CYAN}/terminal-setup:{C.RESET}
  Configure shell integration for:
  • Keybinding setup
  • Shell hooks for context awareness
  • Terminal prompt integration""")
    pause()

    info_box("Additional Configuration", f"""{C.GREEN}/streamer-mode{C.RESET}
  Hides sensitive information for streaming/recording:
  • API keys and tokens
  • File paths that reveal system info
  • Personal identifiers

{C.GREEN}/theme{C.RESET}
  Change the CLI color theme:
  • Dark themes for terminal work
  • Light themes for visibility
  • Custom accent colors

{C.GREEN}/update{C.RESET}
  Check for and install CLI updates.
  Stay current for new features and fixes.

{C.GREEN}/user{C.RESET}
  View your current authentication status.
  Shows GitHub account info, permissions.

{C.GREEN}/login & /logout{C.RESET}
  Manage GitHub authentication.
  /login to authenticate, /logout to sign out.""")
    pause()

    progress.complete_lesson("config_lsp")
    progress.complete_lesson("config")
    progress.check_module_achievements()


def _generate_templates(progress):
    """Generate starter config template files (ported from Codex runner-up)."""
    from pathlib import Path

    hr_fancy("📦 Config Template Generator", C.BRIGHT_GREEN)
    print(f"\n  {C.WHITE}Generate starter configuration files for a Copilot CLI project.{C.RESET}")
    print(f"  {C.DIM}Files will be written to ./templates/ in the project root.{C.RESET}\n")

    if not confirm("Generate config templates?"):
        return

    root = Path(__file__).resolve().parent.parent
    template_dir = root / "templates"
    template_dir.mkdir(parents=True, exist_ok=True)

    (template_dir / "config.json").write_text(
        '{\n'
        '  "model": "claude-sonnet-4",\n'
        '  "logLevel": "info",\n'
        '  "permissions": {"allowAll": false},\n'
        '  "approvedTools": ["bash", "rg", "view"]\n'
        '}\n'
    )
    (template_dir / "mcp-config.json").write_text(
        '{\n'
        '  "servers": [\n'
        '    {"name": "github", "type": "default"},\n'
        '    {"name": "custom", "url": "https://mcp.example.com"}\n'
        '  ]\n'
        '}\n'
    )
    (template_dir / "lsp-config.json").write_text(
        '{\n'
        '  "servers": {\n'
        '    "python": {"command": "pyright-langserver", "args": ["--stdio"]}\n'
        '  }\n'
        '}\n'
    )
    gh = template_dir / ".github"
    gh.mkdir(exist_ok=True)
    (gh / "lsp.json").write_text(
        '{\n'
        '  "workspace": {"diagnostics": true, "formatOnSave": false}\n'
        '}\n'
    )

    print_success("Templates generated in ./templates/:")
    print(f"    {C.GREEN}config.json{C.RESET}          — main CLI config")
    print(f"    {C.GREEN}mcp-config.json{C.RESET}      — MCP server config")
    print(f"    {C.GREEN}lsp-config.json{C.RESET}      — LSP server config")
    print(f"    {C.GREEN}.github/lsp.json{C.RESET}     — project-level LSP config")
    progress.add_xp(30, "Generated config templates")
    pause()


def _run_quiz(progress):
    questions = [
        Question(
            "Where is the main CLI configuration file located?",
            ["/etc/copilot/config.json", "~/.copilot/config.json",
             "~/.config/copilot.json", "/usr/local/copilot/config"],
            1,
            "~/.copilot/config.json is the main configuration file.",
            "intermediate"
        ),
        Question(
            "What does /reset-allowed-tools do?",
            ["Resets all tools to default versions",
             "Re-enables confirmation prompts after /allow-all",
             "Resets tool permissions to admin level",
             "Clears the tool cache"],
            1,
            "It reverses /allow-all — confirmations are required again.",
            "intermediate"
        ),
        Question(
            "Where is project-level LSP configured?",
            [".lsp/config.json", ".github/lsp.json",
             "tsconfig.json", "lsp-config.json"],
            1,
            "Project LSP: .github/lsp.json, User LSP: lsp-config.json",
            "advanced"
        ),
        Question(
            "What does /streamer-mode do?",
            ["Enables streaming responses", "Hides sensitive information for streaming",
             "Optimizes for low-bandwidth", "Enables chat mode"],
            1,
            "Streamer mode hides API keys, paths, and personal info.",
            "beginner"
        ),
        Question(
            "What environment variable controls logging verbosity?",
            ["LOG_LEVEL", "COPILOT_LOG_LEVEL", "DEBUG", "VERBOSE"],
            1,
            "COPILOT_LOG_LEVEL controls logging. Values: error, warn, info, debug, trace.",
            "intermediate"
        ),
        ScenarioQuestion(
            "You're about to do a live coding demo with the Copilot CLI. "
            "You don't want viewers to see your API keys or file paths.",
            "What should you enable?",
            ["/privacy", "/streamer-mode", "/safe-mode", "/demo-mode"],
            1,
            "Streamer mode hides sensitive information during public sessions.",
            "beginner"
        ),
        ScenarioQuestion(
            "You've been using /allow-all for a boilerplate task. Now you're "
            "switching to work on a production deployment script.",
            "What should you do first?",
            ["/reset-allowed-tools", "/plan", "Just be careful", "Start a new session"],
            0,
            "/reset-allowed-tools re-enables confirmations for safety.",
            "intermediate"
        ),
        Question(
            "The --yolo flag is equivalent to which command?",
            ["/experimental", "/allow-all", "/autopilot", "/unsafe"],
            1,
            "--yolo = --allow-all: both skip all confirmation prompts.",
            "intermediate"
        ),
    ]
    run_quiz(questions, progress, "configuration", "Configuration Quiz")


def _run_scenario(progress):
    scenario = {
        "id": "config_setup",
        "title": "Perfect Setup Challenge",
        "description": "Configure the Copilot CLI for a new team project.\n"
                       "Get everything set up correctly from the start.",
        "difficulty": "advanced",
        "steps": [
            {
                "prompt": "First, you want to set coding standards for the whole team. Where do you put them?",
                "options": [
                    "~/.copilot/copilot-instructions.md (personal)",
                    ".github/copilot-instructions.md (repo-level)",
                    "CLAUDE.md (model-specific)",
                    "README.md"
                ],
                "correct": 1,
                "success_msg": "✓ Repo-level instructions apply to everyone on the team!",
                "fail_msg": ".github/copilot-instructions.md is shared via git with the team.",
                "explanation": "Personal instructions are for you; repo-level is for the team."
            },
            {
                "prompt": "Your project has TypeScript backend and Python ML code with different standards. How do you handle this?",
                "options": [
                    "One big instruction file with all rules",
                    "Path-specific instructions in .github/instructions/",
                    "Different branches for different standards",
                    "Tell the AI each time"
                ],
                "correct": 1,
                "success_msg": "✓ Path-specific instructions handle multi-language projects perfectly!",
                "fail_msg": "Use .github/instructions/*.instructions.md for path-specific rules.",
                "explanation": "Different parts of the codebase can have different instructions."
            },
            {
                "prompt": "You need the AI to query a staging database. What do you configure?",
                "options": [
                    "LSP server for SQL",
                    "MCP server with database access",
                    "Custom agent with SQL skills",
                    "Shell alias for database queries"
                ],
                "correct": 1,
                "success_msg": "✓ MCP servers provide database access to the AI!",
                "fail_msg": "MCP servers are the standard way to connect external tools like databases.",
                "explanation": "Add a database MCP server in mcp-config.json."
            },
            {
                "prompt": "Before deploying to production, you want maximum safety. What's the right setup?",
                "options": [
                    "/allow-all for speed",
                    "/reset-allowed-tools + Plan mode",
                    "Autopilot mode",
                    "/streamer-mode"
                ],
                "correct": 1,
                "success_msg": "✓ Reset permissions + Plan mode = maximum safety!",
                "fail_msg": "Reset permissions and use Plan mode for production work.",
                "explanation": "Production work needs confirmations + plan review before execution."
            },
        ]
    }
    run_scenario(scenario, progress)
