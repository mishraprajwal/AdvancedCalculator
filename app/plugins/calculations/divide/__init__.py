from app.command.base_command import BaseCommand
from app.calculation_history import CalculationHistory

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
            history_instance = CalculationHistory()
            history_instance.add_record(operation, result)
            print(operation)
            return result
        except ValueError as e:
            print(f"Error: {e}")
