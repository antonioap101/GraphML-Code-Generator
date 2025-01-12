import unittest

from backend.core.crud.src.generator.languages.java.java_connection_generator import JavaConnectionGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel


class TestJavaConnectionGenerator(unittest.TestCase):

    def setUp(self):
        # Define a sample table
        self.table = TableModel(
            name="users",
            fields=[
                FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
                FieldModel(name="name", type=TypeEnum.TEXT, nullable=False, unique=False),
                FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
                FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True)
            ]
        )

        # Define connection parameters
        self.connection_params_mysql = ConnectionParameters(
            host="localhost",
            port=3306,
            database_name="test_db",
            username="root",
            password="password"
        )

        self.connection_params_postgresql = ConnectionParameters(
            host="localhost",
            port=5432,
            database_name="test_db",
            username="postgres",
            password="password"
        )

    def test_generate_mysql_connection(self):
        code = JavaConnectionGenerator.generate(
            dbms=AllowedDBMS.mysql,
            table_model=self.table,
            connection_params=self.connection_params_mysql
        )

        self.assertIn("jdbc:mysql://localhost:3306/test_db", code)
        self.assertIn("root", code)
        self.assertIn("CREATE TABLE IF NOT EXISTS users", code)
        self.assertIn("id INT NOT NULL PRIMARY KEY AUTO_INCREMENT", code)

    def test_generate_postgresql_connection(self):
        code = JavaConnectionGenerator.generate(
            dbms=AllowedDBMS.postgresql,
            table_model=self.table,
            connection_params=self.connection_params_postgresql
        )

        self.assertIn("jdbc:postgresql://localhost:5432/test_db", code)
        self.assertIn("postgres", code)
        self.assertIn("CREATE TABLE IF NOT EXISTS users", code)
        self.assertIn("id SERIAL NOT NULL PRIMARY KEY", code)

    def test_invalid_dbms(self):
        with self.assertRaises(AttributeError):
            JavaConnectionGenerator.generate(
                dbms="unsupported_dbms",
                table_model=self.table,
                connection_params=self.connection_params_mysql
            )


if __name__ == "__main__":
    unittest.main()
