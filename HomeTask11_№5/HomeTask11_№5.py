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


def get_numeric_input(self):
    while True:
        user_input = input(self)
        try:
            num = float(user_input)
            return num
        except ValueError:
            print("Please enter a valid number.")


# Example of using
calculator = Calculator()

# Strategy of Addition
calculator.set_strategy(Addition())
num1 = get_numeric_input("Enter the first number: ")
num2 = get_numeric_input("Enter the second number: ")
result = calculator.calculate(num1, num2)
print(f"Addition result: {result}")

# Strategy of Subtraction
calculator.set_strategy(Subtraction())
num1 = get_numeric_input("Enter the first number: ")
num2 = get_numeric_input("Enter the second number: ")
result = calculator.calculate(num1, num2)
print(f"Subtraction result: {result}")

# Strategy of Multiplication
calculator.set_strategy(Multiplication())
num1 = get_numeric_input("Enter the first number: ")
num2 = get_numeric_input("Enter the second number: ")
result = calculator.calculate(num1, num2)
print(f"Multiplication result: {result}")

# Strategy of Division
calculator.set_strategy(Division())
num1 = get_numeric_input("Enter the first number: ")
num2 = get_numeric_input("Enter the second number (not zero): ")
result = calculator.calculate(num1, num2)
print(f"Division result: {result}")
