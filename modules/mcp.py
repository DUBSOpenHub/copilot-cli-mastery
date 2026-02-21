"""Module 6: MCP Integration — Model Context Protocol."""

from engine.ui import (
    C, hr_fancy, print_tip, pause, info_box, menu, print_difficulty, type_text,
    print_command
)
from engine.quiz import Question, ScenarioQuestion, FillInQuestion, run_quiz, run_scenario


def run_lesson(progress):
    """Run the MCP training module."""
    progress.visit_section("mcp")

    while True:
        hr_fancy("🔌 Module 6: MCP Integration", C.BRIGHT_CYAN)
        print(f"\n  {C.WHITE}Model Context Protocol — extend the AI with external tools.{C.RESET}\n")

        result = menu([
            ("🎓 Guided Lesson: What is MCP?", "lesson_what"),
            ("🎓 Guided Lesson: Adding MCP Servers", "lesson_add"),
            ("🎓 Guided Lesson: Configuration Deep-Dive", "lesson_config"),
            ("🎯 Quiz: MCP Knowledge", "quiz"),
            ("🧩 Scenario: MCP Setup", "scenario"),
        ], "Choose activity")

        if result is None or result == "quit":
            return
        elif result == "lesson_what":
            _lesson_what(progress)
        elif result == "lesson_add":
            _lesson_add(progress)
        elif result == "lesson_config":
            _lesson_config(progress)
        elif result == "quiz":
            _run_quiz(progress)
        elif result == "scenario":
            _run_scenario(progress)


def _lesson_what(progress):
    hr_fancy("🎓 What is MCP?", C.BRIGHT_GREEN)
    print_difficulty("intermediate")

    type_text("\n  MCP is the bridge between AI and external tools.", color=C.WHITE)
    pause()

    info_box("Model Context Protocol (MCP)", f"""MCP is a standard protocol that connects AI models to external tools.

{C.GREEN}Think of it as:{C.RESET}
  • USB ports for AI — plug in any compatible tool
  • An API bridge between the AI and external services
  • A way to give the AI new capabilities without code changes

{C.YELLOW}How it works:{C.RESET}
  1. An MCP server exposes tools (functions the AI can call)
  2. The AI discovers available tools automatically
  3. When relevant, the AI uses these tools in its workflow

{C.CYAN}Example:{C.RESET}
  An MCP server for a database might expose:
  • query(sql) — run SQL queries
  • schema() — show database schema
  • tables() — list all tables""")
    pause()

    info_box("The GitHub MCP Server (Built-in)", f"""The Copilot CLI ships with a built-in GitHub MCP server.

{C.GREEN}Capabilities:{C.RESET}
  • Search repositories, code, issues, PRs
  • Read file contents from GitHub repos
  • Get commit history and diffs
  • List branches, workflows, actions
  • Get issue and PR details
  • Search users

{C.YELLOW}Always available:{C.RESET} No setup needed — it's built in.

{C.CYAN}Example usage:{C.RESET}
  "Search for all open issues labeled 'bug' in facebook/react"
  → AI uses the GitHub MCP server to query the GitHub API.""")
    pause()

    progress.complete_lesson("mcp_what")
    progress.check_module_achievements()


def _lesson_add(progress):
    hr_fancy("🎓 Adding MCP Servers", C.BRIGHT_GREEN)
    print_difficulty("advanced")

    type_text("\n  Plug in new capabilities with custom MCP servers.", color=C.WHITE)
    pause()

    info_box("The /mcp Command", f"""{C.GREEN}/mcp{C.RESET}                        — list connected MCP servers
{C.GREEN}/mcp add <name> <command>{C.RESET}   — add a new MCP server

{C.YELLOW}Examples:{C.RESET}
  /mcp add postgres npx @modelcontextprotocol/server-postgres
  /mcp add filesystem npx @modelcontextprotocol/server-filesystem
  /mcp add sqlite npx @modelcontextprotocol/server-sqlite

{C.CYAN}The command:{C.RESET}
  This is the shell command that STARTS the MCP server.
  The CLI will run this command and connect to the server.""")
    pause()

    info_box("Popular MCP Servers", f"""{C.GREEN}Database servers:{C.RESET}
  • server-postgres — Query PostgreSQL databases
  • server-sqlite — Query SQLite databases

{C.GREEN}File & data servers:{C.RESET}
  • server-filesystem — Access local files with permissions
  • server-memory — Persistent knowledge graph

{C.GREEN}API servers:{C.RESET}
  • server-github — GitHub API (built-in!)
  • server-slack — Slack integration
  • server-google-maps — Maps and location data

{C.GREEN}Development servers:{C.RESET}
  • server-puppeteer — Browser automation
  • server-brave-search — Web search

{C.YELLOW}Find more:{C.RESET} Search npm for @modelcontextprotocol packages""")
    pause()

    progress.complete_lesson("mcp_add")
    progress.check_module_achievements()


