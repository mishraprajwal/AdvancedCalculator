# Advanced Calculator Application

## Overview

The Advanced Calculator is a powerful CLI application designed for performing arithmetic operations with a focus on extensibility and ease of use. Leveraging a dynamic plugin system, the application allows for easy integration of new commands and functionalities. Utilizing Pandas for calculation history management and incorporating advanced logging practices, it offers a robust solution for arithmetic operations and beyond.

## Features

- **Arithmetic Operations**: Supports basic operations like addition, subtraction, multiplication, and division.
- **Dynamic Plugin System**: Facilitates the seamless addition of new functionalities through plugins.
- **Calculation History Management**: Employs Pandas for efficient handling of calculation history.
- **Professional Logging**: Implements comprehensive logging for operational insights and error tracking.
- **Command Pattern Architecture**: Utilizes the command pattern for structured command execution within the REPL.

## Getting Started

### Prerequisites

- Python 3.8+
- Pip

### Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/mishraprajwal/AdvancedCalculator.git
   cd advanced-calculator

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the application:
    ```bash
    python main.py

4. Usage
Once the application is running, use the command line interface to perform calculations. Example commands include:

add 2 3 - Adds the numbers.
subtract 5 2 - Subtracts the second number from the first.
multiply 4 2 - Multiplies the numbers.
divide 8 2 - Divides the first number by the second.
exit - Closes the application.

5. Extending the Application
To add new commands or functionalities:

-> Create a new Python module in the app/plugins directory.
-> Define a new command class inheriting from BaseCommand and implement the execute method.
-> Ensure the module is named appropriately for automatic recognition and loading by the application.

6. Calculation History Management
The CalculationHistory class, utilizing Pandas, manages the history of calculations, supporting operations like loading, saving, clearing, and deleting records efficiently.

7. Logging
Advanced logging practices are implemented, differentiating log messages by severity (INFO, WARNING, ERROR) and allowing for dynamic logging configuration through environment variables.



