<div align="center">

# 🧮 Advanced Calculator Application

An elegant CLI application for arithmetic operations, designed with extensibility and ease of use at its core.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)

</div>

## 📜 Overview

The **Advanced Calculator** is crafted to perform arithmetic calculations, leveraging a dynamic plugin system for seamless integration of functionalities. With Pandas for efficient history management and sophisticated logging, it stands as a robust tool for both simple and complex operations.

## ✨ Features

- **Arithmetic Mastery**: Expertly handles `addition`, `subtraction`, `multiplication`, and `division`.
- **Expandable Ecosystem**: A dynamic plugin system invites endless possibilities.
- **Historical Insights**: Employs Pandas for a comprehensive calculation history.
- **Insightful Logging**: Advanced practices provide clarity and insight into operations.
- **Structured Commands**: The command pattern ensures tidy command execution.

## 🚀 Getting Started

### Prerequisites

- 🐍 Python 3.8 or newer
- 📦 Pip package manager

### Installation, Usage and Setting Up the Development Environment

1. **Get the Code**:
    ```bash
    git clone https://github.com/mishraprajwal/AdvancedCalculator.git
    ```

For an optimal development experience and to manage dependencies effectively, it's recommended to set up a virtual environment for the Advanced Python Calculator project. Below are the steps to create and activate a virtual environment on Unix-based systems:

2. **Create a Virtual Environment**:
   Navigate to the project's root directory and execute the following command to create a virtual environment named `venv`. This isolates the project's dependencies from the global Python environment.

   ```bash
   virtualenv venv
   ```
   To activate the virtual environment.

   ```bash
   source ./venv/bin/activate
   ```


3. **Dependencies Away**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Launch**:
    ```bash
    python main.py
    ```

5. **Calculate Away**:
    Engage with the CLI for your mathematical needs. Examples:
    - `>>> add 2 3`
    - `>>> subtract 10 3`
    - ... and more.

## 🛠️ Extending the Application

Eager to contribute? Extend the calculator by:
- Creating a module in `app/plugins`.
- Defining a command class inheriting `BaseCommand`.
- Your new command awakens upon next startup!

## 📖 Calculation History Management

Navigate through time with the `CalculationHistory` class—load, save, clear, or delete records with grace and efficiency.

## 📚 Logging

Dive into the depths of operations with finely-tuned logging, categorizing messages for an insightful development and debugging experience.

## 🧪 Testing

Our application is committed to quality and reliability, as demonstrated through comprehensive test coverage. We utilize `pytest` for testing various components, ensuring that each functionality behaves as expected. Tests cover command execution, calculation history management, and the dynamic plugin system.

To run the tests:

```bash
pytest
```

```bash
pytest --pylint
```

```bash
pytest --pylint --cov
```

<div align="center">

by [Prajwal Karunesh Mishra - pm735@njit.edu](https://github.com/mishraprajwal)

</div>

