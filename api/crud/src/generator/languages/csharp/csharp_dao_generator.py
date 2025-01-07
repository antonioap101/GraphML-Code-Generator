from api.crud.src.generator.SQL.SQL_generator_factory import SQLGeneratorFactory
from api.crud.src.generator.languages.dao_generator import DaoGenerator
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from api.crud.src.parsing.constants.types.factory.type_mapper_factory import TypeMapperFactory
from api.crud.src.templates.template_loader import TemplateLoader, TemplateType


class CSharpDaoGenerator(DaoGenerator):
    """
    Generates DAO classes in C# based on table metadata and SQL queries.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table: TableModel) -> str:
        """
        Generates the DAO class code for C# based on the table metadata and DBMS.
        """
        # Get the SQL generator for the DBMS
        sql_generator = SQLGeneratorFactory.get(dbms, table)

        # Generate SQL queries
        insert_query = sql_generator.generate_insert()
        select_query = sql_generator.generate_select()
        update_query = sql_generator.generate_update()
        delete_query = sql_generator.generate_delete()

        sql_mapper = TypeMapperFactory.get_dbms_mapper(dbms)
        csharp_mapper = TypeMapperFactory.get_language_mapper(AllowedLanguages.csharp)

        # Generate field parameters and set statements
        field_parameters = ", ".join(
            f"{csharp_mapper.get_mapping(field.type)} {field.name}"
            for field in table.fields if not field.autoIncrement
        )
        set_insert_parameters = "\n            ".join(
            f"command.Parameters.AddWithValue(\"@{field.name}\", {field.name});"
            for field in table.fields if not field.autoIncrement
        )
        set_update_parameters = "\n            ".join(
            f"command.Parameters.AddWithValue(\"@{field.name}\", {field.name});"
            for field in table.fields if not field.primaryKey
        )

        template = TemplateLoader.load_template(AllowedLanguages.csharp, TemplateType.DAO)

        # Fill the template with the generated values
        csharp_code = template.format(
            ClassName=table.name.capitalize(),
            FieldParameters=field_parameters,
            InsertQuery=insert_query,
            SelectQuery=select_query,
            UpdateQuery=update_query,
            DeleteQuery=delete_query,
            SetInsertParameters=set_insert_parameters,
            SetUpdateParameters=set_update_parameters
        )

        return csharp_code
