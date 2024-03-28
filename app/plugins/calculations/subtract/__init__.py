# app/plugins/calculations/subtract/__init__.py
from app.command.base_command import BaseCommand

class SubtractCommand(BaseCommand):
    def execute(self, *args):
        try:
            if len(args) < 2:
                raise ValueError("Subtraction requires at least two numbers.")
            numbers = [float(arg) for arg in args]
            result = numbers[0] - sum(numbers[1:])
            operation = " - ".join(map(str, numbers)) + f" = {result}"
            self.history_instance.add_record(operation, result)
            print(operation)  # Optionally, print the operation and result
            return result
        except ValueError as e:
            print(f"Error: {e}")
