from api.crud.src.generator.SQL.SQL_generator import SQLGenerator
from api.crud.src.parsing.components.field_model import FieldModel
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.types.factory.type_mapper_factory import TypeMapperFactory
from api.crud.src.parsing.constants.types.type_mapper import TypeEnum


class OracleGenerator(SQLGenerator):
    def __init__(self, table: TableModel):
        super().__init__(table, AllowedDBMS.oracle)

    def generate_create_table(self) -> str:
        """
        Generates the SQL query to create a table in Oracle.
        """
        columns = []
        for field in self.table.fields:
            # Get the specific type for Oracle
            oracle_type = TypeMapperFactory.get_dbms_mapper(AllowedDBMS.oracle).get_mapping(field.type)
            if "{length}" in oracle_type and hasattr(field, "length"):
                oracle_type = oracle_type.format(length=field.length)

            # Build the column definition
            column_def = f"{field.name} {oracle_type}"
            if not field.nullable:
                column_def += " NOT NULL"
            if field.primaryKey:
                column_def += " PRIMARY KEY"
            if field.unique:
                column_def += " UNIQUE"

            columns.append(column_def)

        # Combine columns into the CREATE TABLE query
        return f"CREATE TABLE {self.table.name} (\n  " + ",\n  ".join(columns) + "\n);"

    def generate_insert(self) -> str:
        """
        Generates the SQL query to insert a record into the table in Oracle.
        """
        columns = ", ".join(field.name for field in self.table.fields if not field.autoIncrement)
        placeholders = ", ".join(":" + str(i + 1) for i, field in enumerate(self.table.fields) if not field.autoIncrement)
        return f"INSERT INTO {self.table.name} ({columns}) VALUES ({placeholders});"

    def generate_select(self) -> str:
        """
        Generates the SQL query to read a record from the table in Oracle.
        """
        return f"SELECT * FROM {self.table.name} WHERE id = :1;"

    def generate_update(self) -> str:
        """
        Generates the SQL query to update a record in the table in Oracle.
        """
        set_clause = ", ".join(
            f"{field.name} = :{i + 1}"
            for i, field in enumerate(self.table.fields)
            if not field.primaryKey
        )
        return f"UPDATE {self.table.name} SET {set_clause} WHERE id = :{len(self.table.fields)};"

    def generate_delete(self) -> str:
        """
        Generates the SQL query to delete a record from the table in Oracle.
        """
        return f"DELETE FROM {self.table.name} WHERE id = :1;"


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

    oracle_generator = OracleGenerator(table)
    print(oracle_generator.generate_create_table())
    print(oracle_generator.generate_insert())
    print(oracle_generator.generate_select())
    print(oracle_generator.generate_update())
    print(oracle_generator.generate_delete())
