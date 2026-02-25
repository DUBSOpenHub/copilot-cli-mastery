"""Shared fixtures for the test suite."""

import os
import tempfile
import pytest
import engine.progress as pm


@pytest.fixture(autouse=True)
def _isolate_progress(monkeypatch):
    """Every test gets its own temporary progress file."""
    tmp = tempfile.mktemp(suffix=".json")
    monkeypatch.setattr(pm, "SAVE_FILE", tmp)
    yield
    if os.path.exists(tmp):
        os.remove(tmp)


@pytest.fixture()
def progress():
    """Return a fresh Progress instance backed by the temp file."""
    return pm.Progress()
