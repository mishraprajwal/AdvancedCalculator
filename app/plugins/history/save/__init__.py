# Assuming this is part of app/plugins/history/save/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility  # Ensure correct import path

class SaveCommand(BaseCommand):
    def execute(self, *args):
        if len(args) > 0:
            error_msg = "The save command does not accept any arguments."
            AdvancedLoggingUtility.warning(error_msg)
            print(error_msg)  # Optionally, consider if you still want to keep this print statement
        else:
            try:
                self.history_instance.save_history()
                success_msg = "Calculation history successfully saved."
                AdvancedLoggingUtility.info(success_msg)
                print(success_msg)  # Optionally, consider if you still want to keep this print statement
            except Exception as e:
                failure_msg = f"Failed to save calculation history: {e}"
                AdvancedLoggingUtility.error(failure_msg)
                print(failure_msg)  # Optionally, consider if you still want to keep this print statement
