from testik_database_manager import TestikDB


def main():
    t = TestikDB()

    while True:
        print("Меню выбора:")
        print("1. Добавить тест")
        print("2. Обновить тест")
        print("3. Редактировать навание теста")
        print("4. Добавить вопрос к тесту по id. ")
        print("5. ")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        match choice:
            case "1":
                name = input("Введите название теста: ")
                if name.strip():
                    t.insert_test(name)
                else:
                    print("Вы ввели пустое название теста.")

            case "2":
                test_id = input("Введите ID теста, который хотите обновить: ")
                if test_id.strip() and test_id.isnumeric():
                    name = input("Введите новое название теста: ")
                    test_id = int(test_id)
                    t.update_test(name, test_id)
                else:
                    print(
                        "ID теста должен быть числом и не должен быть пустым.")
            case "3":
                test_id = input("Введите ID теста, который хотите удалить: ")
                if test_id.strip() and test_id.isnumeric():
                    test_id = int(test_id)
                    t.delete_test(test_id)
                else:
                    print(
                        "ID теста должен быть числом и не должен быть пустым.")

            case "4":
                test_id = input("Введите ID теста, в который хотите"
                                " добавить вопрос: ")
                test_id = int(test_id)

                t.insert_question(test_id)

            case "5":
                t.close()
                break
            case _:
                print("Некорректный ввод. Пожалуйста, выберите действие из "
                      "меню.")


def test_pass_menu(t):
    print("Меню прохождения теста:")
    test_id = input("Введите ID теста, который хотите пройти: ")
    if test_id.strip() and test_id.isnumeric():
        pass
    else:
        print("ID теста должен быть числом и не должен быть пустым.")


if __name__ == "__main__":
    main()
