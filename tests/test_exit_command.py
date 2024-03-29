"""Module to test the ExitCommand functionality."""

from app.plugins.exit import ExitCommand

def test_exit_command_exits_application(capfd, monkeypatch):
    """Test the ExitCommand results in application exit with the correct message."""
    exit_status = []

    # Directly append the status code to the list without using lambda
    def mock_exit(status_code):
        exit_status.append(status_code)

    monkeypatch.setattr("sys.exit", mock_exit)

    # Instantiate and execute the command
    command = ExitCommand()
    command.execute()

    # Capture the output
    out, _ = capfd.readouterr()

    # Check the exit status and output message
    assert exit_status == [0], "ExitCommand should exit with status code 0"
    assert "Exiting application." in out, "ExitCommand should print 'Exiting application.' before exiting"
