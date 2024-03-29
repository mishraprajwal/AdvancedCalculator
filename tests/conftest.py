"""conftest.py for pytest configurations and fixtures.

This module contains pytest fixtures and configurations used across
test modules in the project.
"""

import pytest
from app import App

@pytest.fixture
def app_instance():
    """Fixture to create an app instance."""
    return App()

# Ensure this file ends with a newline character.
