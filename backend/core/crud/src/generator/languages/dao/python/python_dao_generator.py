from backend.core.crud.src.formatting.CodeFormatter import CodeFormatter
from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.languages.dao.dao_generator import DaoGenerator
from backend.core.crud.src.generator.languages.validation.validation_code_generator import ValidationCodeGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.constants.types.type_mapper import TypeMapper
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class PythonDaoGenerator(DaoGenerator):
    """
    Generador de clases DAO en Python basadas en los metadatos de la tabla y las consultas SQL generadas.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel) -> str:
        """
        Genera el código de una clase DAO en Python basada en los metadatos de la tabla y el DBMS.
        """
        # Generar código de validación
        validation_code = ValidationCodeGenerator.fromLanguage(AllowedLanguages.python).forFields(table_model.fields)

        # Obtener el generador SQL correspondiente al DBMS
        sql_generator = SQLGenerator.fromDBMS(dbms, table_model)

        # Generar consultas SQL
        insert_query = sql_generator.generate_insert()
        select_query = sql_generator.generate_select()
        update_query = sql_generator.generate_update()
        delete_query = sql_generator.generate_delete()

        python_mapper = TypeMapper.fromLanguage(AllowedLanguages.python)

        # Generar FieldParameters y configuración de parámetros
        field_parameters = ", ".join(
            f"{field.name}: {python_mapper.map(field.type)}"
            for field in table_model.fields if not field.autoIncrement
        )
        set_insert_parameters = ", ".join(
            f"{field.name}"
            for field in table_model.fields if not field.autoIncrement
        )
        set_update_parameters = ", ".join(
            f"{field.name}"
            for field in table_model.fields if not field.primaryKey
        )

        # Load the DAO template
        dao_template = TemplateLoader.forLanguage(AllowedLanguages.python).getDao()

        # Determine the indentation level for ValidationCode
        base_indent = dao_template.split("{ValidationCode}")[0].splitlines()[-1]
        if validation_code and len(validation_code) > 0:
            validation_code = CodeFormatter.format_code_with_indent(validation_code, base_indent)

        # Rellenar la plantilla con los valores generados
        python_code = dao_template.format(
            ClassName=table_model.name.capitalize(),
            FieldParameters=field_parameters,
            ValidationCode=validation_code,
            InsertQuery=insert_query,
            SelectQuery=select_query,
            UpdateQuery=update_query,
            DeleteQuery=delete_query,
            SetInsertParameters=set_insert_parameters,
            SetUpdateParameters=set_update_parameters,
        )

        return python_code

