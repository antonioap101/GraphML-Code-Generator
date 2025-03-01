from backend.core.crud.src.formatting.CodeFormatter import CodeFormatter
from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.dao.dao_generator import DaoGenerator
from backend.core.crud.src.generator.validation.validation_code_generator import ValidationCodeGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.constants.types.type_mapper import TypeMapper
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class JavaDaoGenerator(DaoGenerator):
    """
    Generador de clases DAO en Java basadas en los metadatos de la tabla y las consultas SQL generadas.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel) -> str:
        """
        Genera el código de una clase DAO en Java basada en los metadatos de la tabla y el DBMS.
        """

        # Generar código de validación
        validation_code = ValidationCodeGenerator.fromLanguage(AllowedLanguages.java).forFields(table_model.fields)

        # Obtener el generador SQL correspondiente al DBMS
        sql_generator = SQLGenerator.fromDBMS(dbms, table_model)

        # Generar consultas SQL
        insert_query = sql_generator.generate_insert()
        select_query = sql_generator.generate_select()
        update_query = sql_generator.generate_update()
        delete_query = sql_generator.generate_delete()

        java_mapper = TypeMapper.fromLanguage(AllowedLanguages.java)
        # Generar parámetros y configuración de PreparedStatement
        field_parameters = ", ".join(
            f"{java_mapper.map(field.type)} {field.name}"
            for field in table_model.fields if not field.autoIncrement
        )
        set_insert_parameters = "\n                ".join(
            f"statement.set{java_mapper.map(field.type)}({index}, {field.name});"
            for index, field in enumerate(table_model.fields, start=1) if not field.autoIncrement
        )
        set_update_parameters = "\n                ".join(
            f"statement.set{java_mapper.map(field.type)}({index}, {field.name});"
            for index, field in enumerate(table_model.fields, start=1) if not field.primaryKey
        )

        # Load the DAO template
        dao_template = TemplateLoader.forLanguage(AllowedLanguages.java).getDao()

        # Determine the indentation level for ValidationCode
        base_indent = dao_template.split("{ValidationCode}")[0].splitlines()[-1]
        if validation_code and len(validation_code) > 0:
            validation_code = CodeFormatter.format_code_with_indent(validation_code, base_indent)

        # Rellenar la plantilla con los valores generados
        java_code = dao_template.format(
            ClassName=table_model.name.capitalize(),
            FieldParameters=field_parameters,
            ValidationCode=validation_code,
            InsertQuery=insert_query,
            SelectQuery=select_query,
            UpdateQuery=update_query,
            DeleteQuery=delete_query,
            SetInsertParameters=set_insert_parameters,
            SetUpdateParameters=set_update_parameters,
            ParamIndex=len(table_model.fields) + 1  # Índice del ID en la consulta UPDATE
        )

        return java_code


if __name__ == '__main__':
    from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
    from backend.core.crud.src.parsing.input_elements.table_model import TableModel
    from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
    from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum

    table = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="name", type=TypeEnum.TEXT, nullable=False, unique=False),
            FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
            FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True)
        ]
    )

    python_dao_code = JavaDaoGenerator.generate(
        dbms=AllowedDBMS.postgresql,
        table_model=table
    )

    print(python_dao_code)
