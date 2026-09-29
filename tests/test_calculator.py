import runpy

from app.calculator import Calculator


def test_perform_calculation():
    calculator = Calculator()

    result = calculator.perform_calculation("add", 5, 3)

    assert result == 8
    assert calculator.history == [("add", 5, 3, 8)]

def test_get_history():
    calculator = Calculator()

    calculator.perform_calculation("add", 5, 3)
    calculator.perform_calculation("subtract", 10, 4)

    assert calculator.get_history() == [
        ("add", 5, 3, 8),
        ("subtract", 10, 4, 6),
    ]

def test_get_help():
    calculator = Calculator()

    help_text = calculator.get_help()

    assert "add" in help_text
    assert "subtract" in help_text
    assert "multiply" in help_text
    assert "divide" in help_text
    assert "history" in help_text
    assert "help" in help_text
    assert "exit" in help_text


def test_run_exit(monkeypatch, capsys):
    calculator = Calculator()

    monkeypatch.setattr("builtins.input", lambda _: "exit")

    calculator.run()

    captured = capsys.readouterr()

    assert "Professional Calculator" in captured.out
    assert "Goodbye!" in captured.out


def test_run_help_then_exit(monkeypatch, capsys):
    calculator = Calculator()

    commands = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    calculator.run()

    captured = capsys.readouterr()

    assert "Available commands:" in captured.out
    assert "add" in captured.out
    assert "history" in captured.out
    assert "Goodbye!" in captured.out


def test_run_history_empty_then_exit(monkeypatch, capsys):
    calculator = Calculator()

    commands = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    calculator.run()

    captured = capsys.readouterr()

    assert "No calculations in history." in captured.out
    assert "Goodbye!" in captured.out

def test_run_history_with_calculations_then_exit(monkeypatch, capsys):
    calculator = Calculator()

    calculator.perform_calculation("add", 5, 3)
    calculator.perform_calculation("subtract", 10, 4)

    commands = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    calculator.run()

    captured = capsys.readouterr()

    assert "add: 5, 3 = 8" in captured.out
    assert "subtract: 10, 4 = 6" in captured.out
    assert "Goodbye!" in captured.out


def test_run_add_then_exit(monkeypatch, capsys):
    calculator = Calculator()

    commands = iter(["add", "5", "3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    calculator.run()

    captured = capsys.readouterr()

    assert "Result: 8.0" in captured.out
    assert calculator.get_history() == [
        ("add", 5.0, 3.0, 8.0)
    ]
    assert "Goodbye!" in captured.out


def test_run_invalid_number_then_exit(monkeypatch, capsys):
    calculator = Calculator()

    commands = iter(["add", "abc", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    calculator.run()

    captured = capsys.readouterr()

    assert "Error:" in captured.out
    assert calculator.get_history() == []
    assert "Goodbye!" in captured.out


def test_run_divide_by_zero_then_exit(monkeypatch, capsys):
    calculator = Calculator()

    commands = iter(["divide", "10", "0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    calculator.run()

    captured = capsys.readouterr()

    assert "Error: Cannot divide by zero" in captured.out
    assert calculator.get_history() == []
    assert "Goodbye!" in captured.out


def test_run_invalid_command_then_exit(monkeypatch, capsys):
    calculator = Calculator()

    commands = iter(["power", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    calculator.run()

    captured = capsys.readouterr()

    assert "Invalid command. Type 'help' to see available commands." in captured.out
    assert "Goodbye!" in captured.out


def test_calculator_module_startup(monkeypatch):
    run_called = {"value": False}

    def fake_run(self):
        run_called["value"] = True

    monkeypatch.setattr(Calculator, "run", fake_run)

    runpy.run_module("app.calculator.__main__", run_name="__main__")

    assert run_called["value"] is True 


def test_calculator_module_does_not_start_when_not_main(monkeypatch):
    run_called = {"value": False}

    def fake_run(self):
        run_called["value"] = True

    monkeypatch.setattr(Calculator, "run", fake_run)

    runpy.run_module("app.calculator.__main__", run_name="not_main")

    assert run_called["value"] is False  