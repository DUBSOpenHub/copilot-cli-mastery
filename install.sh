#!/usr/bin/env bash
# Copilot CLI Mastery — Install Script
# Installs the skill into ~/.copilot/skills/cli-mastery/
set -euo pipefail

SKILL_DIR="$HOME/.copilot/skills/cli-mastery"
REPO_URL="https://github.com/DUBSOpenHub/copilot-cli-mastery"
SKILL_RAW="https://raw.githubusercontent.com/DUBSOpenHub/copilot-cli-mastery/main/SKILL.md"

echo "🎓 Copilot CLI Mastery — Installer"
echo "==================================="
echo ""

# Create skill directory
mkdir -p "$SKILL_DIR"

# Detect install method
if command -v curl &>/dev/null; then
    echo "📥 Downloading SKILL.md..."
    curl -sSL "$SKILL_RAW" -o "$SKILL_DIR/SKILL.md"
elif command -v wget &>/dev/null; then
    echo "📥 Downloading SKILL.md..."
    wget -qO "$SKILL_DIR/SKILL.md" "$SKILL_RAW"
else
    echo "❌ Error: curl or wget is required."
    exit 1
fi

echo "✅ Skill installed to: $SKILL_DIR/SKILL.md"
echo ""
echo "🚀 Usage:"
echo "   Open the Copilot CLI and say: \"cliexpert\""
echo "   Or: \"teach me the Copilot CLI\""
echo "   Or: \"quiz me on slash commands\""
echo ""
echo "🐍 Want the standalone Python trainer too?"
echo "   git clone $REPO_URL"
echo "   cd copilot-cli-mastery && python3 mastery.py"
echo ""
echo "Done! 🎉"
