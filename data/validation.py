"""Curriculum validation and real-world scenarios (ported from Codex runner-up)."""

# ── Expected coverage sets (41 commands, 19 shortcuts) ─────────────────

EXPECTED_SLASH_COMMANDS = {
    "/init", "/agent", "/skills", "/mcp", "/plugin", "/model", "/fleet",
    "/tasks", "/ide", "/diff", "/review", "/lsp", "/terminal-setup",
    "/allow-all", "/add-dir", "/list-dirs", "/cwd", "/reset-allowed-tools",
    "/resume", "/rename", "/context", "/usage", "/session", "/compact",
    "/share", "/help", "/changelog", "/feedback", "/theme", "/update",
    "/experimental", "/clear", "/instructions", "/streamer-mode", "/exit",
    "/quit", "/login", "/logout", "/plan", "/user", "/delegate",
}

EXPECTED_SHORTCUTS = {
    "@", "Ctrl+S", "Shift+Tab", "Ctrl+T", "Ctrl+O", "Ctrl+E", "↑/↓",
    "!", "Esc", "Ctrl+C", "Ctrl+D", "Ctrl+L", "Ctrl+X, Ctrl+E",
    "Ctrl+A", "Ctrl+H", "Ctrl+W", "Ctrl+U", "Ctrl+K", "Meta+←/→",
}

# ── Real-world scenario challenges ─────────────────────────────────────

SCENARIOS = [
    {
        "title": "Hotfix Review Under Pressure",
        "difficulty": "intermediate",
        "prompt": "A production bug fix is ready; you must inspect diff, run review, and keep sensitive data hidden for a livestream.",
        "required": ["/diff", "/review", "/streamer-mode"],
        "model_answer": "/streamer-mode on -> /diff -> /review @src/payment.ts",
    },
    {
        "title": "Context Window Rescue",
        "difficulty": "advanced",
        "prompt": "Your session is huge and model quality is dropping; keep continuity while shrinking noise.",
        "required": ["/context", "/compact", "/resume"],
        "model_answer": "/context -> /compact -> /resume (or restart with --continue)",
    },
    {
        "title": "Autonomous Refactor Sprint",
        "difficulty": "expert",
        "prompt": "You want an agent to execute a refactor with minimal prompts, but only after reviewing plan and permissions.",
        "required": ["Shift+Tab", "/delegate", "/allow-all"],
        "model_answer": "Shift+Tab to Plan mode -> validate plan -> /delegate task -> optionally /allow-all",
    },
    {
        "title": "Enterprise Onboarding",
        "difficulty": "advanced",
        "prompt": "Set up custom agents, repo instructions, and MCP integration for a new team repository.",
        "required": [".github/agents", "/instructions", "/mcp"],
        "model_answer": "Add agent profiles to .github/agents, verify /instructions precedence, then /mcp add ...",
    },
    {
        "title": "Power Editing Session",
        "difficulty": "beginner",
        "prompt": "You are crafting a long prompt and need to edit quickly without losing context.",
        "required": ["Ctrl+X, Ctrl+E", "Ctrl+A", "Ctrl+K"],
        "model_answer": "Open in editor with Ctrl+X Ctrl+E, jump with Ctrl+A, trim tail with Ctrl+K",
    },
]

# ── Normalisation map for Opus shortcut key strings ────────────────────

_SHORTCUT_NORMALISATIONS = {
    "↑ / ↓": "↑/↓",
    "Meta+← / Meta+→": "Meta+←/→",
    "Ctrl+X → Ctrl+E": "Ctrl+X, Ctrl+E",
    "@ + filename": "@",
    "! + command": "!",
}


def validate_curriculum():
    """Check that all 41 expected slash commands and 19 shortcuts are present.

    Returns a list of error strings (empty list == pass).
    """
    from modules.slash_commands import COMMAND_CATEGORIES
    from modules.keyboard_shortcuts import SHORTCUTS

    # Extract slash commands from Opus's category dict
    commands_in_data = set()
    for cmds in COMMAND_CATEGORIES.values():
        for cmd_str, _ in cmds:
            for part in cmd_str.replace(" or ", ",").split(","):
                part = part.strip()
                if part.startswith("/"):
                    commands_in_data.add(part)

    # Extract shortcuts, normalising to the expected canonical form
    shortcuts_in_data = set()
    for shortcut_list in SHORTCUTS.values():
        for keys, _ in shortcut_list:
            shortcuts_in_data.add(_SHORTCUT_NORMALISATIONS.get(keys, keys))

    missing_commands = sorted(EXPECTED_SLASH_COMMANDS - commands_in_data)
    missing_shortcuts = sorted(EXPECTED_SHORTCUTS - shortcuts_in_data)

    errors = []
    if missing_commands:
        errors.append(f"Missing slash commands ({len(missing_commands)}): {', '.join(missing_commands)}")
    if missing_shortcuts:
        errors.append(f"Missing shortcuts ({len(missing_shortcuts)}): {', '.join(missing_shortcuts)}")
    return errors
