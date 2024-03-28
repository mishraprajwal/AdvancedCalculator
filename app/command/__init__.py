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
        """
        Parses the command input and executes the command if found,
        passing along any arguments.
        """
        parts = command_input.split()  # Split the input into parts
        if not parts:
            AdvancedLoggingUtility.warning("Empty command input.")
            return
        
        command_name, *args = parts
        try:
            if command_name in self.commands:
                self.commands[command_name].execute(*args)
                AdvancedLoggingUtility.info(f"Command '{command_name}' executed with arguments: {args}")
            else:
                raise KeyError(f"No such command: '{command_name}'")
        except KeyError as e:
            error_msg = str(e)
            AdvancedLoggingUtility.error(error_msg)
            print(error_msg)  # Optionally, consider if you still want to keep this print statement
        except Exception as e:
            error_msg = f"An error occurred during execution of command '{command_name}': {e}"
            AdvancedLoggingUtility.error(error_msg, exception=str(e), command=command_name)
            print(error_msg)  # Handling unexpected errors during command execution

