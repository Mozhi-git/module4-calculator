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