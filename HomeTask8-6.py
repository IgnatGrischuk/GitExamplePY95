import re


def calculate_summ_of_numbers(filename):
    total_sum = 0
    with open(filename, 'r') as file:
        content = file.read()
        numbers = re.findall(r'\d+', content)

        for number in numbers:
            total_sum += int(number)
    return total_sum


filename = 'TaskSix.txt'
result = calculate_summ_of_numbers(filename)
print(f"Сумма всех чисел в файле: {result}")
