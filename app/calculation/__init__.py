from abc import ABC, abstractmethod
from app.operation import Operation


class Calculation(ABC):
    """Abstract base class for calculator operations."""


    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    @abstractmethod
    def calculate(self) -> float:
        pass  # pragma: no cover


class AddCalculation(Calculation):
    def calculate(self) -> float:
        return Operation.add(self.a, self.b)


class SubtractCalculation(Calculation):
    def calculate(self) -> float:
        return Operation.subtract(self.a, self.b)


class MultiplyCalculation(Calculation):
    def calculate(self) -> float:
        return Operation.multiply(self.a, self.b)


class DivideCalculation(Calculation):
    def calculate(self) -> float:
        return Operation.divide(self.a, self.b)


class CalculationFactory:
    """Creates calculation objects based on the requested operation."""


    @staticmethod
    def create_calculation(operation: str, a: float, b: float) -> Calculation:
        """Create the appropriate calculation object for the requested operation."""
        calculation_types = {
            "add": AddCalculation,
            "subtract": SubtractCalculation,
            "multiply": MultiplyCalculation,
            "divide": DivideCalculation,
        }

        calculation_class = calculation_types.get(operation.lower())

        if calculation_class is None:
            raise ValueError("Invalid operation")

        return calculation_class(a, b)