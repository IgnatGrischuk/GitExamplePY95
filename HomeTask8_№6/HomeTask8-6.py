def calculate_sum_of_numbers(filename):
    total_sum = 0
    current_number = 0

    with open(filename, 'r') as file:
        content = file.read()

        for char in content:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            else:
                total_sum += current_number
                current_number = 0

        # Take into account the last number in the file (if it exists)
        total_sum += current_number

    return total_sum


filename = 'Task_6.txt'
result = calculate_sum_of_numbers(filename)
print(f"Сумма всех чисел в файле: {result}")
