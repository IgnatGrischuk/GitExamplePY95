with open('StudentsMarks.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    words = line.split()

    if (len(words) == 3 and words[0].lower() == 'surname' and words[1].lower()
            == 'name' and words[2].lower() == 'grade'):
        continue

    try:
        surname, name, grade = words
        grade = int(grade)

        if grade < 3:
            print(f'{surname} {name}: {grade}')

    except ValueError:
        print(f"Ошибка при обработке строки: {line}")
    except IndexError:
        print(f"Некорректный формат данных в строке: {line}")
