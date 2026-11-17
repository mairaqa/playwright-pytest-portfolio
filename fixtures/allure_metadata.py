"""Collect session metadata without changing individual Allure results."""

from pathlib import Path

import pytest

from utils.allure_metadata import runtime_metadata, write_metadata

_STATE = pytest.StashKey[dict]()


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    """Enable metadata only for an active Allure reporting session."""
    if config.getoption("collectonly", False):
        return
    directory = config.getoption("allure_report_dir", None)
    if directory and config.pluginmanager.hasplugin("allure_listener"):
        config.stash[_STATE] = {
            "directory": Path(directory).resolve(),
            "browsers": set(),
        }


def pytest_collection_finish(session):
    """Use collected parameters, including Playwright's effective defaults."""
    state = session.config.stash.get(_STATE, None)
    if state is not None:
        state["browsers"].update(
            browser
            for item in session.items
            if (callspec := getattr(item, "callspec", None)) is not None
            if isinstance(browser := callspec.params.get("browser_name"), str)
        )


@pytest.hookimpl(optionalhook=True)
def pytest_testnodedown(node, error):
    """Receive selected browsers from xdist without worker file writes."""
    state = node.config.stash.get(_STATE, None)
    if state is not None:
        state["browsers"].update(node.workeroutput.get("allure_metadata_browsers", []))


def pytest_sessionfinish(session, exitstatus):
    """Write shared metadata once, after all workers have finished."""
    config = session.config
    state = config.stash.get(_STATE, None)
    if state is None:
        return
    if hasattr(config, "workerinput"):
        config.workeroutput["allure_metadata_browsers"] = sorted(state["browsers"])
        return
    metadata = runtime_metadata(config.getoption("env"), state["browsers"])
    write_metadata(state["directory"], metadata)
