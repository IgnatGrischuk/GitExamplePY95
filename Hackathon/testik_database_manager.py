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
        self.cursor.execute(query, (name, id, ))

    def insert_question(self, test_id: int, question_name: str):

        query = sql.SQL("insert into Question(test_id, question_name)"
                        " values (%s, %s);")

        self.cursor.execute(query, (test_id, question_name, ))

    def update_question(self, id: int, section_name: str, section_value: str):
        if section_name == "test_id":
            section_value = int(section_value)

        query = sql.SQL(f"update Question set {section_name} = %s "
                        f"where id = %s")

        self.cursor.execute(query, (section_value, id))

    def insert_answer(self, question_id: int,
                      answer: str,
                      is_correct_answer: bool):

        query = sql.SQL("insert into answer(question_id, answer, "
                        "is_correct_answer)"
                        " values (%s, %s, %s);")

        self.cursor.execute(query, (question_id, answer, is_correct_answer))

    def update_answer(self, id, section_name, section_value):

        query = sql.SQL(f"update answer set {section_name} = %s "
                        f"where id = %s")

        self.cursor.execute(query, (section_value, id))

    def delete_test(self, id: int):
        query = sql.SQL("DELETE FROM answer WHERE id = %s;"
                        "DELETE FROM question WHERE id = %s;"
                        "DELETE FROM test WHERE id = %s;")
        self.cursor.execute(query, (id, id, id))

    def delete_answer(self, id: int):
        query = sql.SQL("DELETE FROM answer WHERE id = %s;")
        self.cursor.execute(query, (id, ))

    def delete_question(self, id: int):
        query = sql.SQL("DELETE FROM question WHERE id = %s;"
                        "DELETE FROM answer WHERE id = %s;")
        self.cursor.execute(query, (id, id, ))

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
                        "INNER JOIN question on test.id = question.test_id "
                        "INNER JOIN answer on answer.question_id = "
                        "question.id ")

        self.cursor.execute(query, )
        data = self.cursor.fetchall()
        for i in data:
            print(f"test.id: {i[0]}\n"
                  f"test.name: {i[1]}\n"
                  f"question.id: {i[2]}\n"
                  f"question.test_id: {i[3]}\n"
                  f"question.question_name: {i[4]}\n"
                  f"answer.id: {i[5]}\n"
                  f"answer.question_id: {i[6]}\n"
                  f"answer.answer: {i[7]}\n"
                  f"answer.is_correct_answer: {i[8]}\n\n")

    def close(self):
        self.cursor.close()
        self.conn.close()


t = TestikDB()
# t.insert_test('eshe data')
# t.update_test('greh', 2)
# t.insert_question(2, 'info')
# t.insert_answer(2, 'not cool', False)
# t.update_question(1, 'question_name', 'section')
# t.update_answer(1, 'answer', 'section')
# t.delete_answer(1)
# t.delete_question(1)
# t.delete_test(1)
t.select_data()
t.close()
