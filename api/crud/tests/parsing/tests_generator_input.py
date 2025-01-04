import unittest

from pydantic import ValidationError

from api.crud.src.parsing.CRUDGeneratorInput import CRUDGeneratorInput
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from api.crud.src.parsing.components.FieldModel import FieldModel
from api.crud.src.parsing.components.TableModel import TableModel
from api.crud.src.parsing.constants.types.type_mapper import TypeEnum


class TestGeneratorInput(unittest.TestCase):

    def setUp(self):
        self.empty_table = TableModel(name="test_table", fields=[])
        self.non_empty_table = TableModel(name="test_table2", fields=[FieldModel(name="test_field", type=TypeEnum.TEXT)])

    def test_valid_generator_input(self):
        input_data = CRUDGeneratorInput(
            table=self.empty_table,
            language=AllowedLanguages.typescript,
            dbms=AllowedDBMS.mysql,
            customCode={"key": "value"}
        )
        self.assertEqual(input_data.language, AllowedLanguages.typescript)
        self.assertEqual(input_data.dbms, AllowedDBMS.mysql)
        self.assertEqual(input_data.customCode, {"key": "value"})

        input_data = CRUDGeneratorInput(
            table=self.non_empty_table,
            language=AllowedLanguages.java,
            dbms=AllowedDBMS.sqlite,
            customCode={"key": "value"}
        )
        self.assertEqual(input_data.language, AllowedLanguages.java)
        self.assertEqual(input_data.dbms, AllowedDBMS.sqlite)
        self.assertEqual(input_data.customCode, {"key": "value"})

    def test_invalid_language(self):
        with self.assertRaises(ValidationError):
            CRUDGeneratorInput(
                table=self.empty_table,
                language="invalid_language",
                dbms=AllowedDBMS.mysql
            )

    def test_invalid_dbms(self):
        with self.assertRaises(ValidationError):
            CRUDGeneratorInput(
                table=self.empty_table,
                language=AllowedLanguages.typescript,
                dbms="invalid_dbms"
            )

    def test_optional_custom_code(self):
        input_data = CRUDGeneratorInput(
            table=self.empty_table,
            language=AllowedLanguages.java,
            dbms=AllowedDBMS.postgresql
        )
        self.assertIsNone(input_data.customCode)


if __name__ == "__main__":
    unittest.main()
