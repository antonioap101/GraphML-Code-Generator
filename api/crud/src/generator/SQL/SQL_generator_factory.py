from api.crud.src.generator.SQL.mysql.MySQLGenerator import MySQLGenerator
from api.crud.src.generator.SQL.oracle.OracleGenerator import OracleGenerator
from api.crud.src.generator.SQL.postgres.PostgreSQLGenerator import PostgreSQLGenerator
from api.crud.src.generator.SQL.sqlite.SQLiteGenerator import SQLiteGenerator
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class SQLGeneratorFactory:
    _generators = {
        AllowedDBMS.mysql: MySQLGenerator,
        AllowedDBMS.postgresql: PostgreSQLGenerator,
        AllowedDBMS.sqlite: SQLiteGenerator,
        AllowedDBMS.oracle: OracleGenerator,
    }

    @staticmethod
    def get(dbms: AllowedDBMS, table: TableModel):
        if dbms not in SQLGeneratorFactory._generators:
            raise ValueError("Invalid DBMS: " + dbms)
        return SQLGeneratorFactory._generators[dbms](table)
