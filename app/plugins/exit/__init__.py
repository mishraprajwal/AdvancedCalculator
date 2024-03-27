import sys
from app.command.base_command import BaseCommand  # Adjusted import based on structure

class ExitCommand(BaseCommand):  # Inherits from BaseCommand
    def execute(self, *args):
        print("Exiting...")  # Print message before exiting
        sys.exit(0)  # Use exit code 0 to indicate a successful termination