def _lesson_config(progress):
    hr_fancy("🎓 MCP Configuration", C.BRIGHT_GREEN)
    print_difficulty("expert")

    type_text("\n  Deep-dive into MCP configuration files.", color=C.WHITE)
    pause()

    info_box("mcp-config.json", f"""MCP servers can be configured in a JSON config file.

{C.GREEN}Location:{C.RESET} ~/.copilot/mcp-config.json (user-level)
          .github/mcp-config.json (project-level)

{C.YELLOW}Format:{C.RESET}
```json
{{
  "mcpServers": {{
    "postgres": {{
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-postgres",
        "postgresql://localhost/mydb"
      ],
      "env": {{
        "DB_PASSWORD": "{{{{env.DB_PASSWORD}}}}"
      }}
    }},
    "custom-api": {{
      "command": "node",
      "args": ["./tools/mcp-server.js"],
      "cwd": "/path/to/project"
    }}
  }}
}}
```

{C.CYAN}Fields:{C.RESET}
  • command: the executable to run
  • args: command-line arguments
  • env: environment variables (supports variable substitution)
  • cwd: working directory for the server""")
    pause()

    info_box("MCP Best Practices", f"""{C.GREEN}1. Security:{C.RESET}
   • Never put credentials directly in config files
   • Use environment variable references: {{{{env.SECRET}}}}
   • Review MCP server source before using

{C.GREEN}2. Performance:{C.RESET}
   • Only connect servers you need
   • Each server adds overhead to AI tool discovery
   • Use project-level config for project-specific servers

{C.GREEN}3. Debugging:{C.RESET}
   • /mcp lists connected servers and their status
   • Check server logs for connection issues
   • Verify the server command works independently""")
    pause()

    progress.complete_lesson("mcp_config")
    progress.complete_lesson("mcp")
    progress.check_module_achievements()


def _run_quiz(progress):
    questions = [
        Question(
            "What does MCP stand for?",
            ["Machine Code Protocol", "Model Context Protocol",
             "Multi-Client Platform", "Managed Connection Port"],
            1,
            "Model Context Protocol — the standard for connecting AI to external tools.",
            "beginner"
        ),
        Question(
            "Which MCP server is built into the Copilot CLI?",
            ["PostgreSQL server", "Filesystem server",
             "GitHub MCP server", "No servers are built-in"],
            2,
            "The GitHub MCP server ships with the CLI — search repos, issues, PRs, etc.",
            "beginner"
        ),
        Question(
            "What's the correct command to add an MCP server?",
            ["/mcp install <name>", "/mcp add <name> <command>",
             "/add-mcp <url>", "/plugin mcp <name>"],
            1,
            "/mcp add takes a name and the shell command to start the server.",
            "intermediate"
        ),
        Question(
            "Where is the MCP configuration file located?",
            ["~/.copilot/mcp-config.json", "~/.mcp/config.json",
             "/etc/mcp/servers.json", "~/.config/mcp.json"],
            0,
            "User-level: ~/.copilot/mcp-config.json, Project: .github/mcp-config.json",
            "intermediate"
        ),
        Question(
            "How should you handle secrets in MCP config?",
            ["Put them directly in the JSON", "Use environment variable references",
             "Encrypt the config file", "Create a separate secrets file"],
            1,
            "Use env variable refs like {{env.SECRET}} — never hardcode credentials.",
            "advanced"
        ),
        ScenarioQuestion(
            "Your team needs to query a PostgreSQL database from the Copilot CLI. "
            "The database has sensitive credentials.",
            "What's the safest way to set this up?",
            [
                "Add the connection string directly: /mcp add pg npx server-postgres postgres://user:pass@host/db",
                "Configure in mcp-config.json with env variable references for credentials",
                "Paste the password into the prompt when asked",
                "Skip MCP and query the database manually"
            ],
            1,
            "Config files with env variable references keep credentials out of version control.",
            "advanced"
        ),
    ]
    run_quiz(questions, progress, "mcp", "MCP Integration Quiz")


def _run_scenario(progress):
    scenario = {
        "id": "mcp_setup",
        "title": "MCP Server Setup",
        "description": "Set up MCP servers for a full-stack project\n"
                       "with a database, file system needs, and custom tools.",
        "difficulty": "advanced",
        "steps": [
            {
                "prompt": "You need the AI to query your project's PostgreSQL database. What do you do?",
                "options": [
                    "Export the database to a file and upload it",
                    "/mcp add postgres npx @modelcontextprotocol/server-postgres <conn-string>",
                    "Copy-paste SQL results into the prompt",
                    "Use the built-in database tools"
                ],
                "correct": 1,
                "success_msg": "✓ Adding an MCP server gives the AI direct database access!",
                "fail_msg": "Use /mcp add to connect an MCP database server.",
                "explanation": "MCP servers let the AI query the database directly."
            },
            {
                "prompt": "Where should you store the database password for the MCP server?",
                "options": [
                    "In mcp-config.json directly",
                    "In an environment variable, referenced in config",
                    "In the /mcp add command",
                    "In a .env file committed to git"
                ],
                "correct": 1,
                "success_msg": "✓ Environment variables keep secrets out of config files!",
                "fail_msg": "Use env variables — never hardcode secrets.",
                "explanation": "Config files may be committed to git. Env vars stay local."
            },
            {
                "prompt": "You want to verify your MCP servers are connected. What command?",
                "options": ["/mcp status", "/mcp", "/mcp list", "/mcp check"],
                "correct": 1,
                "success_msg": "✓ /mcp (no arguments) lists all connected servers!",
                "fail_msg": "Just /mcp shows all servers and their connection status.",
                "explanation": "/mcp with no arguments lists everything."
            },
        ]
    }
    run_scenario(scenario, progress)
