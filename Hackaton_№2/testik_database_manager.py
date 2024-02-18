import json
import psycopg2
from psycopg2 import sql, extensions


class TestikDB:
    def __init__(self):
        self.config = TestikDB.get_config()

        self.conn = psycopg2.connect(
            dbname=self.config['dbname'],
            user=self.config['user'],
            password=self.config['password'],
            host=self.config['host'],
            port=self.config['port'])
        self.conn.set_session(autocommit=True)
        self.cursor = self.conn.cursor()

        self.create_tables()

    @staticmethod
    def get_config() -> dict:
        with open('config.json') as config_file:
            return json.load(config_file)

    def create_tables(self):
        query = sql.SQL("CREATE TABLE IF NOT EXISTS test("
                        "id SERIAL PRIMARY KEY,"
                        "name VARCHAR(255)"
                        ");")
        self.cursor.execute(query, )

        query = sql.SQL("CREATE TABLE IF NOT EXISTS question("
                        "id SERIAL PRIMARY KEY,"
                        "test_id INTEGER,"
                        "FOREIGN KEY (test_id) REFERENCES test (id) "
                        "ON UPDATE CASCADE ON DELETE CASCADE,"
                        "question_name VARCHAR(255) NOT NULL"
                        ");")
        self.cursor.execute(query, )

        query = sql.SQL("CREATE TABLE IF NOT EXISTS answer("
                        "id SERIAL PRIMARY KEY,"
                        "question_id INTEGER REFERENCES question(id),"
                        "answer VARCHAR(255),"
                        "is_correct_answer BOOLEAN"
                        ");")
        self.cursor.execute(query, )

    def insert_test(self, name: str):
        query = sql.SQL("INSERT INTO test (name) VALUES (%s)")
        self.cursor.execute(query, (name,))

    def update_test(self, name: str, id: int):
        query = sql.SQL("UPDATE test SET name = %s WHERE id = %s")
        self.cursor.execute(query, (name, id,))

    def get_all_question_id(self):
        query = sql.SQL("SELECT id FROM question")
        self.cursor.execute(query, )
        q_id = self.cursor.fetchall()

        id_in_q = list()

        for id in q_id:
            id_in_q.append(id[0])

        return id_in_q

    def get_all_test_id(self):
        query = sql.SQL("SELECT id FROM test")
        self.cursor.execute(query, )
        test_id = self.cursor.fetchall()

        id_in_test = list()

        for id in test_id:
            id_in_test.append(id[0])

        return id_in_test

    def get_all_answer_id(self):
        query = sql.SQL("SELECT id FROM answer")
        self.cursor.execute(query, )
        answer_id = self.cursor.fetchall()

        id_in_answer = list()

        for id in answer_id:
            id_in_answer.append(id[0])

        return id_in_answer

    def insert_question(self, test_id: int, question_name: str):

        query = sql.SQL("insert into Question(test_id, question_name)"
                        " values (%s, %s);")

        self.cursor.execute(query, (test_id, question_name,))

    def update_question(self, id: int, section_name: str, section_value: str):
        if section_name == "test_id":
            section_value = int(section_value)

        query = sql.SQL(f"update Question set {section_name} = %s "
                        f"where id = %s")

        self.cursor.execute(query, (section_value, id))

    def insert_answer(self, question_id: int, answer: str,
            is_correct_answer):

        query = sql.SQL("insert into answer(question_id, answer, "
                        "is_correct_answer)"
                        " values (%s, %s, %s);")

        self.cursor.execute(query, (question_id, answer, is_correct_answer))

    def update_answer(self, id, section_name, section_value):

        query = sql.SQL(f"update answer set {section_name} = %s "
                        f"where id = %s")

        self.cursor.execute(query, (section_value, id))

    def delete_answer(self, id: int):
        query = sql.SQL("DELETE FROM answer WHERE id = %s;")
        self.cursor.execute(query, (id,))

    def delete_answers(self, id: int):
        query = sql.SQL("DELETE FROM answer WHERE question_id = %s;")
        self.cursor.execute(query, (id,))

    def delete_question(self, id: int):
        query = sql.SQL("DELETE FROM question WHERE id = %s;")
        self.cursor.execute(query, (id,))

    def delete_test(self, test_id: int):
        query = sql.SQL(
            "DELETE FROM answer WHERE question_id "
            "IN (SELECT id FROM question WHERE test_id = %s);"
            "DELETE FROM question WHERE test_id = %s;"
            "DELETE FROM test WHERE id = %s;")
        self.cursor.execute(query, (test_id, test_id, test_id))

    def select_data(self):
        query = sql.SQL("SELECT test.id, "
                        "test.name, "
                        "question.id, "
                        "question.test_id, "
                        "question.question_name, "
                        "answer.id, "
                        "answer.question_id, "
                        "answer.answer, "
                        "answer.is_correct_answer FROM test "
                        "FULL JOIN "
                        "question on test.id = question.test_id "
                        "FULL JOIN "
                        "answer on answer.question_id = question.id ")

        self.cursor.execute(query, )
        data = self.cursor.fetchall()

        print(
            "    Test ID   |"
            "     Test Name      |"
            " Question ID  |"
            " Question Test ID |"
            "    Question Name   |"
            "  Answer ID   |"
            " Answer Question ID |"
            "       Answer       |"
            "  Is Correct Answer  ")

        # Печатаем данные построчно
        for row in data:
            test_id, \
                test_name, \
                question_id, \
                question_test_id, \
                question_name, \
                answer_id, \
                answer_question_id, \
                answer, \
                is_correct_answer = row
            print(
                f" {str(test_id):12} |"
                f" {str(test_name):18} |"
                f" {str(question_id):12} |"
                f" {str(question_test_id):16} |"
                f" {str(question_name):18} |"
                f" {str(answer_id):12} |"
                f" {str(answer_question_id):18} |"
                f" {str(answer):18} |"
                f" {str(is_correct_answer):18}")

    def pass_test(self):
        test_id = int(input("Введите ID теста, который хотите пройти: "))
        questions = self.get_questions_for_test(test_id)
        if not questions:
            print("Вопросов по данному тесту не найдено.")
            return

        for question_id, question_name in questions:
            print(f"Вопрос {question_id}: {question_name}")
            print("Выберите ответ (True/False):")
            user_answer = input().strip().lower()

            if user_answer == 'true':
                user_answer = True
            elif user_answer == 'false':
                user_answer = False
            else:
                print("Некорректный ответ. Введите True или False.")
                continue

            is_correct = self.check_answer(question_id, user_answer)
            if is_correct:
                print("Правильный ответ!\n")
            else:
                print("Неправильный ответ!\n")

        print("Тест завершен.")

    def get_all_question(self, test_id):
        query = sql.SQL(
            "SELECT id, question_name FROM question WHERE test_id = %s")
        self.cursor.execute(query, (test_id,))
        questions = self.cursor.fetchall()
        return questions

    def get_questions_for_test(self, test_id):
        query = sql.SQL("SELECT id, question_name FROM"
                        " question WHERE test_id = %s")
        self.cursor.execute(query, (test_id,))
        questions = self.cursor.fetchall()
        return questions

    def check_answer(self, question_id, user_answer):
        query = sql.SQL("SELECT is_correct_answer FROM answer WHERE"
                        " question_id = %s AND is_correct_answer = %s")
        self.cursor.execute(query, (question_id, str(user_answer).lower()))
        result = self.cursor.fetchone()
        if result:
            return result[0]

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    t = TestikDB()
    # t.insert_test('eshe data')
    # t.update_test('greh', 2)
    # t.insert_question(2, 'info')
    # t.insert_answer(2, 'Test21824', True)
    # t.update_question(1, 'question_name', 'section')
    # t.update_answer(1, 'answer', 'section')
    # t.delete_answer(1)
    # t.delete_question(1)
    # t.delete_test(1)
    t.select_data()
    t.close()
