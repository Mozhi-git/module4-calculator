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

    def get_help(self) -> str:
        return (
            "Available commands: "
            "add, subtract, multiply, divide, history, help, exit"
        )

    def run(self):
        print("Professional Calculator")
        print("Type 'help' to see available commands.")

        while True:
            command = input("Enter command: ").strip().lower()

            
            if command == "help":
                print(self.get_help())
                continue


            if command == "history":
                if not self.history:
                    print("No calculations in history.")
                else:
                    for operation, a, b, result in self.history:
                        print(f"{operation}: {a}, {b} = {result}")
                continue



            if command in {"add", "subtract", "multiply", "divide"}:
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))

                    result = self.perform_calculation(command, a, b)
                    print(f"Result: {result}")

                except ValueError as error:
                    print(f"Error: {error}")

                continue  
            
            
            
            if command == "exit":
                print("Goodbye!")
                break

            print("Invalid command. Type 'help' to see available commands.")