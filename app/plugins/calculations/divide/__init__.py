# In app/plugins/calculations/divide/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility

class DivideCommand(BaseCommand):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    raise ValueError("Division by zero is not allowed.")
                result /= num
            operation = " / ".join(map(str, numbers)) + f" = {result}"
            
            self.history_instance.add_record(operation, result)
            AdvancedLoggingUtility.info(f"Divide operation successful: {operation}")
            return result
        except ValueError as e:
            error_msg = f"Error executing divide command: {e}"
            AdvancedLoggingUtility.error(error_msg)
            return error_msg
