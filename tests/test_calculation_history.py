import os
import tempfile
import pandas as pd
import pytest
from app.calculation_history import CalculationHistory

# Use a fixture to isolate tests by using a temporary file
@pytest.fixture
def temp_calc_history():
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        os.environ['HISTORY_FILE_PATH'] = tmp_file.name
        ch = CalculationHistory()
        yield ch
        os.unlink(tmp_file.name)

def test_initialization(temp_calc_history):
    assert temp_calc_history.history_df.empty
    assert 'Operation' in temp_calc_history.history_df.columns
    assert 'Result' in temp_calc_history.history_df.columns

def test_add_record(temp_calc_history):
    temp_calc_history.add_record('2 + 2', 4)
    assert not temp_calc_history.history_df.empty
    assert temp_calc_history.history_df.iloc[-1]['Operation'] == '2 + 2'
    assert temp_calc_history.history_df.iloc[-1]['Result'] == 4

def test_save_and_load_history(temp_calc_history):
    temp_calc_history.add_record('3 * 3', 9)
    temp_calc_history.save_history()
    new_instance = CalculationHistory()
    assert new_instance.load_history()
    assert not new_instance.history_df.empty
    assert new_instance.history_df.iloc[-1]['Operation'] == '3 * 3'
    assert new_instance.history_df.iloc[-1]['Result'] == 9

def test_clear_history(temp_calc_history):
    temp_calc_history.add_record('1 - 1', 0)
    temp_calc_history.clear_history()
    assert temp_calc_history.history_df.empty

def test_delete_history(temp_calc_history):
    temp_calc_history.add_record('10 / 2', 5)
    temp_calc_history.add_record('10 / 5', 2)
    temp_calc_history.delete_history(0)
    assert len(temp_calc_history.history_df) == 1
    assert temp_calc_history.history_df.iloc[0]['Operation'] == '10 / 5'
    assert temp_calc_history.history_df.iloc[0]['Result'] == 2

