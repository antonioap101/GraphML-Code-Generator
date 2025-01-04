from api.crud.src.generator.SQL.mysql.MySQLGenerator import MySQLGenerator
from api.crud.src.generator.SQL.postgres.PostgreSQLGenerator import PostgreSQLGenerator
from api.crud.src.parsing.components.TableModel import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class SQLGeneratorFactory:

    @staticmethod
    def get(dbms: AllowedDBMS, table: TableModel):
        if dbms == AllowedDBMS.mysql:
            return MySQLGenerator(table)
        elif dbms == AllowedDBMS.postgresql:
            return PostgreSQLGenerator(table)
        else:
            raise ValueError("Invalid DBMS")

    @staticmethod
    def get_mysql_generator(table: TableModel) -> MySQLGenerator:
        return MySQLGenerator(table)

    @staticmethod
    def get_postgresql_generator(schema) -> PostgreSQLGenerator:
        return PostgreSQLGenerator(schema)
