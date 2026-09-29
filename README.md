# Module 4 Professional Calculator

This project is a command-line calculator application written in Python. It demonstrates object-oriented programming, error handling, testing with pytest, parameterized tests, and 100% test coverage.

## Features

- Addition, subtraction, multiplication, and division
- Command-line REPL interface
- Calculation history
- Help and exit commands
- Input validation and error handling
- Object-oriented design with inheritance and abstraction
- Factory design pattern
- Unit and parameterized testing with pytest
- 100% line and branch test coverage


## Project Structure

```text
module4-calculator/
├── app/
│   ├── calculator/
│   │   ├── __init__.py
│   │   └── __main__.py
│   ├── calculation/
│   │   └── __init__.py
│   └── operation/
│       └── __init__.py
├── tests/
│   ├── test_calculator.py
│   ├── test_calculations.py
│   └── test_operations.py
├── requirements.txt
├── README.md
└── .gitignore

## Setup

1. Clone the repository:

```bash
git clone git@github.com:Mozhi-git/module4-calculator.git

```

2. Enter the project directory:

```bash
cd module4-calculator
```

3. Create a virtual environment:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Calculator

Start the calculator with:

```bash
python -m app.calculator
```

## Available Commands

- `add` - Add two numbers
- `subtract` - Subtract the second number from the first
- `multiply` - Multiply two numbers
- `divide` - Divide the first number by the second
- `history` - Show calculations from the current session
- `help` - Show available commands
- `exit` - Exit the calculator

## Testing

Run all tests with:

```bash
python -m pytest
```

Check line and branch coverage with:

```bash
python -m pytest --cov=app --cov-branch --cov-report=term-missing
```

## Object-Oriented Design

The project uses several object-oriented programming concepts:

- `Operation` provides static methods for arithmetic operations.
- `Calculation` is an abstract base class.
- `AddCalculation`, `SubtractCalculation`, `MultiplyCalculation`, and `DivideCalculation` inherit from `Calculation`.
- `CalculationFactory` creates the correct calculation object based on the user's command.
- `Calculator` manages user interaction, calculation history, and the REPL interface.

## Error Handling

The application demonstrates both LBYL and EAFP error-handling approaches:

- LBYL (Look Before You Leap) is used to check conditions such as division by zero and valid commands.
- EAFP (Easier to Ask Forgiveness than Permission) is used with `try` and `except` to handle invalid numeric input and calculation errors.