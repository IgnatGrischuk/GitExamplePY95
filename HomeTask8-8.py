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


def add_employee_to_json(data, new_employee):
    data.append(new_employee)


def add_employee_to_csv(file_path, new_employee):
    data = read_csv_file(file_path)
    data.append(new_employee)
    write_csv_file(file_path, data)


def search_employee_by_name(data, name):
    for employee in data:
        if employee['name'] == name:
            return employee
    return None


def filter_by_programming_language(data, language):
    filtered_employees = [employee for employee in data if
                          language.lower() in map(str.lower,
                                                  employee['languages'])]
    return filtered_employees


def filter_by_birth_year(data, year):
    birth_year = datetime.strptime(year, '%d.%m.%Y').year
    filtered_employees = [employee for employee in data if
                          'birthday' in employee and datetime.strptime(
                              employee['birthday'],
                              '%d.%m.%Y').year < birth_year]
    return filtered_employees


def average_height(data):
    heights = [float(employee['height']) for employee in data]
    return sum(heights) / len(heights) if len(heights) > 0 else 0


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
            new_employee = {
                'name': input("Введите имя нового сотрудника: "),
                'birthday': input(
                    "Введите дату рождения нового сотрудника (в формате "
                    "dd.mm.yyyy): "),
                'height': input("Введите рост нового сотрудника: "),
                'weight': input("Введите вес нового сотрудника: "),
                'car': input(
                    "Есть ли у нового сотрудника машина (True/False): "
                    "").lower() == 'true',
                'languages': input(
                    "Введите языки программирования через запятую: ").split(
                    ','),
            }
            json_data = read_json_file(json_file_path)
            add_employee_to_json(json_data, new_employee)
            write_json_file(json_file_path, json_data)
            print("Информация о новом сотруднике добавлена в JSON")

        elif choice == '4':
            new_employee = {
                'name': input("Введите имя нового сотрудника: "),
                'birthday': input(
                    "Введите дату рождения нового сотрудника (в формате "
                    "dd.mm.yyyy): "),
                'height': input("Введите рост нового сотрудника: "),
                'weight': input("Введите вес нового сотрудника: "),
                'car': input(
                    "Есть ли у нового сотрудника машина (True/False): "
                    "").lower() == 'true',
                'languages': input(
                    "Введите языки программирования через запятую: ").split(
                    ','),
            }
            add_employee_to_csv(csv_file_path, new_employee)
            print("Информация о новом сотруднике добавлена в CSV")

        elif choice == '5':
            name_to_search = input("Введите имя сотрудника для поиска: ")
            json_data = read_json_file(json_file_path)
            employee = search_employee_by_name(json_data, name_to_search)
            if employee:
                print("Информация о сотруднике:")
                print(employee)
            else:
                print("Сотрудник с именем '{}' не найден.".format(
                    name_to_search))

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
            birth_year_to_filter = input(
                "Введите год рождения для фильтрации: ")
            json_data = read_json_file(json_file_path)
            filtered_employees = filter_by_birth_year(json_data,
                                                      birth_year_to_filter)
            average = average_height(filtered_employees)
            print(
                "Средний рост сотрудников, родившихся до {}: {:.2f} см".format(
                    birth_year_to_filter, average))

        elif choice == '8':
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите корректное действие.")


if __name__ == "__main__":
    main()
