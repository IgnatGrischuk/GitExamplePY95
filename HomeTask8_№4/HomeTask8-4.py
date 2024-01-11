import re


def load_stop_words(filename):
    stop_words = set()

    try:
        with open(filename, 'r') as stop_words_file:
            for line in stop_words_file:
                words = line.strip().split()
                stop_words.update(words)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")

    return stop_words


def censor_text(input_filename, stop_words_filename):
    stop_words = load_stop_words(stop_words_filename)

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

            for word in stop_words:
                content = re.sub(
                    fr'\b{re.escape(word)}\b|\b{re.escape(word)}[.,;!?]*',
                    '*' * len(word), content, flags=re.IGNORECASE)

            print(content)
    except FileNotFoundError:
        print(f"Файл {input_filename} не найден.")


input_filename = 'Task_4.txt'
stop_words_filename = 'stop_words.txt'
censor_text(input_filename, stop_words_filename)
