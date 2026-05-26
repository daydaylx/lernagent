import asyncio
from pathlib import Path

import pytest

from app.ui import PathInputScreen, RepoTutorApp
from textual.widgets import Input, RadioSet, Static


def _run(coro):
    return asyncio.run(coro)


def test_app_shows_path_dialog_when_no_path():
    async def inner():
        app = RepoTutorApp()
        async with app.run_test() as pilot:
            assert isinstance(app.screen, PathInputScreen)

    _run(inner())


def test_app_skips_dialog_when_path_given(tmp_path: Path):
    async def inner():
        app = RepoTutorApp(project_path=tmp_path)
        async with app.run_test() as pilot:
            assert not isinstance(app.screen, PathInputScreen)

    _run(inner())


def test_path_dialog_rejects_nonexistent_path():
    async def inner():
        app = RepoTutorApp()
        async with app.run_test() as pilot:
            inp = app.screen.query_one("#path-input", Input)
            inp.value = "/dev/null/nonexistent_12345"
            await inp.action_submit()
            await pilot.pause()
            # Dialog must still be visible
            assert isinstance(app.screen, PathInputScreen)

    _run(inner())


def test_path_dialog_accepts_valid_path(tmp_path: Path):
    async def inner():
        app = RepoTutorApp()
        async with app.run_test() as pilot:
            inp = app.screen.query_one("#path-input", Input)
            inp.value = str(tmp_path)
            await inp.action_submit()
            # Allow message chain: Submitted → _PathChosen → pop_screen
            await pilot.pause()
            await asyncio.sleep(0.05)
            assert app._project_path == tmp_path

    _run(inner())


def test_default_mode_is_normal(tmp_path: Path):
    async def inner():
        app = RepoTutorApp(project_path=tmp_path)
        async with app.run_test() as pilot:
            assert app._current_mode == "normal"

    _run(inner())


def test_output_panel_shows_initial_hint(tmp_path: Path):
    async def inner():
        app = RepoTutorApp(project_path=tmp_path)
        async with app.run_test() as pilot:
            output = app.query_one("#output-static", Static)
            assert "Datei" in str(output.content)

    _run(inner())


def test_followup_without_file_shows_error(tmp_path: Path):
    async def inner():
        app = RepoTutorApp(project_path=tmp_path)
        async with app.run_test() as pilot:
            inp = app.query_one("#followup-input", Input)
            inp.value = "Was macht diese Datei?"
            await inp.action_submit()
            await pilot.pause()
            status = app.query_one("#status-bar", Static)
            assert "Datei" in str(status.content)

    _run(inner())


def test_mode_changes_on_radio_select(tmp_path: Path):
    async def inner():
        app = RepoTutorApp(project_path=tmp_path)
        async with app.run_test() as pilot:
            radio_set = app.query_one("#mode-select", RadioSet)
            radio_set.action_next_button()
            await pilot.pause()
            assert app._current_mode in ("simple", "normal", "context", "quiz")

    _run(inner())
