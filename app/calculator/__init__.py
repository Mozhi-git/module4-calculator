from app.calculation import CalculationFactory


class Calculator:
    def __init__(self):
        self.history = []


    def perform_calculation(self, operation: str, a: float, b: float) -> float:
        calculation = CalculationFactory.create_calculation(operation, a, b)
        result = calculation.calculate()
        self.history.append((operation.lower(), a, b, result))
        return result

    def get_history(self):
        return self.history