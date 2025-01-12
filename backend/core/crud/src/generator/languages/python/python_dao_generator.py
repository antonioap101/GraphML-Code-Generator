from backend.core.crud.src.formatting.CodeFormatter import CodeFormatter
from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.dao.dao_generator import DaoGenerator
from backend.core.crud.src.generator.validation.validation_code_generator import ValidationCodeGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.constants.types.type_mapper import TypeMapper
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class PythonDaoGenerator(DaoGenerator):
    """
    Generates Python DAO classes using SQLAlchemy and dynamic SQL templates.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel) -> str:
        # Generate validation code for fields
        validation_code = ValidationCodeGenerator.fromLanguage(AllowedLanguages.python).forFields(table_model.fields)

        # Obtain SQL queries for CRUD operations
        sql_generator = SQLGenerator.fromDBMS(dbms, table_model)
        insert_query = sql_generator.generate_insert()
        select_query = sql_generator.generate_select()
        update_query = sql_generator.generate_update()
        delete_query = sql_generator.generate_delete()

        python_mapper = TypeMapper.fromLanguage(AllowedLanguages.python)

        # Generate field parameters for methods
        field_parameters = ", ".join(
            f"{field.name}: {python_mapper.map(field.type)}"
            for field in table_model.fields if not field.autoIncrement
        )
        set_insert_parameters = ", ".join(field.name for field in table_model.fields if not field.autoIncrement)

        set_update_parameters = ", ".join(field.name for field in table_model.fields if not field.primaryKey)

        # Load the DAO template
        dao_template = TemplateLoader.forLanguage(AllowedLanguages.python).getDao()

        # Format validation code with the appropriate indentation
        base_indent = dao_template.split("{ValidationCode}")[0].splitlines()[-1]
        if validation_code:
            validation_code = CodeFormatter.format_code_with_indent(validation_code, base_indent)

        # Populate the DAO template with values
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

    python_dao_code = PythonDaoGenerator.generate(
        dbms=AllowedDBMS.postgresql,
        table_model=table
    )

    print(python_dao_code)
