"""
Test module for the SaveCommand class.
Ensures that the save operation behaves correctly under different conditions.
"""

import logging
from unittest.mock import MagicMock, patch
import pytest
from app.plugins.history.save import SaveCommand
from app.calculation_history import CalculationHistory

@pytest.fixture
def save_command():
    """Fixture for creating a SaveCommand instance with a mocked CalculationHistory."""
    command = SaveCommand()
    command.history_instance = MagicMock(spec=CalculationHistory)
    return command

def test_save_command_no_arguments_success(save_command, caplog):
    """
    Test the save command without passing any arguments, expecting a success message
    when the history saves successfully.
    """
    caplog.set_level(logging.INFO)
    save_command.execute()
    assert "Calculation history successfully saved." in caplog.text, \
        "Expected success message not logged"

def test_save_command_no_arguments_failure(save_command, caplog):
    """
    Test the save command without passing any arguments, expecting a failure message
    when the history cannot be saved due to an exception.
    """
    caplog.set_level(logging.ERROR)
    with patch.object(save_command.history_instance, 'save_history', side_effect=Exception('Test failure')):
        save_command.execute()
        assert "Failed to save calculation history: Test failure" in caplog.text, \
            "Expected failure message not logged"

def test_save_command_with_arguments(save_command, caplog):
    """
    Test the save command with arguments passed, expecting a warning message
    indicating that no arguments should be passed.
    """
    caplog.set_level(logging.WARNING)
    save_command.execute("unexpected_argument")
    assert "The save command does not accept any arguments." in caplog.text, \
        "Expected warning message not logged"
