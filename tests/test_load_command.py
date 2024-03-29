"""
Test module for the LoadCommand class.
Ensures that the load operation behaves correctly under different conditions.
"""

import logging
from unittest.mock import MagicMock
import pytest
from app.plugins.history.load import LoadCommand
from app.calculation_history import CalculationHistory

@pytest.fixture
def load_command():
    """Fixture for creating a LoadCommand instance with a mocked CalculationHistory."""
    command = LoadCommand()
    command.history_instance = MagicMock(spec=CalculationHistory)
    return command

def test_load_command_no_arguments_success(load_command, caplog):
    """
    Test the load command without passing any arguments, expecting a success message
    when the history loads successfully.
    """
    caplog.set_level(logging.INFO)
    load_command.history_instance.load_history.return_value = True
    load_command.execute()
    assert "Calculation history successfully loaded." in caplog.text, \
        "Expected success message not logged"

def test_load_command_no_arguments_failure(load_command, caplog):
    """
    Test the load command without passing any arguments, expecting a failure message
    when the history cannot be loaded.
    """
    caplog.set_level(logging.ERROR)
    load_command.history_instance.load_history.return_value = False
    load_command.execute()
    assert "Failed to load calculation history." in caplog.text, \
        "Expected failure message not logged"

def test_load_command_with_arguments(load_command, caplog):
    """
    Test the load command with arguments passed, expecting a warning message
    indicating that no arguments should be passed.
    """
    caplog.set_level(logging.WARNING)
    load_command.execute("unexpected_argument")
    assert "The load command does not accept any arguments." in caplog.text, \
        "Expected warning message not logged"
