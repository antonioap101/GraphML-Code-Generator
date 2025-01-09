from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.languages.connection.connection_generator import ConnectionGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class CSharpConnectionGenerator(ConnectionGenerator):
    """
    Code generator for handling database connections and table creation in C#.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel, connection_params: ConnectionParameters) -> str:
        """
        Generates the code to handle database connections and table creation in C#.
        """
        # Get the CREATE TABLE query from the SQL generator
        sql_generator = SQLGenerator.fromDBMS(dbms, table_model)
        create_table_query = sql_generator.generate_create_table()

        template = TemplateLoader.forLanguage(AllowedLanguages.csharp).getConnection()

        # Fill the template with the generated values
        csharp_code = template.format(
            dbHost=connection_params.host,
            dbName=connection_params.database_name,
            dbUser=connection_params.username,
            dbPassword=connection_params.password,
            CreateTableQuery=create_table_query
        )

        return csharp_code


if __name__ == "__main__":
    table = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="name", type=TypeEnum.TEXT, nullable=False, unique=False),
            FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
            FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True)
        ]
    )

    csharp_code = CSharpConnectionGenerator.generate(
        dbms=AllowedDBMS.sqlite,
        table_model=table,
        connection_params=ConnectionParameters(
            host="localhost",
            port=1433,
            database_name="my_database",
            username="sa",
            password="password"
        )
    )
    print(csharp_code)
