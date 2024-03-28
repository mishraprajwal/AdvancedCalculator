# app/plugins/calculations/subtract/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility

class SubtractCommand(BaseCommand):
    def execute(self, *args):
        try:
            if len(args) < 2:
                raise ValueError("Subtraction requires at least two numbers.")
            numbers = [float(arg) for arg in args]
            result = numbers[0] - sum(numbers[1:])
            operation = " - ".join(map(str, numbers)) + f" = {result}"
            
            self.history_instance.add_record(operation, result)
            AdvancedLoggingUtility.info(f"Subtract operation successful: {operation}")
            return result
        except ValueError as e:
            AdvancedLoggingUtility.error("Error executing subtract command: All arguments must be numbers.", error=str(e))
            return "Error: All arguments must be numbers."
