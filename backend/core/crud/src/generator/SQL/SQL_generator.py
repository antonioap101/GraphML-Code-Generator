from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
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
        self.placeholder_template = self.template_loader.getPlaceholder()
        self.auto_increment_keyword = self.template_loader.getAutoIncrementKeyword()
        self.type_mapper = TypeMapper.fromDBMS(dbms)

    @classmethod
    def fromDBMS(cls, dbms: AllowedDBMS, table: TableModel) -> "SQLGenerator":
        return cls(table, dbms)

    def generate_create_table(self) -> str:
        """
        Generates the CREATE TABLE query for the current DBMS.
        """
        columns = [self._generate_column_definition(field) for field in self.table.fields]
        columns_str = ", ".join(columns)
        template = self.template_loader.getSQLTemplate(TemplateType.SQL.CREATE_TABLE)
        return template.format(table_name=self.table.name, columns=columns_str)

    def _generate_column_definition(self, field: FieldModel) -> str:
        """
        Generates the SQL definition for a single column based on the DBMS and field attributes.
        """
        dbms_type = self.type_mapper.map(field.type)

        # Handle auto-increment specific syntax for PostgreSQL
        if self.dbms == AllowedDBMS.postgresql and field.autoIncrement:
            dbms_type = self.auto_increment_keyword

        # Build the column definition
        column_def = f"{field.name} {dbms_type}"
        if not field.nullable:
            column_def += " NOT NULL"
        if field.primaryKey:
            column_def += " PRIMARY KEY"
        if field.unique:
            column_def += " UNIQUE"

        # Handle auto-increment for other DBMS
        if self.dbms != AllowedDBMS.postgresql and field.autoIncrement and self.auto_increment_keyword:
            column_def += f" {self.auto_increment_keyword}"

        return column_def

    def __generate_placeholders(self, count: int, exclude_auto_increment: bool, index: int = 1) -> str:
        """
        Genera placeholders para las consultas basados en el DBMS actual.

        Args:
            count (int): Número de placeholders a generar.
            index (int): Índice inicial del placeholder (solo aplica para PostgreSQL).
            exclude_auto_increment (bool): Excluir campos auto-incrementales.

        Returns:
            str: Una cadena con los placeholders generados.
        """
        fields = [field for field in self.table.fields if not exclude_auto_increment or not field.autoIncrement]

        if self.dbms in (AllowedDBMS.sqlite, AllowedDBMS.mysql):
            return ", ".join(self.placeholder_template for _ in fields[:count])
        elif self.dbms == AllowedDBMS.postgresql:
            return ", ".join(self.placeholder_template.format(i=i + index) for i in range(count))
        else:
            raise ValueError(f"Unsupported DBMS: {self.dbms}")

    def generate_insert(self) -> str:
        """
        Genera la consulta INSERT para el DBMS actual.
        """
        columns = ", ".join(field.name for field in self.table.fields if not field.autoIncrement)
        placeholders = self.__generate_placeholders(len([field for field in self.table.fields if not field.autoIncrement]),
                                                    exclude_auto_increment=True)
        template = self.template_loader.getSQLTemplate(TemplateType.SQL.INSERT)
        return template.format(table_name=self.table.name, columns=columns, placeholders=placeholders)

    def generate_select(self) -> str:
        """
        Genera la consulta SELECT para el DBMS actual.
        """
        primary_key_placeholder = self.__generate_placeholders(1, exclude_auto_increment=False)
        template = self.template_loader.getSQLTemplate(TemplateType.SQL.SELECT)
        return template.format(table_name=self.table.name, condition=f"id = {primary_key_placeholder}")

    def generate_update(self) -> str:
        """
        Genera la consulta UPDATE para el DBMS actual.
        """
        primary_key_placeholder = self.__generate_placeholders(1, exclude_auto_increment=False)
        set_clause = ", ".join(
            f"{field.name} = {self.__generate_placeholders(1, exclude_auto_increment=True, index=i+1)}"
            for i, field in enumerate(self.table.fields)
            if not field.primaryKey
        )
        template = self.template_loader.getSQLTemplate(TemplateType.SQL.UPDATE)
        return template.format(table_name=self.table.name, set_clause=set_clause, condition=f"id = {primary_key_placeholder}")

    def generate_delete(self) -> str:
        """
        Genera la consulta DELETE para el DBMS actual.
        """
        primary_key_placeholder = self.__generate_placeholders(1, exclude_auto_increment=False)
        template = self.template_loader.getSQLTemplate(TemplateType.SQL.DELETE)
        return template.format(table_name=self.table.name, condition=f"id = {primary_key_placeholder}")


# Ejemplo de uso
if __name__ == "__main__":
    from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
    from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
    from backend.core.crud.src.parsing.input_elements.table_model import TableModel

    table = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="username", type=TypeEnum.TEXT, nullable=False, unique=True),
            FieldModel(name="email", type=TypeEnum.TEXT, nullable=False),
        ],
    )

    print("...............PostgreSQL...............")
    postgres_generator = SQLGenerator.fromDBMS(AllowedDBMS.postgresql, table)
    print(postgres_generator.generate_create_table())
    print(postgres_generator.generate_insert())
    print(postgres_generator.generate_select())
    print(postgres_generator.generate_update())
    print(postgres_generator.generate_delete())

    print("...............MySQL...............")
    mysql_generator = SQLGenerator.fromDBMS(AllowedDBMS.mysql, table)
    print(mysql_generator.generate_create_table())
    print(mysql_generator.generate_insert())
    print(mysql_generator.generate_select())
    print(mysql_generator.generate_update())
    print(mysql_generator.generate_delete())

    print("...............SQLite...............")
    sqlite_generator = SQLGenerator.fromDBMS(AllowedDBMS.sqlite, table)
    print(sqlite_generator.generate_create_table())
    print(sqlite_generator.generate_insert())
    print(sqlite_generator.generate_select())
    print(sqlite_generator.generate_update())
    print(sqlite_generator.generate_delete())
