# Assuming this class is in app/calculation_history.py
import os
import pandas as pd
from dotenv import load_dotenv
from app.advanced_logging_utility import AdvancedLoggingUtility  # Adjusted import path

class CalculationHistory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        load_dotenv()
        self.history_file = os.getenv('HISTORY_FILE_PATH', 'calculation_history.csv')
        self.history_file = os.path.abspath(self.history_file)
        self.history_df = self.load_or_initialize_history()
        AdvancedLoggingUtility.info("CalculationHistory initialized", 
                                    history_file=self.history_file)

    def load_or_initialize_history(self):
        if os.path.exists(self.history_file):
            history_df = pd.read_csv(self.history_file)
            AdvancedLoggingUtility.info("Calculation history loaded from file.", 
                                        file_path=self.history_file)
            return history_df
        else:
            AdvancedLoggingUtility.info("No existing calculation history found, initializing new history.")
            return pd.DataFrame(columns=['Operation', 'Result'])

    def add_record(self, operation, result):
        new_record = {'Operation': operation, 'Result': result}
        self.history_df = self.history_df.append(new_record, ignore_index=True)
        self.save_history()
        AdvancedLoggingUtility.info("Record added", operation=operation, result=result)

    def save_history(self):
        try:
            os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
            self.history_df.to_csv(self.history_file, index=False)
            AdvancedLoggingUtility.info("Calculation history saved.", 
                                        file_path=self.history_file)
        except Exception as e:
            AdvancedLoggingUtility.error("Failed to save calculation history.", 
                                         error=str(e), file_path=self.history_file)

    def load_history(self):
        if os.path.exists(self.history_file):
            self.history_df = pd.read_csv(self.history_file)
            AdvancedLoggingUtility.info("Calculation history reloaded.", 
                                        file_path=self.history_file)
            return True
        else:
            AdvancedLoggingUtility.warning("Attempted to reload history, but no calculation history file exists.")
            return False

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Operation', 'Result'])
        self.save_history()
        AdvancedLoggingUtility.info("Calculation history cleared.")

    def delete_history(self, index):
        try:
            self.history_df = self.history_df.drop(index).reset_index(drop=True)
            self.save_history()
            AdvancedLoggingUtility.info("Record deleted.", index=index)
            return True
        except KeyError:
            AdvancedLoggingUtility.warning("Attempted to delete record, but index does not exist.", 
                                           index=index)
            return False
