from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.connection.connection_generator import ConnectionGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class PythonConnectionGenerator(ConnectionGenerator):
    """
    Generates the Python code for handling database connections and table creation using SQLAlchemy.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel, connection_params: ConnectionParameters) -> str:
        # Map DBMS to dialect and driver for SQLAlchemy
        dialect_driver_map = {
            AllowedDBMS.mysql: ("mysql", "pymysql"),
            AllowedDBMS.postgresql: ("postgresql", "psycopg2"),
            AllowedDBMS.sqlite: ("sqlite", None),
        }
        dialect, driver = dialect_driver_map.get(dbms, (None, None))
        if not dialect:
            raise ValueError(f"Unsupported DBMS: {dbms}")

        sql_generator = SQLGenerator.fromDBMS(dbms, table_model)
        create_table_query = sql_generator.generate_create_table()

        # Load and format the connection template
        python_code = TemplateLoader.forLanguage(AllowedLanguages.python).getConnection().format(
            dbDialect=dialect,
            dbDriver=driver or "",  # SQLite does not require a driver
            dbHost=connection_params.host or "",
            dbPort=connection_params.port or "",
            dbName=connection_params.database_name,
            dbUser=connection_params.username or "",
            dbPassword=connection_params.password or "",
            CreateTableQuery=create_table_query,
        )

        return python_code


# Example usage
if __name__ == "__main__":
    from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
    from backend.core.crud.src.parsing.input_elements.table_model import TableModel
    from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
    from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum

    table = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="name", type=TypeEnum.TEXT, nullable=False, unique=False),
            FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
            FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True)
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
