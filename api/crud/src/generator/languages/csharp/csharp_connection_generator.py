from api.crud.src.generator.SQL.SQL_generator_factory import SQLGeneratorFactory
from api.crud.src.generator.languages.connection_generator import ConnectionGenerator
from api.crud.src.parsing.components.connection_parameters import ConnectionParameters
from api.crud.src.parsing.components.field_model import FieldModel
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from api.crud.src.templates.template_loader import TemplateLoader, TemplateType


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
        sql_generator = SQLGeneratorFactory.get(dbms, table_model)
        create_table_query = sql_generator.generate_create_table()

        template = TemplateLoader.load_template(AllowedLanguages.csharp, TemplateType.CONNECTION)

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
            FieldModel(name="id", type="number", primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="name", type="string", nullable=False, unique=False),
            FieldModel(name="email", type="string", nullable=False, unique=True),
            FieldModel(name="age", type="number", nullable=True)
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
