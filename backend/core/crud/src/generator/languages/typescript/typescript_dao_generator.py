from backend.core.crud.src.formatting.CodeFormatter import CodeFormatter
from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.dao.dao_generator import DaoGenerator
from backend.core.crud.src.generator.validation.validation_code_generator import ValidationCodeGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class TypeScriptDaoGenerator(DaoGenerator):
    """
    Generador de la implementación Data Access Object (DAO) en TypeScript.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel) -> str:
        """
        Genera el código DAO en TypeScript.
        """
        # Generador de validaciones
        validation_code = ValidationCodeGenerator.fromLanguage(AllowedLanguages.typescript).forFields(table_model.fields)

        # Generador de consultas SQL
        sql_generator = SQLGenerator.fromDBMS(dbms, table_model)

        # Configuración general
        class_name = table_model.name.capitalize()

        # Consultas SQL
        insert_query = sql_generator.generate_insert()
        select_query = sql_generator.generate_select()
        update_query = sql_generator.generate_update()
        delete_query = sql_generator.generate_delete()

        # Parámetros de los métodos
        field_parameters = ", ".join(
            f"{field.name}: {field.type}" for field in table_model.fields if not field.autoIncrement
        )
        insert_values = ", ".join(f"{field.name}" for field in table_model.fields if not field.autoIncrement)
        update_values = ", ".join(f"{field.name}" for field in table_model.fields if not field.primaryKey)

        # Load the DAO template
        dao_template = TemplateLoader.forLanguage(AllowedLanguages.typescript).getDao()

        # Determine the indentation level for ValidationCode
        base_indent = dao_template.split("{ValidationCode}")[0].splitlines()[-1]
        if validation_code and len(validation_code) > 0:
            validation_code = CodeFormatter.format_code_with_indent(validation_code, base_indent)

        # Rellenar plantilla
        ts_code = dao_template.format(
            ClassName=class_name,
            FieldParameters=field_parameters,
            ValidationCode=validation_code,
            InsertQuery=insert_query,
            InsertValues=insert_values,
            SelectQuery=select_query,
            UpdateQuery=update_query,
            UpdateValues=update_values,
            DeleteQuery=delete_query,
        )

        return ts_code


if __name__ == '__main__':
    from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
    from backend.core.crud.src.parsing.input_elements.table_model import TableModel

    table = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="name", type=TypeEnum.TEXT, nullable=False),
            FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
            FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True)
        ]
    )

    ts_code = TypeScriptDaoGenerator.generate(
        dbms=AllowedDBMS.postgresql,
        table_model=table
    )
    print(ts_code)