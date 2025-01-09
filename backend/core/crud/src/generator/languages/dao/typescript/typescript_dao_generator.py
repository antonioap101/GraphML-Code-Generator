from backend.core.crud.src.generator.SQL.SQL_generator import SQLGenerator
from backend.core.crud.src.generator.languages.dao.dao_generator import DaoGenerator
from backend.core.crud.src.generator.languages.validation.validation_code_generator import ValidationCodeGenerator
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
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
        param_name = table_model.name.lower()

        # Consultas SQL
        insert_query = sql_generator.generate_insert()
        insert_values = ", ".join(f"{field.name}" for field in table_model.fields if not field.autoIncrement)
        select_query = sql_generator.generate_select()
        update_query = sql_generator.generate_update()
        update_values = ", ".join(f"{field.name}" for field in table_model.fields if not field.primaryKey)
        delete_query = sql_generator.generate_delete()

        # Rellenar plantilla
        ts_code = TemplateLoader.forLanguage(AllowedLanguages.typescript).getDao().format(
            ClassName=class_name,
            paramName=param_name,
            ValidationCode=validation_code,
            InsertQuery=insert_query,
            InsertValues=insert_values,
            SelectQuery=select_query,
            UpdateQuery=update_query,
            UpdateValues=update_values,
            DeleteQuery=delete_query,
        )

        return ts_code

