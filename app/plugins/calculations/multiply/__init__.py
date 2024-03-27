from app.command.base_command import BaseCommand
from app.calculation_history import CalculationHistory

class MultiplyCommand(BaseCommand):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = 1
            for num in numbers:
                result *= num
            operation = " * ".join(map(str, numbers)) + f" = {result}"
            history_instance = CalculationHistory()
            history_instance.add_record(operation, result)
            print(operation)
            return result
        except ValueError:
            print("Error: All arguments must be numbers.")
