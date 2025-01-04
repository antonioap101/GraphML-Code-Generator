from api.crud.src.generator.SQL.SQL_generator import SQLGenerator
from api.crud.src.parsing.components.TableModel import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.types.factory.type_mapper_factory import TypeMapperFactory


class MySQLGenerator(SQLGenerator):
    def __init__(self, table: TableModel):
        super().__init__(table, AllowedDBMS.mysql)

    def generate_create_table(self) -> str:
        """
        Genera la consulta SQL para crear una tabla en MySQL.
        """
        columns = []
        for field in self.table.fields:
            # Obtener el tipo específico para MySQL
            mysql_type = TypeMapperFactory.get_dbms_mapper(AllowedDBMS.mysql).get_mapping(field.type)
            if "{length}" in mysql_type and hasattr(field, "length"):
                mysql_type = mysql_type.format(length=field.length)

            # Construir la definición de columna
            column_def = f"{field.name} {mysql_type}"
            if not field.nullable:
                column_def += " NOT NULL"
            if field.autoIncrement:
                column_def += " AUTO_INCREMENT"
            if field.primaryKey:
                column_def += " PRIMARY KEY"
            if field.unique:
                column_def += " UNIQUE"

            columns.append(column_def)

        # Combinar columnas en la consulta CREATE TABLE
        return f"CREATE TABLE {self.table.name} (\n  " + ",\n  ".join(columns) + "\n);"

    def generate_insert(self) -> str:
        """
        Genera la consulta SQL para insertar un registro en la tabla en MySQL.
        """
        columns = ", ".join(field.name for field in self.table.fields if not field.autoIncrement)
        placeholders = ", ".join("%s" for field in self.table.fields if not field.autoIncrement)
        return f"INSERT INTO {self.table.name} ({columns}) VALUES ({placeholders});"

    def generate_select(self) -> str:
        """
        Genera la consulta SQL para leer un registro en la tabla en MySQL.
        """
        return f"SELECT * FROM {self.table.name} WHERE id = %s;"

    def generate_update(self) -> str:
        """
        Genera la consulta SQL para actualizar un registro en la tabla en MySQL.
        """
        set_clause = ", ".join(
            f"{field.name} = %s"
            for field in self.table.fields
            if not field.primaryKey
        )
        return f"UPDATE {self.table.name} SET {set_clause} WHERE id = %s;"

    def generate_delete(self) -> str:
        """
        Genera la consulta SQL para eliminar un registro en la tabla en MySQL.
        """
        return f"DELETE FROM {self.table.name} WHERE id = %s;"
