import unittest

from pydantic import ValidationError

from backend.core.crud.src.parsing.CRUDCodeGeneratorInput import CRUDCodeGeneratorInput
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel


class TestGeneratorInput(unittest.TestCase):

    def setUp(self):
        self.connection_params = ConnectionParameters(
            host="localhost",
            port=5432,
            database_name="test_db",
            username="test_user",
            password="test_password"
        )

        self.empty_table = TableModel(name="test_table", fields=[])
        self.non_empty_table = TableModel(
            name="test_table2",
            fields=[FieldModel(name="test_field", type=TypeEnum.TEXT)]
        )

    def test_valid_generator_input(self):
        input_data = CRUDCodeGeneratorInput(
            table=self.empty_table,
            language=AllowedLanguages.typescript,
            dbms=AllowedDBMS.mysql,
            connectionParams=self.connection_params
        )
        self.assertEqual(input_data.language, AllowedLanguages.typescript)
        self.assertEqual(input_data.dbms, AllowedDBMS.mysql)
        self.assertEqual(input_data.connectionParams.host, "localhost")

        input_data = CRUDCodeGeneratorInput(
            table=self.non_empty_table,
            language=AllowedLanguages.java,
            dbms=AllowedDBMS.sqlite,
            connectionParams=self.connection_params
        )
        self.assertEqual(input_data.language, AllowedLanguages.java)
        self.assertEqual(input_data.dbms, AllowedDBMS.sqlite)
        self.assertEqual(input_data.connectionParams.database_name, "test_db")

    def test_invalid_language(self):
        with self.assertRaises(ValidationError):
            CRUDCodeGeneratorInput(
                table=self.empty_table,
                language="invalid_language",
                dbms=AllowedDBMS.mysql,
                connectionParams=self.connection_params
            )

    def test_invalid_dbms(self):
        with self.assertRaises(ValidationError):
            CRUDCodeGeneratorInput(
                table=self.empty_table,
                language=AllowedLanguages.typescript,
                dbms="invalid_dbms",
                connectionParams=self.connection_params
            )

    def test_invalid_connection_params(self):
        with self.assertRaises(ValidationError):
            ConnectionParameters(
                host="",
                port=5432,
                database_name="test_db",
                username="test_user",
                password="test_password"
            )

        with self.assertRaises(ValidationError):
            ConnectionParameters(
                host="localhost",
                port=70000,  # Invalid port
                database_name="test_db",
                username="test_user",
                password="test_password"
            )

    def test_optional_fields(self):
        minimal_params = ConnectionParameters(
            host="localhost",
            port=5432,
            database_name="test_db"
        )
        input_data = CRUDCodeGeneratorInput(
            table=self.empty_table,
            language=AllowedLanguages.python,
            dbms=AllowedDBMS.postgresql,
            connectionParams=minimal_params
        )
        self.assertEqual(input_data.connectionParams.username, "username")
        self.assertEqual(input_data.connectionParams.password, "password")


if __name__ == "__main__":
    unittest.main()
