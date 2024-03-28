# Assuming this is part of app/plugins/history/delete/__init__.py
from app.command.base_command import BaseCommand
from app.advanced_logging_utility import AdvancedLoggingUtility  # Ensure correct import path

class DeleteCommand(BaseCommand):
    def execute(self, *args):
        if len(args) != 1:
            error_msg = "The delete command requires exactly one argument: the index of the record to delete."
            AdvancedLoggingUtility.warning(error_msg)
            print(error_msg)  # Optionally, consider if you want to keep this print statement
        else:
            try:
                index = int(args[0])
                if self.history_instance.delete_history(index):
                    success_msg = f"Successfully deleted record at index {index}."
                    AdvancedLoggingUtility.info(success_msg)
                    print(success_msg)  # Optionally, consider if you want to keep this print statement
                else:
                    failure_msg = f"Failed to delete record at index {index}. No record found."
                    AdvancedLoggingUtility.warning(failure_msg)
                    print(failure_msg)  # Optionally, consider if you want to keep this print statement
            except ValueError:
                error_msg = "Error: Index must be an integer."
                AdvancedLoggingUtility.error(error_msg)
                print(error_msg)  # Optionally, consider if you want to keep this print statement
