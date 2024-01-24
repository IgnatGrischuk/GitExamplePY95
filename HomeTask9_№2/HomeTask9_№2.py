class Math:

    @staticmethod
    def addition(value_one, value_two):
        return value_one + value_two

    @staticmethod
    def subtraction(value_one, value_two):
        return value_one - value_two

    @staticmethod
    def multiplication(value_one, value_two):
        return value_one * value_two

    @staticmethod
    def division(value_one, value_two):
        if value_two != 0:
            return value_one / value_two
        else:
            print("Error: Division by zero is not allowed")
            return None


# External code
math_operations = Math()

result_addition = math_operations.addition(10, 35)
print(f"Addition: 10 + 35 = {result_addition}")

result_subtraction = math_operations.subtraction(55, 70)
print(f"Subtraction: 55 - 70 = {result_subtraction}")

result_multiplication = math_operations.multiplication(100, 3000)
print(f"Multiplication: 100 * 3000 = {result_multiplication}")

result_division = math_operations.division(10, 0)
if result_division is not None:
    print(f"Division: 10 / 0 = {result_division}")

result_division_valid = math_operations.division(1000, 90)
if result_division_valid is not None:
    print(f"Division: 1000 / 90 = {result_division_valid}")
