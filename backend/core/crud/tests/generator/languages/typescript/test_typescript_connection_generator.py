import unittest

from backend.core.crud.src.generator.languages.typescript.typescript_connection_generator import TypeScriptConnectionGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel


class TestTypeScriptConnectionGenerator(unittest.TestCase):

    def setUp(self):
        self.table = TableModel(
            name="users",
            fields=[
                FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
                FieldModel(name="name", type=TypeEnum.TEXT, nullable=False, unique=False),
                FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
                FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True)
            ]
        )
        self.connection_params_mysql = ConnectionParameters(
            host="localhost",
            port=3306,
            database_name="test_db",
            username="root",
            password="password"
        )
        self.connection_params_postgres = ConnectionParameters(
            host="localhost",
            port=5432,
            database_name="test_db",
            username="postgres",
            password="password"
        )

    def test_generate_mysql_connection(self):
        ts_code = TypeScriptConnectionGenerator.generate(
            dbms=AllowedDBMS.mysql,
            table_model=self.table,
            connection_params=self.connection_params_mysql
        )
        self.assertIn("mysql", ts_code)
        self.assertIn("3306", ts_code)
        self.assertIn("test_db", ts_code)
        self.assertIn("root", ts_code)
        self.assertIn("password", ts_code)
        self.assertIn("CREATE TABLE IF NOT EXISTS users", ts_code)

    def test_generate_postgresql_connection(self):
        ts_code = TypeScriptConnectionGenerator.generate(
            dbms=AllowedDBMS.postgresql,
            table_model=self.table,
            connection_params=self.connection_params_postgres
        )
        self.assertIn("postgresql", ts_code)
        self.assertIn("5432", ts_code)
        self.assertIn("test_db", ts_code)
        self.assertIn("postgres", ts_code)
        self.assertIn("password", ts_code)
        self.assertIn("CREATE TABLE IF NOT EXISTS users", ts_code)

    def test_generate_sqlite_connection(self):
        ts_code = TypeScriptConnectionGenerator.generate(
            dbms=AllowedDBMS.sqlite,
            table_model=self.table,
            connection_params=self.connection_params_mysql
        )
        self.assertIn("sqlite", ts_code)
        self.assertIn("test_db", ts_code)
        self.assertIn("CREATE TABLE IF NOT EXISTS users", ts_code)

    def test_invalid_dbms(self):
        with self.assertRaises(AttributeError):
            TypeScriptConnectionGenerator.generate(
                dbms="unsupported_dbms",
                table_model=self.table,
                connection_params=self.connection_params_mysql
            )


if __name__ == "__main__":
    unittest.main()
