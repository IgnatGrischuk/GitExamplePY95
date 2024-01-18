def cyclic_sequence():
    while True:
        yield from [1, 2, 3, 4]


def main():
    try:
        count = int(input('Enter the number of digits to withdraw: '))
        if count < 0:
            print('Please enter positive digit.')
            return

        generator = cyclic_sequence()
        result = [next(generator) for _ in range(count)]
        print('Endless cyclic sequence: ', result)

    except ValueError:
        print('Please enter correct number.')


if __name__ == '__main__':
    main()
