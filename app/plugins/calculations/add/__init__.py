# app/plugins/calculations/add/__init__.py
from app.command.base_command import BaseCommand
from app.calculation_history import CalculationHistory

class AddCommand(BaseCommand):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            operation = " + ".join(map(str, numbers)) + f" = {result}"
            # Utilizing the singleton instance of CalculationHistory
            history_instance = CalculationHistory()
            history_instance.add_record(operation, result)
            print(operation)  # Optionally, print the operation and result
            return result
        except ValueError:
            print("Error: All arguments must be numbers.")
