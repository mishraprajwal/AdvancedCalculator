"""
This module contains tests for the DeleteCommand class,
focusing on ensuring that deletion operations are handled correctly,
including both successful and unsuccessful deletion attempts.
"""

import logging
from unittest.mock import MagicMock
import pytest
from app.plugins.history.delete import DeleteCommand
from app.calculation_history import CalculationHistory

@pytest.fixture
def delete_command():
    """Fixture for creating a DeleteCommand instance with a mocked CalculationHistory."""
    command = DeleteCommand()
    command.history_instance = MagicMock(spec=CalculationHistory)
    return command

def test_delete_command_valid_index(delete_command, caplog):
    """
    Test deleting a history record with a valid index.
    Ensures the command logs a success message.
    """
    caplog.set_level(logging.INFO)
    delete_command.history_instance.delete_history.return_value = True
    delete_command.execute("1")
    assert "Successfully deleted record at index 1." in caplog.text, "Expected success message not logged"

def test_delete_command_invalid_index(delete_command, caplog):
    """
    Test deleting a history record with an invalid index, expecting a failure message.
    """
    caplog.set_level(logging.WARNING)
    delete_command.history_instance.delete_history.return_value = False
    delete_command.execute("999")
    assert "Failed to delete record at index 999. No record found." in caplog.text, "Expected failure message not logged"

def test_delete_command_with_non_integer_argument(delete_command, caplog):
    """
    Test attempting to delete with a non-integer index, expecting an error message.
    """
    caplog.set_level(logging.ERROR)
    delete_command.execute("non-integer")
    assert "Error: Index must be an integer." in caplog.text, "Expected error message not logged"
