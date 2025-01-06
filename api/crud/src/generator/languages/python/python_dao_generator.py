from api.crud.src.generator.languages.dao_generator import DaoGenerator
from api.crud.src.parsing.components.field_model import FieldModel
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class PythonDaoGenerator(DaoGenerator):
    """
    Generates Python DAO code for CRUD operations.
    """
    TEMPLATE = """
class {TableName}DAO:

    @staticmethod
    def create({columns}):
        query = \"\"\"INSERT INTO {table_name} ({columns}) VALUES ({placeholders}) RETURNING id;\"\"\"
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, ({values}))
                conn.commit()
                return cursor.fetchone()[0]

    @staticmethod
    def read(id):
        query = \"\"\"SELECT * FROM {table_name} WHERE id = %s;\"\"\"
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id,))
                return cursor.fetchone()

    @staticmethod
    def update(id, {update_columns}):
        query = \"\"\"UPDATE {table_name} SET {update_set_clause} WHERE id = %s;\"\"\"
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id, {update_values}))
                conn.commit()

    @staticmethod
    def delete(id):
        query = \"\"\"DELETE FROM {table_name} WHERE id = %s;\"\"\"
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id,))
                conn.commit()
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel) -> str:
        columns = [field.name for field in table_model.fields if not field.autoIncrement]
        placeholders = ["%s"] * len(columns)
        update_columns = [f"{field.name}=%s" for field in table_model.fields if not field.primaryKey]

        dao_code = PythonDaoGenerator.TEMPLATE.format(
            TableName=table_model.name.capitalize(),
            table_name=table_model.name,
            columns=", ".join(columns),
            placeholders=", ".join(placeholders),
            values=", ".join(columns),
            update_columns=", ".join(update_columns),
            update_set_clause=", ".join(update_columns),
            update_values=", ".join(columns),
        )

        return dao_code


# Example usage
if __name__ == "__main__":
    table = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type="number", primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="name", type="string", nullable=False, unique=False),
            FieldModel(name="email", type="string", nullable=False, unique=True),
            FieldModel(name="age", type="number", nullable=True)
        ]
    )

    python_dao_code = PythonDaoGenerator.generate(
        dbms=AllowedDBMS.postgresql,
        table_model=table
    )

    print(python_dao_code)
