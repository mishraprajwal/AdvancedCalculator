"""Tests for the ClearCommand class."""

from unittest.mock import MagicMock
import pytest
from app.plugins.history.clear import ClearCommand
from app.calculation_history import CalculationHistory

@pytest.fixture
def clear_command(caplog):
    """Fixture to provide a ClearCommand instance with a mock history_instance."""
    command = ClearCommand()
    command.history_instance = MagicMock(spec=CalculationHistory)
    return command

def test_clear_command_no_arguments(clear_command, caplog):
    """Test clearing the history without passing any arguments."""
    clear_command.execute()
    # Since we are using a MagicMock for history_instance, you may need to manually
    # add a log entry to caplog or adjust your expectations based on the actual implementation.
    # This example assumes that the logging occurs outside the command, hence no log in caplog.
    clear_command.history_instance.clear_history.assert_called_once_with()

def test_clear_command_with_arguments(clear_command, caplog):
    """Test attempting to clear the history with arguments, which should not be accepted."""
    clear_command.execute("unexpected_arg")
    # Similar to the above, adjust the expectation or logging mechanism as per your implementation.
    clear_command.history_instance.clear_history.assert_not_called()
