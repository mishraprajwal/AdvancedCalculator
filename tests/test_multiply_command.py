"""Test cases for the MultiplyCommand."""

import pytest
from app.plugins.calculations.multiply import MultiplyCommand
from app.calculation_history import CalculationHistory

@pytest.fixture
def multiply_command_instance():
    """Fixture to create a MultiplyCommand instance."""
    command = MultiplyCommand()
    command.history_instance = CalculationHistory()
    return command

def test_multiply_command_success(multiply_command_instance):
    """Test MultiplyCommand with valid numeric arguments."""
    result = multiply_command_instance.execute("2", "3")
    assert result == 6, "MultiplyCommand should correctly multiply numeric arguments"

def test_multiply_command_invalid_input(multiply_command_instance):
    """Test MultiplyCommand with invalid (non-numeric) arguments."""
    result = multiply_command_instance.execute("2", "b")
    assert result == "Error: All arguments must be numbers.", "MultiplyCommand should return error message for non-numeric arguments"
