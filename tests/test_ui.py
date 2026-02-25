"""Tests for the terminal UI engine."""

import io
import os
import sys

import pytest


def test_strip_ansi():
    from engine.ui import _strip_ansi
    assert _strip_ansi("\033[31mhello\033[0m") == "hello"
    assert _strip_ansi("plain") == "plain"
    assert _strip_ansi("") == ""


def test_get_width():
    from engine.ui import get_width
    w = get_width()
    assert 1 <= w <= 100


def test_progress_bar_output(capsys):
    from engine.ui import progress_bar
    progress_bar(50, 100, width=20, label="Test")
    out = capsys.readouterr().out
    assert "50%" in out
    assert "50/100" in out


def test_progress_bar_zero(capsys):
    from engine.ui import progress_bar
    progress_bar(0, 0, width=10)
    out = capsys.readouterr().out
    assert "0%" in out


def test_print_difficulty_all_levels(capsys):
    from engine.ui import print_difficulty
    for level in ("beginner", "intermediate", "advanced", "expert", "unknown"):
        print_difficulty(level)
    out = capsys.readouterr().out
    assert "BEGINNER" in out
    assert "EXPERT" in out


def test_no_color_env(monkeypatch):
    """NO_COLOR env var disables all ANSI codes."""
    monkeypatch.setenv("NO_COLOR", "1")
    from engine.ui import C
    assert C.RED == ""
    assert C.BOLD == ""
    assert C.RESET == ""


def test_no_color_flag(monkeypatch):
    """--no-color CLI flag disables all ANSI codes."""
    monkeypatch.setattr(sys, "argv", ["mastery.py", "--no-color"])
    monkeypatch.delenv("NO_COLOR", raising=False)
    from engine.ui import C
    assert C.GREEN == ""
