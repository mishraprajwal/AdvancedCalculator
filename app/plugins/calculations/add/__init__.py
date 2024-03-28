from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility

class AddCommand(BaseCommand):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            operation = " + ".join(map(str, numbers)) + f" = {result}"
            
            # Record the operation and result using the logging utility
            AdvancedLoggingUtility.info(f"Executing operation: {operation}")
            self.history_instance.add_record(operation, result)
            
            # Optionally, log the successful addition operation
            AdvancedLoggingUtility.info(f"Operation successful: {operation}", operation=operation, result=result)
            return result
        except ValueError as e:
            # Log the error with additional context if needed
            AdvancedLoggingUtility.error("Error executing add command: All arguments must be numbers.", error=str(e))
            return "Error: All arguments must be numbers."
