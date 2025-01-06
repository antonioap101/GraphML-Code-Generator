from api.crud.src.generator.SQL.SQL_generator_factory import SQLGeneratorFactory
from api.crud.src.generator.languages.connection_generator import ConnectionGenerator
from api.crud.src.parsing.components.connection_parameters import ConnectionParameters
from api.crud.src.parsing.components.field_model import FieldModel
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class PythonConnectionGenerator(ConnectionGenerator):
    """
    Generates the Python code for handling database connections and table creation.
    """
    TEMPLATE = """
import psycopg2
from psycopg2 import sql
from contextlib import contextmanager

DB_CONFIG = {{
    'host': '{dbHost}',
    'port': {dbPort},
    'database': '{dbName}',
    'user': '{dbUser}',
    'password': '{dbPassword}'
}}

@contextmanager
def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()

def ensure_table_exists():
    create_table_query = \"\"\"{CreateTableQuery}\"\"\"
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
            conn.commit()
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel, connection_params: ConnectionParameters) -> str:
        sql_generator = SQLGeneratorFactory.get(dbms, table_model)
        create_table_query = sql_generator.generate_create_table()

        python_code = PythonConnectionGenerator.TEMPLATE.format(
            dbHost=connection_params.host,
            dbPort=connection_params.port,
            dbName=connection_params.database_name,
            dbUser=connection_params.username,
            dbPassword=connection_params.password,
            CreateTableQuery=create_table_query,
        )

        return python_code


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

    connection_params = ConnectionParameters(
        host="localhost",
        port=5432,
        database_name="example_db",
        username="user",
        password="password"
    )

    python_connection_code = PythonConnectionGenerator.generate(
        dbms=AllowedDBMS.postgresql,
        table_model=table,
        connection_params=connection_params
    )

    print(python_connection_code)
