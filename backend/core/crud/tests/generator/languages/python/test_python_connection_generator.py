import unittest

from backend.core.crud.src.generator.languages.python.python_connection_generator import PythonConnectionGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel


class TestPythonConnectionGenerator(unittest.TestCase):

    def setUp(self):
        self.table = TableModel(
            name="users",
            fields=[
                FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
                FieldModel(name="name", type=TypeEnum.TEXT, nullable=False, unique=False),
                FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
                FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True),
            ],
        )

        self.connection_params_postgres = ConnectionParameters(
            host="localhost",
            port=5432,
            database_name="test_db",
            username="test_user",
            password="test_password",
        )

        self.connection_params_mysql = ConnectionParameters(
            host="localhost",
            port=3306,
            database_name="test_db",
            username="test_user",
            password="test_password",
        )

    def test_generate_postgres_connection(self):
        code = PythonConnectionGenerator.generate(
            dbms=AllowedDBMS.postgresql,
            table_model=self.table,
            connection_params=self.connection_params_postgres
        )

        self.assertIn("postgresql", code)
        self.assertIn("psycopg2", code)
        self.assertIn("CREATE TABLE IF NOT EXISTS users", code)
        self.assertIn("id SERIAL NOT NULL PRIMARY KEY", code)
        self.assertIn("name VARCHAR(250) NOT NULL", code)
        self.assertIn("email VARCHAR(250) NOT NULL UNIQUE", code)

    def test_generate_mysql_connection(self):
        code = PythonConnectionGenerator.generate(
            dbms=AllowedDBMS.mysql,
            table_model=self.table,
            connection_params=self.connection_params_mysql
        )

        self.assertIn("mysql", code)
        self.assertIn("pymysql", code)
        self.assertIn("CREATE TABLE IF NOT EXISTS users", code)
        self.assertIn("id INT NOT NULL PRIMARY KEY AUTO_INCREMENT", code)
        self.assertIn("name VARCHAR(250) NOT NULL", code)
        self.assertIn("email VARCHAR(250) NOT NULL UNIQUE", code)

    def test_unsupported_dbms(self):
        with self.assertRaises(ValueError) as context:
            PythonConnectionGenerator.generate(
                dbms="unsupported_dbms",  # Invalid DBMS
                table_model=self.table,
                connection_params=self.connection_params_postgres
            )
        self.assertIn("Unsupported DBMS", str(context.exception))


if __name__ == "__main__":
    unittest.main()
