def fibonacci_generator(sequence):
    value_one, value_two = 0, 1
    while value_one < sequence:
        yield value_one
        value_one, value_two = value_two, value_one + value_two


def main():
    try:
        sequence = int(input('Enter the number to which you want'
                             ' to print sequence: '))
        if sequence < 0:
            print('The value must be positive.')
            return

        fibonacci_sequence = list(fibonacci_generator(sequence))
        print(fibonacci_sequence)

        print(f"Fibonacci sequence up to {sequence} ")
    except ValueError:
        print('Error:Enter correct number. ')


if __name__ == '__main__':
    main()
