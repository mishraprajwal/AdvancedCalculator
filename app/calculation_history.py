import os
import pandas as pd
from dotenv import load_dotenv

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

    def load_or_initialize_history(self):
        if os.path.exists(self.history_file):
            return pd.read_csv(self.history_file)
        else:
            # Adjusted column names to better reflect the data structure
            return pd.DataFrame(columns=['Operation', 'Result'])

    def add_record(self, operation, result):
        # Simplifying the addition of a new record
        new_record = {'Operation': operation, 'Result': result}
        self.history_df = self.history_df.append(new_record, ignore_index=True)
        self.save_history()

    def save_history(self):
        # Ensuring the directory exists before saving
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        self.history_df.to_csv(self.history_file, index=False)

    def load_history(self):
        # Added check to reload the history dataframe from the CSV
        if os.path.exists(self.history_file):
            self.history_df = pd.read_csv(self.history_file)
            print("Calculation history loaded.")
            return True
        else:
            print("There is no calculation history file.")
            return False

    def clear_history(self):
        # Resetting the dataframe to clear history
        self.history_df = pd.DataFrame(columns=['Operation', 'Result'])
        self.save_history()
        print("Calculation history cleared.")

    def delete_history(self, index):
        # Improved deletion logic and user feedback
        try:
            self.history_df = self.history_df.drop(index).reset_index(drop=True)
            self.save_history()
            print(f"Record at index {index} deleted.")
            return True
        except KeyError:
            print(f"No record found at index {index}.")
            return False
