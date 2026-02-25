"""Tests for the 8 training modules."""

import importlib

import pytest

MODULE_NAMES = [
    "modules.slash_commands",
    "modules.keyboard_shortcuts",
    "modules.modes",
    "modules.agents",
    "modules.skills",
    "modules.mcp",
    "modules.advanced",
    "modules.configuration",
]


@pytest.mark.parametrize("mod_name", MODULE_NAMES)
def test_module_has_run_lesson(mod_name):
    mod = importlib.import_module(mod_name)
    assert hasattr(mod, "run_lesson")
    assert callable(mod.run_lesson)


@pytest.mark.parametrize("mod_name", MODULE_NAMES)
def test_module_has_quiz_content(mod_name):
    mod = importlib.import_module(mod_name)
    source = open(mod.__file__).read()
    assert "Question(" in source or "run_quiz" in source


def test_slash_command_categories():
    from modules.slash_commands import COMMAND_CATEGORIES
    assert len(COMMAND_CATEGORIES) >= 8
    total = sum(len(v) for v in COMMAND_CATEGORIES.values())
    assert total >= 35


def test_shortcut_categories():
    from modules.keyboard_shortcuts import SHORTCUTS
    assert len(SHORTCUTS) >= 4
    total = sum(len(v) for v in SHORTCUTS.values())
    assert total >= 19
