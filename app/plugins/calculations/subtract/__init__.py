# app/plugins/calculations/subtract/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility  # Ensure correct import path

class SubtractCommand(BaseCommand):
    def execute(self, *args):
        try:
            if len(args) < 2:
                raise ValueError("Subtraction requires at least two numbers.")
            numbers = [float(arg) for arg in args]
            result = numbers[0] - sum(numbers[1:])
            operation = " - ".join(map(str, numbers)) + f" = {result}"
            self.history_instance.add_record(operation, result)
            AdvancedLoggingUtility.info(f"Subtraction operation successful: {operation}")
            return result  # Returning result; consider if you want to log this differently or in addition
        except ValueError as e:
            error_msg = f"Error in subtraction operation: {e}"
            AdvancedLoggingUtility.error(error_msg)
            return error_msg  # Handling the error by returning it; adjust based on your application's needs
