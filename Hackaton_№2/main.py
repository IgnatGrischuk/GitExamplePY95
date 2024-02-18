from testik_database_manager import TestikDB


def main():
    t = TestikDB()

    while True:
        print("Меню выбора:")
        print("\t1. Добавить тест.")
        print("\t2. Переименовать тест.")
        print("\t3. Удаление теста.")
        print("\t4. Добавить вопрос к тесту по id.")
        print("\t5. Добавить ответ к вопросу по id.")
        print("\t6. Удалить тест по id.")
        print("\t7. Удалить вопрос по id.")
        print("\t8. Удалить ответ по id.")
        print("\t9. Вывести данные.")
        print("\t10. Пройти тест.")
        print("\t11. Выйти.")

        choice = input("Выберите действие: ")

        match choice:
            case "1":
                name = input("Введите название теста: ")
                t.insert_test(name)
            case "2":
                test_id = input("Введите ID теста, который хотите обновить: ")
                try:
                    test_id = int(test_id)
                except ValueError:
                    print("НЕ корректные значения")
                else:
                    if test_id in t.get_all_test_id():
                        name = input("Введите новое название теста: ")
                        t.update_test(name, test_id)
                    else:
                        print("Нет такого теста!")
            case "3":
                test_id = input("Введите ID теста, который хотите удалить: ")
                try:
                    test_id = int(test_id)
                except ValueError:
                    print("НЕ корректные значения")
                else:
                    t.delete_test(test_id)
            case "4":
                all_test_id = t.get_all_test_id()
                test_id = input("Введите ID теста, "
                                "в который хотите добавить вопрос: ")

                try:
                    test_id = int(test_id)

                except ValueError:
                    print("Вы ввели некоректные значения")
                else:
                    if test_id in all_test_id:
                        question_name = input("Введите название вопроса: ")
                        if question_name.strip():
                            t.insert_question(test_id, question_name.strip())
                        else:
                            print("Название теста не может быть пустым!")
                    else:
                        print("Нет такого теста!")
            case "5":
                question_id = input("Введите id вопроса, "
                                    "к которому добавим ответ: ")
                all_question_id = t.get_all_question_id()

                try:
                    question_id = int(question_id)
                except ValueError:
                    print("Нет такого вопроса!")
                else:
                    if question_id in all_question_id:
                        answer_name = input("Введите название вопроса: ")
                        is_answer = input("Введите верен ли ответ или нет"
                                          "(TRUE/FALSE): ")
                        if answer_name.strip():
                            t.insert_answer(question_id,
                                            answer_name.strip(),
                                            is_answer)
                        else:
                            print("Название ответа не может быть пустым!")
                    else:
                        print("Нет такого теста!")
            case "6":
                id = input("Введите id теста: ")
                try:
                    id = int(id)
                except ValueError:
                    print("Некорректный id!")
                else:
                    t.delete_test(id)
            case "7":
                id = input("Введите id вопроса: ")
                try:
                    id = int(id)
                except ValueError:
                    print("Некорректный id!")
                else:
                    if id in t.get_all_question_id():
                        t.delete_answers(id)
                        t.delete_question(id)
            case "8":
                id = input("Введите id ответа: ")
                try:
                    id = int(id)
                except ValueError:
                    print("Некорректный id!")
                else:
                    if id in t.get_all_answer_id():
                        t.delete_answer(id)
            case "9":
                t.select_data()
            case "10":
                t.pass_test()
            case "11":
                t.close()
                break
            case _:
                print("Некорректный ввод. Пожалуйста, выберите действие из "
                      "меню.")


if __name__ == "__main__":
    main()
