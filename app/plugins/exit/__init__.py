import sys
from app.command import Command

class ExitCommand(Command):
    def execute(self):
        print("Exiting application.")  # Print the message before exiting
        sys.exit(0)  # It's more standard to exit with a status code, e.g., 0 for success
