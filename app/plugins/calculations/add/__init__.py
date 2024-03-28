# app/plugins/calculations/add/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility

class AddCommand(BaseCommand):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            operation = " + ".join(map(str, numbers)) + f" = {result}"
            
            # Record the operation and result
            self.history_instance.add_record(operation, result)
            
            AdvancedLoggingUtility.info(f"Add operation successful: {operation}")
            return result
        except ValueError as e:
            AdvancedLoggingUtility.error("Error executing add command: All arguments must be numbers.", error=str(e))
            return "Error: All arguments must be numbers."
