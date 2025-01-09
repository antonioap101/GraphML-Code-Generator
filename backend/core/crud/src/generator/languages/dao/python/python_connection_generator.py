from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.languages.connection.connection_generator import ConnectionGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class PythonConnectionGenerator(ConnectionGenerator):
    """
    Generates the Python code for handling database connections and table creation.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel, connection_params: ConnectionParameters) -> str:
        sql_generator = SQLGenerator.fromDBMS(dbms, table_model)
        create_table_query = sql_generator.generate_create_table()

        python_code = TemplateLoader.forLanguage(AllowedLanguages.python).getConnection().format(
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
