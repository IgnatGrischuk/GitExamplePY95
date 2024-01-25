def calculator(number_one, number_two, operation):
    try:
        if operation == '+':
            result = number_one + number_two
        elif operation == '-':
            result = number_one - number_two
        elif operation == '*':
            result = number_one * number_two
        elif operation == '/':
            result = number_one / number_two
        else:
            raise ValueError('Неверная операция.'
                             ' Поддерживаются только: +, -, *, /')
        return result
    except ZeroDivisionError as zero_error:
        raise ValueError(f"Ошибка при выполнении операции: {zero_error}")
    except ValueError as value_error:
        raise ValueError(f"Ошибка при выполнении операции: {value_error}")


# Example of using:
try:
    result = calculator(10, 0, '/')
    print(result)
except ValueError as e:
    print(e)
