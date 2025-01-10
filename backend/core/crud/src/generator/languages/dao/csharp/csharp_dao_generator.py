from backend.core.crud.src.formatting.CodeFormatter import CodeFormatter
from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.languages.dao.dao_generator import DaoGenerator
from backend.core.crud.src.generator.languages.validation.validation_code_generator import ValidationCodeGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.constants.types.type_mapper import TypeMapper
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class CSharpDaoGenerator(DaoGenerator):
    """
    Generates DAO classes in C# based on table metadata and SQL queries.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel) -> str:
        """
        Generates the DAO class code for C# based on the table metadata and DBMS.
        """
        # Generar código de validación
        validation_code = ValidationCodeGenerator.fromLanguage(AllowedLanguages.csharp).forFields(table_model.fields)

        # Get the SQL generator for the DBMS
        sql_generator = SQLGenerator.fromDBMS(dbms, table_model)

        # Generate SQL queries
        insert_query = sql_generator.generate_insert()
        select_query = sql_generator.generate_select()
        update_query = sql_generator.generate_update()
        delete_query = sql_generator.generate_delete()

        csharp_mapper = TypeMapper.fromLanguage(AllowedLanguages.csharp)

        # Generate field parameters and set statements
        field_parameters = ", ".join(
            f"{csharp_mapper.map(field.type)} {field.name}"
            for field in table_model.fields if not field.autoIncrement
        )
        set_insert_parameters = "\n            ".join(
            f"command.Parameters.AddWithValue(\"@{field.name}\", {field.name});"
            for field in table_model.fields if not field.autoIncrement
        )
        set_update_parameters = "\n            ".join(
            f"command.Parameters.AddWithValue(\"@{field.name}\", {field.name});"
            for field in table_model.fields if not field.primaryKey
        )

        # Load the DAO template
        dao_template = TemplateLoader.forLanguage(AllowedLanguages.csharp).getDao()

        # Determine the indentation level for ValidationCode
        base_indent = dao_template.split("{ValidationCode}")[0].splitlines()[-1]
        if validation_code and len(validation_code) > 0:
            validation_code = CodeFormatter.format_code_with_indent(validation_code, base_indent)

        # Fill the template with the generated values
        csharp_code = dao_template.format(
            ClassName=table_model.name.capitalize(),
            FieldParameters=field_parameters,
            ValidationCode=validation_code,
            InsertQuery=insert_query,
            SelectQuery=select_query,
            UpdateQuery=update_query,
            DeleteQuery=delete_query,
            SetInsertParameters=set_insert_parameters,
            SetUpdateParameters=set_update_parameters
        )

        return csharp_code
