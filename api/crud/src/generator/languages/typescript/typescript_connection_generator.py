from api.crud.src.generator.SQL.SQL_generator_factory import SQLGeneratorFactory
from api.crud.src.generator.languages.connection_generator import ConnectionGenerator
from api.crud.src.parsing.components.connection_parameters import ConnectionParameters
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class TypeScriptConnectionGenerator(ConnectionGenerator):
    """
    Generates the code for handling database connections and ensuring table creation in TypeScript.
    """

    TEMPLATE = """
import {{ Pool, PoolClient }} from 'pg';

const pool = new Pool({{
  host: '{dbHost}',
  port: {dbPort},
  database: '{dbName}',
  user: '{dbUser}',
  password: '{dbPassword}',
}});

export async function getConnection(): Promise<PoolClient> {{
  return await pool.connect();
}}

export async function ensureTableExists(): Promise<void> {{
  const createTableQuery = `{CreateTableQuery}`;
  const client = await getConnection();
  try {{
    await client.query(createTableQuery);
  }} catch (error) {{
    console.error('Error ensuring table exists:', error);
    throw error;
  }} finally {{
    client.release();
  }}
}}
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel, connection_params: ConnectionParameters) -> str:
        """
        Generates the TypeScript code for database connection and table creation.
        """
        # Generate SQL query using the appropriate SQL generator
        sql_generator = SQLGeneratorFactory.get(dbms, table_model)
        create_table_query = sql_generator.generate_create_table()

        # Format the TypeScript code using the provided parameters
        ts_code = TypeScriptConnectionGenerator.TEMPLATE.format(
            dbHost=connection_params.host,
            dbPort=connection_params.port,
            dbName=connection_params.database_name,
            dbUser=connection_params.username,
            dbPassword=connection_params.password,
            CreateTableQuery=create_table_query,
        )

        return ts_code
