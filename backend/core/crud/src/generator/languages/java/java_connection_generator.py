from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.connection.connection_generator import ConnectionGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class JavaConnectionGenerator(ConnectionGenerator):
    """
    Generador de código para manejar la conexión a la base de datos y la creación de tablas.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel, connection_params: ConnectionParameters) -> str:
        """
        Genera el código para manejar la conexión a la base de datos y la creación de tablas.
        """
        # Obtener la consulta CREATE TABLE del generador SQL
        sql_generator = SQLGenerator.fromDBMS(dbms, table_model)
        create_table_query = sql_generator.generate_create_table()

        # Rellenar la plantilla
        java_code = TemplateLoader.forLanguage(AllowedLanguages.java).getConnection().format(
            dbUrl=JavaConnectionGenerator.generate_db_url(dbms, connection_params),
            dbUser=connection_params.username,
            dbPassword=connection_params.password,
            CreateTableQuery=create_table_query
        )

        return java_code


if __name__ == '__main__':
    table = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="name", type=TypeEnum.TEXT, nullable=False, unique=False),
            FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
            FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True)
        ]
    )

    java_code = JavaConnectionGenerator.generate(
        dbms=AllowedDBMS.mysql,
        table_model=table,
        connection_params=ConnectionParameters(
            host="localhost",
            port=3306,
            database_name="my_database",
            username="root",
            password="root"
        )
    )
    print(java_code)
