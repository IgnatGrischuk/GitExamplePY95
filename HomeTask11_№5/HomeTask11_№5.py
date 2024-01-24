class OperationStrategy:
    def execute(self, value_one, value_two):
        pass


class Addition(OperationStrategy):
    def execute(self, value_one, value_two):
        return value_one + value_two


class Subtraction(OperationStrategy):
    def execute(self, value_one, value_two):
        return value_one - value_two


class Multiplication(OperationStrategy):
    def execute(self, value_one, value_two):
        return value_one * value_two


class Division(OperationStrategy):
    def execute(self, value_one, value_two):
        if value_two == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return value_one / value_two


class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, num1, num2):
        if not self.strategy:
            raise ValueError("Strategy not set")
        return self.strategy.execute(num1, num2)


# Example of using
calculator = Calculator()

# Strategy of Addition
calculator.set_strategy(Addition())
result = calculator.calculate(5, 3)
print(f"Addition result: {result}")

# Strategy of Subtraction
calculator.set_strategy(Subtraction())
result = calculator.calculate(5, 3)
print(f"Subtraction result: {result}")

# Strategy of Multiplication
calculator.set_strategy(Multiplication())
result = calculator.calculate(5, 3)
print(f"Multiplication result: {result}")

# Strategy of Division
calculator.set_strategy(Division())
result = calculator.calculate(5, 3)
print(f"Division result: {result}")
