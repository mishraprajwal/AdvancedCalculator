"""Test cases for the SubtractCommand."""

import pytest
from app.plugins.calculations.subtract import SubtractCommand
from app.calculation_history import CalculationHistory

@pytest.fixture
def subtract_command_instance():
    """Fixture to create a SubtractCommand instance."""
    command = SubtractCommand()
    command.history_instance = CalculationHistory()
    return command

def test_subtract_command_success(subtract_command_instance):
    """Test SubtractCommand with valid numeric arguments."""
    result = subtract_command_instance.execute("5", "3")
    assert result == 2, "SubtractCommand should correctly subtract numeric arguments"

def test_subtract_command_invalid_input(subtract_command_instance):
    """Test SubtractCommand with invalid (non-numeric) arguments."""
    result = subtract_command_instance.execute("5", "a")
    assert result == "Error: All arguments must be numbers.", "SubtractCommand should return error message for non-numeric arguments"
