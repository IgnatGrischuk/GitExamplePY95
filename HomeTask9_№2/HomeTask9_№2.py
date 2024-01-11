class Math:

    def addition(self, value_one, value_two):
        result = value_one + value_two
        print(f"Addition: {value_one} + {value_two} = {result}")

    def subtraction(self, value_one, value_two):
        result = value_one + value_two
        print(f"Subtraction: {value_one} - {value_two} = {result}")

    def multiplication(self, value_one, value_two):
        result = value_one * value_two
        print(f"Multiplication: {value_one} + {value_two} = {result}")

    def division(self, value_one, value_two):
        if value_two != 0:
            result = value_one / value_two
            print(f"Division: {value_one} / {value_two} = {result}")
        else:
            print(f"Error: Division by zero is not allowed")


math_operations = Math()

math_operations.addition(10, 35)
math_operations.subtraction(55, 70)
math_operations.multiplication(100, 3000)
math_operations.division(10, 0)
math_operations.division(1000, 90)
