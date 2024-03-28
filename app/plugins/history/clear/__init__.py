# app/plugins/history/clear/__init__.py
from app.command.base_command import BaseCommand

class ClearCommand(BaseCommand):
    def execute(self, *args):
        if len(args) > 0:
            print("The clear command does not accept any arguments.")
        else:
            # Assuming self.history_instance is initialized in BaseCommand
            self.history_instance.clear_history()
            print("Calculation history cleared.")
