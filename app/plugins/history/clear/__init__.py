# app/plugins/history/clear/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility  # Ensure correct import path

class ClearCommand(BaseCommand):
    def execute(self, *args):
        if len(args) > 0:
            error_msg = "The clear command does not accept any arguments."
            AdvancedLoggingUtility.warning(error_msg)
            print(error_msg)  # Consider if you still want to print this to stdout
        else:
            # Assuming self.history_instance is correctly initialized in BaseCommand
            self.history_instance.clear_history()
            success_msg = "Calculation history cleared."
            AdvancedLoggingUtility.info(success_msg)
            print(success_msg)  # Consider if you still want to print this to stdout
