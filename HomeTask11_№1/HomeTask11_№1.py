def fibonacci_generator(sequence):
    value_one, value_two = 0, 1
    count = 0
    while count < sequence:
        yield value_one
        value_one, value_two = value_two, value_one + value_two
        count += 1


def main():
    try:
        sequence = int(input('Enter the number of elements you want '
                             'in the Fibonacci sequence: '))
        if sequence <= 0:
            print('The value must be a positive integer.')
            return

        fibonacci_sequence = list(fibonacci_generator(sequence))
        print(fibonacci_sequence)

        print(f"Fibonacci sequence with {sequence} elements:")
    except ValueError:
        print('Error: Enter a correct number.')


if __name__ == '__main__':
    main()
