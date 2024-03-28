# app/plugins/calculations/divide/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility  # Ensure correct import path

class DivideCommand(BaseCommand):
    def execute(self, *args):
        try:
            if len(args) < 2:
                raise ValueError("Division requires at least two numbers.")
            numbers = [float(arg) for arg in args]
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    raise ValueError("Division by zero is not allowed.")
                result /= num
            operation = " / ".join(map(str, numbers)) + f" = {result}"
            self.history_instance.add_record(operation, result)
            AdvancedLoggingUtility.info(f"Division operation successful: {operation}")
            return result
        except ValueError as e:
            error_msg = f"Error in division operation: {e}"
            AdvancedLoggingUtility.error(error_msg)
            return error_msg  # Returning the error message; adjust as needed for your application
