# app/plugins/calculations/divide/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility

class DivideCommand(BaseCommand):
    def execute(self, *args):
        try:
            if len(args) < 2:
                raise ValueError("Division requires at least two numbers.")
            numbers = [float(arg) for arg in args]
            result = numbers[0]
            for number in numbers[1:]:
                if number == 0:
                    raise ValueError("Division by zero is not allowed.")
                result /= number
            operation = " / ".join(map(str, numbers)) + f" = {result}"
            
            self.history_instance.add_record(operation, result)
            AdvancedLoggingUtility.info(f"Divide operation successful: {operation}")
            return result
        except ValueError as e:
            AdvancedLoggingUtility.error("Error executing divide command: ", error=str(e))
            return str(e)
