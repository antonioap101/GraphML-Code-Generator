import unittest

from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel


class TestSQLGenerator(unittest.TestCase):

    def setUp(self):
        self.table = TableModel(
            name="users",
            fields=[
                FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
                FieldModel(name="username", type=TypeEnum.TEXT, nullable=False, unique=True),
                FieldModel(name="email", type=TypeEnum.TEXT, nullable=False),
            ],
        )

    def test_mysql_create_table(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.mysql, self.table)
        expected_query = (
            "CREATE TABLE IF NOT EXISTS users ("
            "id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, "
            "username VARCHAR(250) NOT NULL UNIQUE, "
            "email VARCHAR(250) NOT NULL);"
        )
        self.assertEqual(generator.generate_create_table(), expected_query)

    def test_postgresql_create_table(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.postgresql, self.table)
        expected_query = (
            "CREATE TABLE IF NOT EXISTS users ("
            "id SERIAL NOT NULL PRIMARY KEY, "
            "username VARCHAR(250) NOT NULL UNIQUE, "
            "email VARCHAR(250) NOT NULL);"
        )
        self.assertEqual(generator.generate_create_table(), expected_query)

    def test_sqlite_create_table(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.sqlite, self.table)
        expected_query = (
            "CREATE TABLE IF NOT EXISTS users ("
            "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
            "username TEXT NOT NULL UNIQUE, "
            "email TEXT NOT NULL);"
        )
        self.assertEqual(generator.generate_create_table(), expected_query)

    def test_mysql_insert(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.mysql, self.table)
        expected_query = "INSERT INTO users (username, email) VALUES (?, ?);"
        self.assertEqual(generator.generate_insert(), expected_query)

    def test_postgresql_insert(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.postgresql, self.table)
        expected_query = "INSERT INTO users (username, email) VALUES ($1, $2) RETURNING *;"
        self.assertEqual(generator.generate_insert(), expected_query)

    def test_sqlite_insert(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.sqlite, self.table)
        expected_query = "INSERT INTO users (username, email) VALUES (?, ?);"
        self.assertEqual(generator.generate_insert(), expected_query)

    def test_mysql_select(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.mysql, self.table)
        expected_query = "SELECT * FROM users WHERE id = ?;"
        self.assertEqual(generator.generate_select(), expected_query)

    def test_postgresql_select(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.postgresql, self.table)
        expected_query = "SELECT * FROM users WHERE id = $1;"
        self.assertEqual(generator.generate_select(), expected_query)

    def test_sqlite_select(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.sqlite, self.table)
        expected_query = "SELECT * FROM users WHERE id = ?;"
        self.assertEqual(generator.generate_select(), expected_query)

    def test_mysql_update(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.mysql, self.table)
        expected_query = "UPDATE users SET username = ?, email = ? WHERE id = ?;"
        self.assertEqual(generator.generate_update(), expected_query)

    def test_postgresql_update(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.postgresql, self.table)
        expected_query = "UPDATE users SET username = $2, email = $3 WHERE id = $1 RETURNING *;"
        self.assertEqual(generator.generate_update(), expected_query)

    def test_sqlite_update(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.sqlite, self.table)
        expected_query = "UPDATE users SET username = ?, email = ? WHERE id = ?;"
        self.assertEqual(generator.generate_update(), expected_query)

    def test_mysql_delete(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.mysql, self.table)
        expected_query = "DELETE FROM users WHERE id = ?;"
        self.assertEqual(generator.generate_delete(), expected_query)

    def test_postgresql_delete(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.postgresql, self.table)
        expected_query = "DELETE FROM users WHERE id = $1;"
        self.assertEqual(generator.generate_delete(), expected_query)

    def test_sqlite_delete(self):
        generator = SQLGenerator.fromDBMS(AllowedDBMS.sqlite, self.table)
        expected_query = "DELETE FROM users WHERE id = ?;"
        self.assertEqual(generator.generate_delete(), expected_query)


if __name__ == "__main__":
    unittest.main()

