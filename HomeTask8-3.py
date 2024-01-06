import re
from collections import Counter

def find_most_common_word(line):
    words = re.findall(r'\b\w+\b', line.lower())
    word_counter = Counter(words)
    most_common_word, count = word_counter.most_common(1)[0]
    return most_common_word, count


def process_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                most_common_word, count = find_most_common_word(line)
                output_file.write(f"{most_common_word}: {count}\n")


if __name__ == '__main__':
    input_filename = 'Task1.txt'
    output_filename = 'Task1-1.txt'

    process_file(input_filename, output_filename)
    print('Программа успешно выполнена.', '\n')