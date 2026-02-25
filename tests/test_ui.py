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


def test_reduced_motion_no_color(monkeypatch):
    """NO_COLOR triggers reduced motion."""
    monkeypatch.setenv("NO_COLOR", "1")
    from engine.ui import _reduced_motion
    assert _reduced_motion() is True


def test_reduced_motion_env(monkeypatch):
    """REDUCE_MOTION env var triggers reduced motion."""
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.setenv("REDUCE_MOTION", "1")
    from engine.ui import _reduced_motion
    assert _reduced_motion() is True


def test_reduced_motion_dumb_term(monkeypatch):
    """TERM=dumb triggers reduced motion."""
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.delenv("REDUCE_MOTION", raising=False)
    monkeypatch.setenv("TERM", "dumb")
    from engine.ui import _reduced_motion
    assert _reduced_motion() is True


def test_type_text_skips_delay(monkeypatch, capsys):
    """type_text prints instantly under reduced motion."""
    monkeypatch.setenv("NO_COLOR", "1")
    from engine.ui import type_text
    import time
    start = time.monotonic()
    type_text("Hello, world!" * 10)
    elapsed = time.monotonic() - start
    assert elapsed < 0.1
    assert "Hello" in capsys.readouterr().out


def test_clear_noop_when_reduced(monkeypatch):
    """clear() should be a no-op under reduced motion."""
    monkeypatch.setenv("NO_COLOR", "1")
    from engine.ui import clear
    # Should not raise or call os.system
    clear()
