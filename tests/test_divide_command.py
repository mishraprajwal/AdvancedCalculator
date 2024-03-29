"""Tests for the DivideCommand in the calculator application.

This module contains pytest test cases for testing the functionality of the
DivideCommand class, ensuring it correctly handles division operations, including
error handling for invalid inputs and division by zero scenarios.
"""

import pytest
from app.plugins.calculations.divide import DivideCommand
from app.calculation_history import CalculationHistory

@pytest.fixture
def divide_command_instance():
    """Fixture for creating a fresh instance of the DivideCommand class."""
    command = DivideCommand()
    command.history_instance = CalculationHistory()  # Ensure a fresh CalculationHistory
    return command

def test_divide_command_invalid_input(divide_command_instance):
    """Test the DivideCommand with invalid (non-numeric) arguments to ensure proper error handling."""
    result = divide_command_instance.execute("a", "2")
    expected_error_msg = "Error executing divide command: could not convert string to float: 'a'"
    assert result == expected_error_msg, "DivideCommand should return an error message for non-numeric arguments"

def test_divide_command_division_by_zero(divide_command_instance):
    """Test the DivideCommand with a division by zero scenario to ensure it handles the error correctly."""
    result = divide_command_instance.execute("10", "0")
    expected_error_msg = "Error executing divide command: Division by zero is not allowed."
    assert result == expected_error_msg, "DivideCommand should return an error message for division by zero"
