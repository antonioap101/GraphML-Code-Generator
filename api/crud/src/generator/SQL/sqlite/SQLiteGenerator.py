from api.crud.src.generator.SQL.SQL_generator import SQLGenerator
from api.crud.src.parsing.components.field_model import FieldModel
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.types.factory.type_mapper_factory import TypeMapperFactory
from api.crud.src.parsing.constants.types.type_mapper import TypeEnum


class SQLiteGenerator(SQLGenerator):
    def __init__(self, table: TableModel):
        super().__init__(table, AllowedDBMS.sqlite)

    def generate_create_table(self) -> str:
        """
        Genera la consulta SQL para crear una tabla en SQLite.
        """
        columns = []
        for field in self.table.fields:
            # Obtener el tipo específico para SQLite
            sqlite_type = TypeMapperFactory.get_dbms_mapper(AllowedDBMS.sqlite).get_mapping(field.type)
            if "{length}" in sqlite_type and hasattr(field, "length"):
                sqlite_type = sqlite_type.format(length=field.length)

            # Construir la definición de columna
            column_def = f"{field.name} {sqlite_type}"
            if not field.nullable:
                column_def += " NOT NULL"
            if field.autoIncrement and field.primaryKey:
                # SQLite usa AUTOINCREMENT solo en combinación con INTEGER PRIMARY KEY
                column_def = f"{field.name} INTEGER PRIMARY KEY AUTOINCREMENT"
            elif field.primaryKey:
                column_def += " PRIMARY KEY"
            if field.unique:
                column_def += " UNIQUE"

            columns.append(column_def)

        # Combinar columnas en la consulta CREATE TABLE
        return f"CREATE TABLE {self.table.name} (\n  " + ",\n  ".join(columns) + "\n);"

    def generate_insert(self) -> str:
        """
        Genera la consulta SQL para insertar un registro en la tabla en SQLite.
        """
        columns = ", ".join(field.name for field in self.table.fields if not field.autoIncrement)
        placeholders = ", ".join("?" for field in self.table.fields if not field.autoIncrement)
        return f"INSERT INTO {self.table.name} ({columns}) VALUES ({placeholders});"

    def generate_select(self) -> str:
        """
        Genera la consulta SQL para leer un registro en la tabla en SQLite.
        """
        return f"SELECT * FROM {self.table.name} WHERE id = ?;"

    def generate_update(self) -> str:
        """
        Genera la consulta SQL para actualizar un registro en la tabla en SQLite.
        """
        set_clause = ", ".join(
            f"{field.name} = ?"
            for field in self.table.fields
            if not field.primaryKey
        )
        return f"UPDATE {self.table.name} SET {set_clause} WHERE id = ?;"

    def generate_delete(self) -> str:
        """
        Genera la consulta SQL para eliminar un registro en la tabla en SQLite.
        """
        return f"DELETE FROM {self.table.name} WHERE id = ?;"


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

    sqlite_generator = SQLiteGenerator(table)
    print(sqlite_generator.generate_create_table())
    print(sqlite_generator.generate_insert())
    print(sqlite_generator.generate_select())
    print(sqlite_generator.generate_update())
    print(sqlite_generator.generate_delete())
