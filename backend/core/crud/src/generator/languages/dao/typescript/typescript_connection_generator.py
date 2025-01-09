from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.languages.connection.connection_generator import ConnectionGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class TypeScriptConnectionGenerator(ConnectionGenerator):
    """
    Generates the code for handling database connections and ensuring table creation in TypeScript.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel, connection_params: ConnectionParameters) -> str:
        """
        Generates the TypeScript code for database connection and table creation.
        """
        # Generate SQL query using the appropriate SQL generator
        sql_generator = SQLGenerator.fromDBMS(dbms, table_model)
        create_table_query = sql_generator.generate_create_table()

        # Format the TypeScript code using the provided parameters
        ts_code = TemplateLoader.forLanguage(AllowedLanguages.typescript).getConnection().format(
            dbHost=connection_params.host,
            dbPort=connection_params.port,
            dbName=connection_params.database_name,
            dbUser=connection_params.username,
            dbPassword=connection_params.password,
            CreateTableQuery=create_table_query,
        )

        return ts_code
