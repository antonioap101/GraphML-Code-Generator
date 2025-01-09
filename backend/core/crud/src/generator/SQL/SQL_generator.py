from typing import Dict
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.constants.types.type_mapper import TypeMapper


class SQLGenerator:
    """
    Generador de consultas SQL para distintos DBMS, con configuración centralizada.
    """

    _dbms_config: Dict[AllowedDBMS, Dict] = {
        AllowedDBMS.mysql: {
            "placeholder": "%s",
            "auto_increment_keyword": "AUTO_INCREMENT",
            "type_mapper": TypeMapper.fromDBMS(AllowedDBMS.mysql),
        },
        AllowedDBMS.postgresql: {
            "placeholder": "%s",
            "auto_increment_keyword": "SERIAL",
            "type_mapper": TypeMapper.fromDBMS(AllowedDBMS.postgresql),
        },
        AllowedDBMS.sqlite: {
            "placeholder": "?",
            "auto_increment_keyword": "AUTOINCREMENT",
            "type_mapper": TypeMapper.fromDBMS(AllowedDBMS.sqlite),
        },
        AllowedDBMS.oracle: {
            "placeholder": ":{}",
            "auto_increment_keyword": None,  # Oracle no usa AUTO_INCREMENT
            "type_mapper": TypeMapper.fromDBMS(AllowedDBMS.oracle),
        },
    }

    def __init__(self, table: TableModel, dbms: AllowedDBMS):
        self.table = table
        self.dbms = dbms
        self.config = self._dbms_config[dbms]
        self.type_mapper = self.config["type_mapper"]

    @classmethod
    def fromDBMS(cls, dbms: AllowedDBMS, table: TableModel) -> "SQLGenerator":
        if dbms not in cls._dbms_config:
            raise ValueError(f"DBMS no soportado: {dbms}")
        return cls(table, dbms)

    def generate_create_table(self) -> str:
        """
        Genera la consulta CREATE TABLE para el DBMS actual.
        """
        columns = []
        for field in self.table.fields:
            dbms_type = self.type_mapper.map(field.type)
            if "{length}" in dbms_type and hasattr(field, "length"):
                dbms_type = dbms_type.format(length=field.length)

            column_def = f"{field.name} {dbms_type}"
            if not field.nullable:
                column_def += " NOT NULL"
            if field.autoIncrement:
                if self.config["auto_increment_keyword"]:
                    column_def += f" {self.config['auto_increment_keyword']}"
            if field.primaryKey:
                column_def += " PRIMARY KEY"
            if field.unique:
                column_def += " UNIQUE"

            columns.append(column_def)

        return f"CREATE TABLE {self.table.name} (\n  " + ",\n  ".join(columns) + "\n);"

    def generate_insert(self) -> str:
        """
        Genera la consulta INSERT para el DBMS actual.
        """
        columns = ", ".join(field.name for field in self.table.fields if not field.autoIncrement)
        placeholders = ", ".join(
            self.config["placeholder"].format(i + 1) for i, field in enumerate(self.table.fields) if not field.autoIncrement
        )
        return f"INSERT INTO {self.table.name} ({columns}) VALUES ({placeholders});"

    def generate_select(self) -> str:
        """
        Genera la consulta SELECT para el DBMS actual.
        """
        return f"SELECT * FROM {self.table.name} WHERE id = {self.config['placeholder'].format(1)};"

    def generate_update(self) -> str:
        """
        Genera la consulta UPDATE para el DBMS actual.
        """
        set_clause = ", ".join(
            f"{field.name} = {self.config['placeholder'].format(i + 1)}"
            for i, field in enumerate(self.table.fields)
            if not field.primaryKey
        )
        return f"UPDATE {self.table.name} SET {set_clause} WHERE id = {self.config['placeholder'].format(len(self.table.fields))};"

    def generate_delete(self) -> str:
        """
        Genera la consulta DELETE para el DBMS actual.
        """
        return f"DELETE FROM {self.table.name} WHERE id = {self.config['placeholder'].format(1)};"


# Ejenmplo de uso
if __name__ == "__main__":
    table = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="username", type=TypeEnum.TEXT, nullable=False, unique=True),
            FieldModel(name="email", type=TypeEnum.TEXT, nullable=False),
        ],
    )

    mysql_generator = SQLGenerator.fromDBMS(AllowedDBMS.mysql, table)
    print(mysql_generator.generate_create_table())
    print(mysql_generator.generate_insert())
    print(mysql_generator.generate_select())
    print(mysql_generator.generate_update())
    print(mysql_generator.generate_delete())

    postgres_generator = SQLGenerator.fromDBMS(AllowedDBMS.postgresql, table)
    print(postgres_generator.generate_create_table())
    print(postgres_generator.generate_insert())
    print(postgres_generator.generate_select())
    print(postgres_generator.generate_update())
    print(postgres_generator.generate_delete())

    sqlite_generator = SQLGenerator.fromDBMS(AllowedDBMS.sqlite, table)
    print(sqlite_generator.generate_create_table())
    print(sqlite_generator.generate_insert())
    print(sqlite_generator.generate_select())
    print(sqlite_generator.generate_update())
    print(sqlite_generator.generate_delete())

    oracle_generator = SQLGenerator.fromDBMS(AllowedDBMS.oracle, table)
    print(oracle_generator.generate_create_table())
    print(oracle_generator.generate_insert())
    print(oracle_generator.generate_select())
    print(oracle_generator.generate_update())
    print(oracle_generator.generate_delete())
