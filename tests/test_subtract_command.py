import pytest
from app.plugins.calculations.subtract import SubtractCommand
from app.calculation_history import CalculationHistory

@pytest.fixture
def subtract_command():
    command = SubtractCommand()
    # Clear any existing history to ensure a clean state for each test
    command.history_instance.clear_history()
    return command

def test_subtract_command_valid(subtract_command, capfd):
    result = subtract_command.execute('5', '3', '1')
    assert result == 1, "SubtractCommand should correctly subtract numbers and return the result"
    # Verify the operation is recorded in the history
    history = subtract_command.history_instance.history_df
    assert not history.empty, "The operation should be recorded in the history"
    assert history.iloc[-1]['Operation'] == '5 - 3 - 1', "The operation should match the input"
    assert history.iloc[-1]['Result'] == 1, "The result should match the operation's outcome"
    # Check stdout
    captured = capfd.readouterr()
    assert "5 - 3 - 1 = 1" in captured.out, "The operation and result should be printed to stdout"

def test_subtract_command_invalid(subtract_command, capfd):
    result = subtract_command.execute('x', '-')
    assert result == "Error: All arguments must be numbers.", "SubtractCommand should return an error message for invalid inputs"
    # Check stdout for the error message
    captured = capfd.readouterr()
    assert "Error: All arguments must be numbers." in captured.out, "The error message should be printed to stdout"
    # Ensure no operation is recorded for invalid input
    history = subtract_command.history_instance.history_df
    assert history.empty, "No operation should be recorded in the history for invalid inputs"
