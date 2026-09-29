import pytest


from app.calculation import (
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    CalculationFactory,
)

def test_add_calculation():
    calculation = AddCalculation(5, 3)
    assert calculation.calculate() == 8

def test_subtract_calculation():
    calculation = SubtractCalculation(10, 4)
    assert calculation.calculate() == 6

def test_multiply_calculation():
    calculation = MultiplyCalculation(6, 4)
    assert calculation.calculate() == 24

def test_divide_calculation():
    calculation = DivideCalculation(20, 4)
    assert calculation.calculate() == 5.0


def test_factory_creates_add_calculation():
    calculation = CalculationFactory.create_calculation("add", 5, 3)

    assert isinstance(calculation, AddCalculation)
    assert calculation.calculate() == 8


def test_factory_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create_calculation("power", 5, 3)


@pytest.mark.parametrize(
    "operation, a, b, expected_class, expected_result",
    [
        ("add", 5, 3, AddCalculation, 8),
        ("subtract", 10, 4, SubtractCalculation, 6),
        ("multiply", 6, 4, MultiplyCalculation, 24),
        ("divide", 20, 4, DivideCalculation, 5.0),
    ],
)


def test_factory_operations(operation, a, b, expected_class, expected_result):
    calculation = CalculationFactory.create_calculation(operation, a, b)

    assert isinstance(calculation, expected_class)
    assert calculation.calculate() == expected_result        