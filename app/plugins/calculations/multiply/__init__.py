# app/plugins/calculations/multiply/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility

class MultiplyCommand(BaseCommand):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = 1
            for number in numbers:
                result *= number
            operation = " * ".join(map(str, numbers)) + f" = {result}"
            
            self.history_instance.add_record(operation, result)
            AdvancedLoggingUtility.info(f"Multiply operation successful: {operation}")
            return result
        except ValueError as e:
            AdvancedLoggingUtility.error("Error executing multiply command: All arguments must be numbers.", error=str(e))
            return "Error: All arguments must be numbers."
