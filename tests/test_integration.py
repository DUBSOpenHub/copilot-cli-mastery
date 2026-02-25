"""Integration and end-to-end tests."""

import os
import subprocess
import sys


def test_self_test_cli():
    """The --self-test flag should exit 0."""
    result = subprocess.run(
        [sys.executable, "mastery.py", "--self-test"],
        capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(__file__)),
    )
    assert result.returncode == 0
    assert "PASSED" in result.stdout


def test_non_interactive_cli():
    """The --non-interactive flag should exit 0."""
    result = subprocess.run(
        [sys.executable, "mastery.py", "--non-interactive"],
        capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(__file__)),
    )
    assert result.returncode == 0
    assert "PASSED" in result.stdout


def test_no_color_flag():
    """The --no-color flag should produce output without ANSI escapes."""
    result = subprocess.run(
        [sys.executable, "mastery.py", "--self-test", "--no-color"],
        capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(__file__)),
    )
    assert result.returncode == 0
    assert "\033[" not in result.stdout


def test_export_reference():
    """export_reference() should produce a valid cheatsheet."""
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from mastery import export_reference
    path = export_reference()
    assert os.path.exists(path)
    content = open(path).read()
    assert "SLASH COMMANDS" in content
    assert "KEYBOARD SHORTCUTS" in content
    assert len(content) > 500


def test_skill_md_frontmatter():
    """SKILL.md must have valid YAML frontmatter."""
    skill_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "SKILL.md")
    content = open(skill_path).read()
    assert content.startswith("---")
    parts = content.split("---", 2)
    assert len(parts) >= 3
    yaml_section = parts[1]
    assert "name:" in yaml_section
    assert "description:" in yaml_section
    assert "tools:" in yaml_section
