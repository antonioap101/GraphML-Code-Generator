from api.crud.src.generator.SQL.SQL_generator_factory import SQLGeneratorFactory
from api.crud.src.generator.languages.dao_generator import DaoGenerator
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from api.crud.src.templates.template_loader import TemplateType, TemplateLoader


class TypeScriptDaoGenerator(DaoGenerator):
    """
    Generates the Data Access Object (DAO) implementation in TypeScript.
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel) -> str:
        """
        Generates the TypeScript code for DAO.
        """
        sql_generator = SQLGeneratorFactory.get(dbms, table_model)
        class_name = table_model.name.capitalize()
        param_name = table_model.name.lower()

        insert_query = sql_generator.generate_insert()
        insert_values = ", ".join(f"{field.name}" for field in table_model.fields if not field.autoIncrement)

        select_query = sql_generator.generate_select()

        update_query = sql_generator.generate_update()
        update_values = ", ".join(f"{field.name}" for field in table_model.fields if not field.primaryKey)

        delete_query = sql_generator.generate_delete()

        ts_code = TemplateLoader.load_template(AllowedLanguages.typescript, TemplateType.DAO).format(
            ClassName=class_name,
            paramName=param_name,
            InsertQuery=insert_query,
            InsertValues=insert_values,
            SelectQuery=select_query,
            UpdateQuery=update_query,
            UpdateValues=update_values,
            DeleteQuery=delete_query,
        )

        return ts_code
