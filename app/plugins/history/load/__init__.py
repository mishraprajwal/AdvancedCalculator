# Assuming this is part of app/plugins/history/load/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility  # Ensure correct import path

class LoadCommand(BaseCommand):
    def execute(self, *args):
        if len(args) > 0:
            error_msg = "The load command does not accept any arguments."
            AdvancedLoggingUtility.warning(error_msg)
            print(error_msg)  # Consider if you still need this with advanced logging in place
        else:
            if self.history_instance.load_history():
                success_msg = "Calculation history successfully loaded."
                AdvancedLoggingUtility.info(success_msg)
                print(success_msg)  # Consider if you still need this with advanced logging in place
            else:
                failure_msg = "Failed to load calculation history."
                AdvancedLoggingUtility.error(failure_msg)
                print(failure_msg)  # Consider if you still need this with advanced logging in place
