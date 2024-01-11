import json
import random


# Считываем Json файл
def get_words(mode: str):
    with open("Wonderland.json", "r") as json_file:
        words = json.load(json_file)
    return get_rand_word(words[mode])


# Выбираем рандомное слово из списка слов
def get_rand_word(words):
    print(words)
    words = random.choice(words)
    return words


if __name__ == '__main__':
    word = get_words('easy_words')


# Делаем проверку на ввод одной буквы
def input_letter():
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    letter = input('Введите вашу букву: ')
    if 0 < len(letter) < 2:
        if letter in alphabet:
            return letter
        else:
            print('Введена не корректная буква')
            return input_letter()
    else:
        print('Введите вашу букву')
        return letter


# Делаем проверку на введенное слово

def is_letter_in_word(letter, word):
    return letter in word


def is_word_in_word_list(word, words_list):
    return word in words_list


is_word_in_word_list()
