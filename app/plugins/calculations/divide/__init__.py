# app/plugins/calculations/divide/__init__.py
from app.command.base_command import BaseCommand

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
            print(operation)  # Optionally, print the operation and result
            return result
        except ValueError as e:
            print(f"Error: {e}")
