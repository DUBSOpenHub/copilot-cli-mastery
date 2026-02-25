"""Tests for curriculum validation and data integrity."""

from data.validation import (
    validate_curriculum,
    EXPECTED_SLASH_COMMANDS,
    EXPECTED_SHORTCUTS,
    SCENARIOS,
    _SHORTCUT_NORMALISATIONS,
)


def test_curriculum_coverage():
    assert validate_curriculum() == []


def test_expected_counts():
    assert len(EXPECTED_SLASH_COMMANDS) == 41
    assert len(EXPECTED_SHORTCUTS) == 19
    assert len(SCENARIOS) == 5


def test_scenario_fields():
    for i, s in enumerate(SCENARIOS):
        for key in ("title", "difficulty", "prompt", "required", "model_answer"):
            assert key in s, f"Scenario {i} missing {key}"
        assert len(s["required"]) > 0
        assert s["difficulty"] in ("beginner", "intermediate", "advanced", "expert")


def test_normalisation_keys_exist():
    from modules.keyboard_shortcuts import SHORTCUTS
    all_keys = set()
    for shortcut_list in SHORTCUTS.values():
        for keys, _ in shortcut_list:
            all_keys.add(keys)
    for raw_key in _SHORTCUT_NORMALISATIONS:
        assert raw_key in all_keys, f'"{raw_key}" not in SHORTCUTS data'
