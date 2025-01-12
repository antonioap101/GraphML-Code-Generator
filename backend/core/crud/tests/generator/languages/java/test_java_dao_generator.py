import unittest

from backend.core.crud.src.generator.languages.java.java_dao_generator import JavaDaoGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.parsing.input_elements.validations import Validations


class TestJavaDaoGenerator(unittest.TestCase):

    def setUp(self):
        self.table_model = TableModel(
            name="users",
            fields=[
                FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
                FieldModel(name="name", type=TypeEnum.TEXT, nullable=False),
                FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
                FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True),
            ]
        )

    def test_generate_postgresql(self):
        java_code = JavaDaoGenerator.generate(
            dbms=AllowedDBMS.postgresql,
            table_model=self.table_model
        )

        # Check that the code contains PostgreSQL-specific syntax
        self.assertIn("RETURNING *", java_code)
        self.assertIn("$1", java_code)
        self.assertIn("statement.setString", java_code)
        self.assertIn("statement.setInt", java_code)

    def test_generate_mysql(self):
        java_code = JavaDaoGenerator.generate(
            dbms=AllowedDBMS.mysql,
            table_model=self.table_model
        )

        # Check that the code contains MySQL-specific syntax
        self.assertNotIn("RETURNING *", java_code)
        self.assertIn("?", java_code)
        self.assertIn("statement.setString", java_code)
        self.assertIn("statement.setInt", java_code)

    def test_generate_sqlite(self):
        java_code = JavaDaoGenerator.generate(
            dbms=AllowedDBMS.sqlite,
            table_model=self.table_model
        )

        # Check that the code contains SQLite-specific syntax
        self.assertNotIn("RETURNING *", java_code)
        self.assertIn("?", java_code)
        self.assertIn("statement.setString", java_code)
        self.assertIn("statement.setInt", java_code)


    def test_generate_validation_code(self):
        # Add validations to the fields
        self.table_model.fields[1].validations = Validations(
            minLength=3,
            maxLength=50
        )
        self.table_model.fields[2].validations = Validations(
            pattern="^[a-zA-Z0-9_]+$"
        )

        java_code = JavaDaoGenerator.generate(
            dbms=AllowedDBMS.postgresql,
            table_model=self.table_model
        )

        # Check that validation code is included
        self.assertIn("if (name.length() < 3)", java_code)
        self.assertIn("if (name.length() > 50)", java_code)
        self.assertIn("if (!email.matches", java_code)


if __name__ == "__main__":
    unittest.main()
