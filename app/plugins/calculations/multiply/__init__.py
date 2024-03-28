# app/plugins/calculations/multiply/__init__.py
from app.command.base_command import BaseCommand

class MultiplyCommand(BaseCommand):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = 1
            for num in numbers:
                result *= num
            operation = " * ".join(map(str, numbers)) + f" = {result}"
            self.history_instance.add_record(operation, result)
            print(operation)  # Optionally, print the operation and result
            return result
        except ValueError:
            print("Error: All arguments must be numbers.")
