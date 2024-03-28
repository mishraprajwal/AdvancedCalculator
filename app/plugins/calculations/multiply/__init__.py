# app/plugins/calculations/multiply/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility  # Ensure correct import path

class MultiplyCommand(BaseCommand):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = 1
            for num in numbers:
                result *= num
            operation = " * ".join(map(str, numbers)) + f" = {result}"
            self.history_instance.add_record(operation, result)
            AdvancedLoggingUtility.info(f"Multiplication operation successful: {operation}")
            return result  # Consider how you want to handle the result in your application context
        except ValueError:
            error_msg = "Error: All arguments must be numbers."
            AdvancedLoggingUtility.error(error_msg)
            return error_msg  # Adjust based on your application's error handling strategy
