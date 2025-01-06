from api.crud.src.generator.SQL.SQL_generator_factory import SQLGeneratorFactory
from api.crud.src.generator.languages.connection_generator import ConnectionGenerator
from api.crud.src.parsing.components.connection_parameters import ConnectionParameters
from api.crud.src.parsing.components.field_model import FieldModel
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class JavaConnectionGenerator(ConnectionGenerator):
    """
    Generador de código para manejar la conexión a la base de datos y la creación de tablas.
    """

    # Plantilla base para la clase de conexión
    TEMPLATE = """
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class DatabaseConnection {{
    private static final String URL = "{dbUrl}";
    private static final String USER = "{dbUser}";
    private static final String PASSWORD = "{dbPassword}";

    public static Connection getConnection() throws SQLException {{
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }}

    public static void ensureTableExists() {{
        String createTableQuery = "{CreateTableQuery}";
        try (Connection connection = getConnection();
             Statement statement = connection.createStatement()) {{
             statement.execute(createTableQuery);
        }} catch (SQLException e) {{
            e.printStackTrace();
            throw new RuntimeException("Error ensuring table exists", e);
        }}
    }}
}}
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel, connection_params: ConnectionParameters) -> str:
        """
        Genera el código para manejar la conexión a la base de datos y la creación de tablas.
        """
        # Obtener la consulta CREATE TABLE del generador SQL
        sql_generator = SQLGeneratorFactory.get(dbms, table_model)
        create_table_query = sql_generator.generate_create_table()

        # Rellenar la plantilla
        java_code = JavaConnectionGenerator.TEMPLATE.format(
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
            FieldModel(name="id", type="number", primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="name", type="string", nullable=False, unique=False),
            FieldModel(name="email", type="string", nullable=False, unique=True),
            FieldModel(name="age", type="number", nullable=True)
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
