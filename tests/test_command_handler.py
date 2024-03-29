"""Test suite for CommandHandler functionality.

This module tests the CommandHandler class's ability to register, recognize,
and execute commands, as well as its handling of unknown commands.
"""

import logging
from unittest.mock import MagicMock
import pytest
from app.command import CommandHandler, Command


class MockCommand(Command):
    """A mock command class for testing command registration and execution."""
    def execute(self, *args):
        """Mock execution logic for a command."""
        print("Mock command executed.")


@pytest.fixture
def command_handler(caplog):
    """Fixture for creating a CommandHandler instance with logging level set to capture ERROR logs."""
    caplog.set_level(logging.ERROR)
    return CommandHandler()


def test_register_command(command_handler):
    """Ensure commands can be registered to the CommandHandler."""
    mock_command = MockCommand()
    command_name = "test"
    command_handler.register_command(command_name, mock_command)
    assert command_name in command_handler.commands, "Command should be registered within the handler."


def test_execute_registered_command(command_handler):
    """Verify that a registered command is executed properly."""
    mock_command = MockCommand()
    mock_command.execute = MagicMock()
    command_name = "mock"
    command_handler.register_command(command_name, mock_command)

    command_handler.execute_command(command_name)
    mock_command.execute.assert_called_once_with()


def test_execute_unknown_command_logs_error(command_handler, caplog):
    """Verify that executing an unknown command logs an appropriate error."""
    unknown_command_input = "unknown"
    command_handler.execute_command(unknown_command_input)
    expected_error_message = f"No such command: '{unknown_command_input}'"
    assert any(expected_error_message in message for message in caplog.messages), \
        "Executing an unknown command should log an error."
