import unittest

from backend.core.crud.src.generator.SQL import PostgreSQLGenerator
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum


class TestPostgreSQLGenerator(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        self.table = TableModel(
            name="users",
            fields=[
                FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
                FieldModel(name="name", type=TypeEnum.TEXT, nullable=False, unique=False),
                FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
                FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True)
            ]
        )
        self.generator = PostgreSQLGenerator(self.table)

    def test_generate_create_table(self):
        """
        Prueba para validar la consulta CREATE TABLE.
        """
        expected_query = (
            "CREATE TABLE users (\n"
            "  id SERIAL PRIMARY KEY,\n"
            "  name CHARACTER VARYING({length}) NOT NULL,\n"
            "  email CHARACTER VARYING({length}) NOT NULL UNIQUE,\n"
            "  age INTEGER\n"
            ");"
        )
        self.assertEqual(self.generator.generate_create_table(), expected_query)

    def test_generate_insert(self):
        """
        Prueba para validar la consulta INSERT.
        """
        expected_query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s);"
        self.assertEqual(self.generator.generate_insert(), expected_query)

    def test_generate_select(self):
        """
        Prueba para validar la consulta SELECT.
        """
        expected_query = "SELECT * FROM users WHERE id = %s;"
        self.assertEqual(self.generator.generate_select(), expected_query)

    def test_generate_update(self):
        """
        Prueba para validar la consulta UPDATE.
        """
        expected_query = "UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s;"
        self.assertEqual(self.generator.generate_update(), expected_query)

    def test_generate_delete(self):
        """
        Prueba para validar la consulta DELETE.
        """
        expected_query = "DELETE FROM users WHERE id = %s;"
        self.assertEqual(self.generator.generate_delete(), expected_query)


if __name__ == "__main__":
    unittest.main()
