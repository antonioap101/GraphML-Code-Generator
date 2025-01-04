from api.crud.src.generator.SQL.SQL_generator import SQLGenerator
from api.crud.src.parsing.components.FieldModel import FieldModel
from api.crud.src.parsing.components.TableModel import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.types.factory.type_mapper_factory import TypeMapperFactory
from api.crud.src.parsing.constants.types.type_mapper import TypeEnum


class PostgreSQLGenerator(SQLGenerator):
    def __init__(self, table: TableModel):
        super().__init__(table, AllowedDBMS.postgresql)

    def generate_create_table(self) -> str:
        """
        Genera la consulta SQL para crear una tabla en PostgreSQL.
        """
        columns = []
        for field in self.table.fields:
            # Obtener el tipo específico para PostgreSQL
            postgres_type = TypeMapperFactory.get_dbms_mapper(AllowedDBMS.postgresql).get_mapping(field.type)
            if "{length}" in postgres_type and hasattr(field, "length"):
                postgres_type = postgres_type.format(length=field.length)

            # Construir la definición de columna
            column_def = f"{field.name} {postgres_type}"
            if not field.nullable:
                column_def += " NOT NULL"
            if field.autoIncrement:
                if postgres_type == "INTEGER":  # Convertir INTEGER a SERIAL para PostgreSQL
                    column_def = f"{field.name} SERIAL"
            if field.primaryKey:
                column_def += " PRIMARY KEY"
            if field.unique:
                column_def += " UNIQUE"

            columns.append(column_def)

        # Combinar columnas en la consulta CREATE TABLE
        return f"CREATE TABLE {self.table.name} (\n  " + ",\n  ".join(columns) + "\n);"

    def generate_insert(self) -> str:
        """
        Genera la consulta SQL para insertar un registro en la tabla en PostgreSQL.
        """
        columns = ", ".join(field.name for field in self.table.fields if not field.autoIncrement)
        placeholders = ", ".join("%s" for field in self.table.fields if not field.autoIncrement)
        return f"INSERT INTO {self.table.name} ({columns}) VALUES ({placeholders});"

    def generate_select(self) -> str:
        """
        Genera la consulta SQL para leer un registro en la tabla en PostgreSQL.
        """
        return f"SELECT * FROM {self.table.name} WHERE id = %s;"

    def generate_update(self) -> str:
        """
        Genera la consulta SQL para actualizar un registro en la tabla en PostgreSQL.
        """
        set_clause = ", ".join(
            f"{field.name} = %s"
            for field in self.table.fields
            if not field.primaryKey
        )
        return f"UPDATE {self.table.name} SET {set_clause} WHERE id = %s;"

    def generate_delete(self) -> str:
        """
        Genera la consulta SQL para eliminar un registro en la tabla en PostgreSQL.
        """
        return f"DELETE FROM {self.table.name} WHERE id = %s;"


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

    postgres_generator = PostgreSQLGenerator(table)
    print(postgres_generator.generate_create_table())
    print(postgres_generator.generate_insert())
    print(postgres_generator.generate_select())
    print(postgres_generator.generate_update())
    print(postgres_generator.generate_delete())


