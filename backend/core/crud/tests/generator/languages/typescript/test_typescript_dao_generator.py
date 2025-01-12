import unittest
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.generator.languages.python.python_dao_generator import PythonDaoGenerator

class TestPythonDaoGenerator(unittest.TestCase):

    def setUp(self):
        self.table = TableModel(
            name="users",
            fields=[
                FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
                FieldModel(name="name", type=TypeEnum.TEXT, nullable=False, unique=False),
                FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
                FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True),
            ]
        )

    def test_generate_postgresql_dao(self):
        generated_code = PythonDaoGenerator.generate(
            dbms=AllowedDBMS.postgresql,
            table_model=self.table
        )
        self.assertIn("class UsersDAO:", generated_code)
        self.assertIn("INSERT INTO users", generated_code)
        self.assertIn("RETURNING *;", generated_code)
        self.assertIn("UPDATE users", generated_code)
        self.assertIn("DELETE FROM users", generated_code)
        self.assertIn("SELECT * FROM users", generated_code)

    def test_generate_mysql_dao(self):
        generated_code = PythonDaoGenerator.generate(
            dbms=AllowedDBMS.mysql,
            table_model=self.table
        )
        self.assertIn("class UsersDAO:", generated_code)
        self.assertIn("INSERT INTO users", generated_code)
        self.assertIn("UPDATE users", generated_code)
        self.assertIn("DELETE FROM users", generated_code)
        self.assertIn("SELECT * FROM users", generated_code)

    def test_generate_sqlite_dao(self):
        generated_code = PythonDaoGenerator.generate(
            dbms=AllowedDBMS.sqlite,
            table_model=self.table
        )
        self.assertIn("class UsersDAO:", generated_code)
        self.assertIn("INSERT INTO users", generated_code)
        self.assertIn("UPDATE users", generated_code)
        self.assertIn("DELETE FROM users", generated_code)
        self.assertIn("SELECT * FROM users", generated_code)

    def test_generate_with_custom_fields(self):
        custom_table = TableModel(
            name="products",
            fields=[
                FieldModel(name="product_id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
                FieldModel(name="product_name", type=TypeEnum.TEXT, nullable=False, unique=False),
                FieldModel(name="price", type=TypeEnum.NUMBER, nullable=False),
            ]
        )
        generated_code = PythonDaoGenerator.generate(
            dbms=AllowedDBMS.postgresql,
            table_model=custom_table
        )
        self.assertIn("class ProductsDAO:", generated_code)
        self.assertIn("INSERT INTO products", generated_code)
        self.assertIn("UPDATE products", generated_code)
        self.assertIn("DELETE FROM products", generated_code)
        self.assertIn("SELECT * FROM products", generated_code)

if __name__ == "__main__":
    unittest.main()