# Assuming this is part of app/command/__init__.py
from abc import ABC, abstractmethod
from app.advanced_logging_utility import AdvancedLoggingUtility  # Ensure correct import path

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        """Execute the command with given arguments."""
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
        AdvancedLoggingUtility.info(f"Command '{command_name}' registered.")

    def execute_command(self, command_input: str):
        parts = command_input.split()
        if not parts:
            AdvancedLoggingUtility.warning("No command provided.")
            return
        
        command_name, *args = parts
        if command_name not in self.commands:
            error_msg = f"No such command: '{command_name}'"
            AdvancedLoggingUtility.error(error_msg)
            print(error_msg)  # Printing the error message for direct user feedback
            return  # Early return to stop execution if command is not found

        try:
            # At this point, command_name is guaranteed to be in self.commands
            self.commands[command_name].execute(*args)
            AdvancedLoggingUtility.info(f"Command '{command_name}' executed with arguments: {args}")
        except Exception as e:
            error_msg = f"An error occurred during execution of command '{command_name}': {e}"
            AdvancedLoggingUtility.error(error_msg, exception=str(e), command=command_name)
            print(error_msg)  # Handling unexpected errors during command execution

