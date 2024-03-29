"""Test cases for the AddCommand."""

import pytest
from app.plugins.calculations.add import AddCommand
from app.calculation_history import CalculationHistory

@pytest.fixture
def add_command_instance():
    """Fixture to create an AddCommand instance."""
    command = AddCommand()
    command.history_instance = CalculationHistory()  # Ensure a fresh CalculationHistory
    return command

def test_add_command_success(add_command_instance):
    """Test AddCommand with valid numeric arguments."""
    result = add_command_instance.execute("1", "2", "3")
    assert result == 6, "AddCommand should correctly add numeric arguments"

def test_add_command_invalid_input(add_command_instance):
    """Test AddCommand with invalid (non-numeric) arguments."""
    result = add_command_instance.execute("a", "2", "3")
    assert result == "Error: All arguments must be numbers.", "AddCommand should return error message for non-numeric arguments"
