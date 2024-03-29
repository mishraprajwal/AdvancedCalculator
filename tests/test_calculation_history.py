# pylint: disable=protected-access
"""Module for testing the CalculationHistory class functionality."""

import os
import tempfile
import pytest
from app.calculation_history import CalculationHistory

@pytest.fixture
def temp_calc_history():
    """Fixture to create a temporary CalculationHistory instance with a fresh environment."""
    CalculationHistory._reset_instance_for_testing()  # Reset singleton before each test
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        os.environ['HISTORY_FILE_PATH'] = tmp_file.name
        ch = CalculationHistory()
        yield ch
        os.unlink(tmp_file.name)

def test_initialization(temp_calc_history):
    """Test that the CalculationHistory instance initializes correctly."""
    assert temp_calc_history.history_df.empty, "DataFrame should be empty upon initialization"
    assert 'Operation' in temp_calc_history.history_df.columns, "Operation column missing"
    assert 'Result' in temp_calc_history.history_df.columns, "Result column missing"

def test_add_record(temp_calc_history):
    """Test adding a record to the calculation history."""
    temp_calc_history.add_record('2 + 2', 4)
    assert not temp_calc_history.history_df.empty, "DataFrame should not be empty after adding a record"
    assert temp_calc_history.history_df.iloc[-1]['Operation'] == '2 + 2', "Operation mismatch"
    assert temp_calc_history.history_df.iloc[-1]['Result'] == 4, "Result mismatch"

def test_save_and_load_history(temp_calc_history):
    """Test saving and then loading the calculation history."""
    temp_calc_history.add_record('3 * 3', 9)
    temp_calc_history.save_history()
    new_instance = CalculationHistory()
    assert new_instance.load_history(), "Should successfully load history"
    assert not new_instance.history_df.empty, "DataFrame should not be empty after loading history"
    assert new_instance.history_df.iloc[-1]['Operation'] == '3 * 3', "Operation mismatch after loading"
    assert new_instance.history_df.iloc[-1]['Result'] == 9, "Result mismatch after loading"

def test_clear_history(temp_calc_history):
    """Test clearing the calculation history."""
    temp_calc_history.add_record('1 - 1', 0)
    temp_calc_history.clear_history()
    assert temp_calc_history.history_df.empty, "DataFrame should be empty after clearing history"

def test_delete_history(temp_calc_history):
    """Test deleting a specific record from the calculation history."""
    temp_calc_history.add_record('10 / 2', 5)
    temp_calc_history.add_record('10 / 5', 2)
    temp_calc_history.delete_history(0)
    assert len(temp_calc_history.history_df) == 1, "DataFrame should contain one record after deletion"
    assert temp_calc_history.history_df.iloc[0]['Operation'] == '10 / 5', "Operation mismatch after deletion"
    assert temp_calc_history.history_df.iloc[0]['Result'] == 2, "Result mismatch after deletion"
