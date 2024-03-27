from app.command.base_command import BaseCommand
from app.calculation_history import CalculationHistory

class SubtractCommand(BaseCommand):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = numbers[0] - sum(numbers[1:])
            operation = " - ".join(map(str, numbers)) + f" = {result}"
            history_instance = CalculationHistory()
            history_instance.add_record(operation, result)
            print(operation)
            return result
        except ValueError:
            print("Error: All arguments must be numbers.")
