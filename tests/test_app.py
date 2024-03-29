"""Module to test the app's functionality.

This module contains tests to verify the behavior of the App class, 
especially its handling of environment variables and user commands.
"""

import pytest
from app import App

def test_app_get_environment_variable():
    """Test retrieval of the ENVIRONMENT variable."""
    app = App()
    # Retrieve the current environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit, "Application should exit gracefully on 'exit' command"

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    # Expect the application to exit upon processing an unknown command
    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Assert that the exit code is 0, indicating a successful exit
    assert excinfo.value.code == 0, "Application should exit with status code 0"

    # Optionally, check for the presence of the unknown command error message in the output
    captured = capfd.readouterr()
    assert "No such command: 'unknown_command'" in captured.out, "Application should notify about unknown command"
