import json
import csv
from datetime import datetime


def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def write_json_file(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def read_csv_file(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]
    return data


def write_csv_file(file_path, data):
    fieldnames = list(data[0].keys()) if data else []
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)


def get_valid_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            datetime.strptime(date_str, '%d.%m.%Y')
            return date_str
        except ValueError:
            print("Ошибка: Введите корректную дату (в формате dd.mm.yyyy).")


def get_valid_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число.")


def add_new_employee():
    new_employee = {
        'name': input("Введите имя нового сотрудника: "),
        'birthday': get_valid_date_input("Введите дату рождения: "),
        'height': get_valid_float_input("Введите рост: "),
        'weight': get_valid_float_input("Введите вес: "),
        'car': input(
            "Есть ли у сотрудника машина (True/False): ").lower() == 'true',
        'languages': input(
            "Введите языки программирования через запятую: ").split(','),
    }
    return new_employee


def add_employee_to_json(data, new_employee):
    data.append(new_employee)


def add_employee_to_csv(file_path, new_employee):
    data = read_csv_file(file_path)
    data.append(new_employee)
    write_csv_file(file_path, data)


def search_employee_by_name(data, name):
    for employee in data:
        if employee['name'].lower() == name.lower():
            return employee
    return None


def display_employee_info(employee):
    if employee:
        print("\nИнформация о сотруднике:")
        print(f"Имя: {employee['name']}")
        print(f"Дата рождения: {employee['birthday']}")
        print(f"Рост: {employee['height']} см")
        print(f"Вес: {employee['weight']} кг")
        print(f"Машина: {'Да' if employee['car'] else 'Нет'}")
        print(f"Языки программирования: {', '.join(employee['languages'])}")
    else:
        print("\nСотрудник не найден.")


# noinspection PyTypeChecker
def filter_by_programming_language(data, language):
    filtered_employees = [employee for employee in data if
                          language.lower() in map(str.lower,
                                                  employee['languages'])]
    return filtered_employees


def filter_by_birth_year(data, year):
    try:
        birth_year = int(year)
        if not 1900 <= birth_year <= 9999:
            raise ValueError("Год рождения должен быть в диапазоне от 1900 "
                             "до 9999.")
    except ValueError:
        print("Ошибка: Введите корректный год"
              " рождения (число в формате YYYY).")
        return []

    filtered_employees = [employee for employee in data if
                          'birthday' in employee and
                          datetime.strptime(employee['birthday'],
                                            '%d.%m.%Y').year < birth_year]

    if not filtered_employees:
        print("Сотрудники с указанным годом рождения не найдены.")
    return filtered_employees


def average_height(data):
    heights = [float(employee['height']) for employee in data]
    return sum(heights) / len(heights) if len(heights) > 0 else 0


# noinspection PyArgumentList
def main():
    json_file_path = 'employees.json'
    csv_file_path = 'employees.csv'

    while True:
        print("\nВыберите действие:")
        print("1. Считать данные из JSON и преобразовать в CSV")
        print("2. Сохранить данные в CSV")
        print("3. Добавить информацию о новом сотруднике в JSON")
        print("4. Добавить информацию о новом сотруднике в CSV")
        print("5. Вывести информацию о сотруднике по имени")
        print("6. Фильтр по языку программирования")
        print("7. Фильтр по году рождения")
        print("8. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':
            json_data = read_json_file(json_file_path)
            write_csv_file(csv_file_path, json_data)
            print("Данные успешно преобразованы в CSV")

        elif choice == '2':
            csv_data = read_csv_file(csv_file_path)
            write_csv_file(csv_file_path, csv_data)
            print("Данные успешно сохранены в CSV")

        elif choice == '3':
            new_employee = add_new_employee()
            json_data = read_json_file(json_file_path)
            add_employee_to_json(json_data, new_employee)
            write_json_file(json_file_path, json_data)
            print("Информация о новом сотруднике добавлена в JSON")

        elif choice == '4':
            new_employee = add_new_employee()
            add_employee_to_csv(csv_file_path, new_employee)
            print("Информация о новом сотруднике добавлена в CSV")

        elif choice == '5':
            name_to_search = input(
                "Введите имя сотрудника для поиска: ").strip()
            json_data = read_json_file(json_file_path)
            employee = search_employee_by_name(json_data, name_to_search)
            display_employee_info(employee)

        elif choice == '6':
            language_to_filter = input(
                "Введите язык программирования для фильтрации: ")
            json_data = read_json_file(json_file_path)
            filtered_employees = (filter_by_programming_language
                                  (json_data, language_to_filter))
            print("Сотрудники, владеющие языком программирования '{}':".format(
                language_to_filter))
            for employee in filtered_employees:
                print(employee)

        elif choice == '7':
            birth_year_to_filter = filter_by_birth_year()
            json_data = read_json_file(json_file_path)
            filtered_employees = filter_by_birth_year(json_data,
                                                      birth_year_to_filter)
            average = average_height(filtered_employees)
            print(
                f"Средний рост сотрудников, родившихся до "
                f"{birth_year_to_filter}: {average:.2f} см")
        elif choice == '8':
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите корректное действие.")


if __name__ == "__main__":
    main()
