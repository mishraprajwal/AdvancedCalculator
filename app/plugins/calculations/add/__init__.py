# Adjusted AddCommand to use self.history_instance
from app.command.base_command import BaseCommand

class AddCommand(BaseCommand):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            operation = " + ".join(map(str, numbers)) + f" = {result}"
            self.history_instance.add_record(operation, result)
            print(operation)
            return result
        except ValueError:
            print("Error: All arguments must be numbers.")
