from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.constants.types.type_mapper import TypeMapper
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader, TemplateType


class SQLGenerator:
    """
    Generador de consultas SQL para distintos DBMS, con configuración centralizada.
    """

    def __init__(self, table: TableModel, dbms: AllowedDBMS):
        self.table = table
        self.dbms = dbms
        self.template_loader = TemplateLoader.forDBMS(dbms)
        self.placeholder = self.template_loader.getPlaceholder()
        self.auto_increment_keyword = self.template_loader.getAutoIncrementKeyword()
        self.type_mapper = TypeMapper.fromDBMS(dbms)

    @classmethod
    def fromDBMS(cls, dbms: AllowedDBMS, table: TableModel) -> "SQLGenerator":
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
            if field.autoIncrement and self.auto_increment_keyword:
                column_def += f" {self.auto_increment_keyword}"
            if not field.nullable:
                column_def += " NOT NULL"
            if field.primaryKey:
                column_def += " PRIMARY KEY"
            if field.unique:
                column_def += " UNIQUE"

            columns.append(column_def)

        columns_str = ", ".join(columns)
        template = self.template_loader.getSQLTemplate(TemplateType.SQL.CREATE_TABLE)
        return template.format(table_name=self.table.name, columns=columns_str)

    def generate_insert(self) -> str:
        """
        Genera la consulta INSERT para el DBMS actual.
        """
        columns = ", ".join(field.name for field in self.table.fields if not field.autoIncrement)
        placeholders = ", ".join(self.placeholder for field in self.table.fields if not field.autoIncrement)
        template = self.template_loader.getSQLTemplate(TemplateType.SQL.INSERT)
        return template.format(table_name=self.table.name, columns=columns, placeholders=placeholders)

    def generate_select(self) -> str:
        """
        Genera la consulta SELECT para el DBMS actual.
        """
        pkeys = [field.name for field in self.table.fields if field.primaryKey]
        template = self.template_loader.getSQLTemplate(TemplateType.SQL.SELECT)
        return template.format(table_name=self.table.name, condition=f"id = {self.placeholder}", primary_key_placeholder=pkeys[0])

    def generate_update(self) -> str:
        """
        Genera la consulta UPDATE para el DBMS actual.
        """
        pkeys = [field.name for field in self.table.fields if field.primaryKey]
        set_clause = ", ".join(
            f"{field.name} = {self.placeholder}"
            for field in self.table.fields
            if not field.primaryKey
        )
        template = self.template_loader.getSQLTemplate(TemplateType.SQL.UPDATE)
        return template.format(table_name=self.table.name, set_clause=set_clause, primary_key_placeholder=pkeys[0])

    def generate_delete(self) -> str:
        """
        Genera la consulta DELETE para el DBMS actual.
        """
        pkeys = [field.name for field in self.table.fields if field.primaryKey]
        template = self.template_loader.getSQLTemplate(TemplateType.SQL.DELETE)
        return template.format(table_name=self.table.name, primary_key_placeholder=pkeys[0])


# Ejemplo de uso
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
