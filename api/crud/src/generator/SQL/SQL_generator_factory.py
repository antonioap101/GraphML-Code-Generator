from api.crud.src.generator.SQL.mysql.MySQLGenerator import MySQLGenerator
from api.crud.src.generator.SQL.postgres.PostgreSQLGenerator import PostgreSQLGenerator
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class SQLGeneratorFactory:

    @staticmethod
    def get(dbms: AllowedDBMS, table: TableModel):
        if dbms == AllowedDBMS.mysql:
            return MySQLGenerator(table)
        elif dbms == AllowedDBMS.postgresql:
            return PostgreSQLGenerator(table)
        elif dbms == AllowedDBMS.sqlite:
            raise NotImplementedError("SQLite generator not implemented yet")
        elif dbms == AllowedDBMS.oracle:
            raise NotImplementedError("Oracle generator not implemented yet")
        else:
            raise ValueError("Invalid DBMS: " + dbms)

    @staticmethod
    def get_mysql_generator(table: TableModel) -> MySQLGenerator:
        return MySQLGenerator(table)

    @staticmethod
    def get_postgresql_generator(schema) -> PostgreSQLGenerator:
        return PostgreSQLGenerator(schema)
