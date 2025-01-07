from api.crud.src.generator.languages.dao_generator import DaoGenerator
from api.crud.src.parsing.components.field_model import FieldModel
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from api.crud.src.templates.template_loader import TemplateType, TemplateLoader


class PythonDaoGenerator(DaoGenerator):
    """
    Generates Python DAO code for CRUD operations.
    """
    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel) -> str:
        columns = [field.name for field in table_model.fields if not field.autoIncrement]
        placeholders = ["%s"] * len(columns)
        update_columns = [f"{field.name}=%s" for field in table_model.fields if not field.primaryKey]

        python_code = TemplateLoader.load_template(AllowedLanguages.python, TemplateType.DAO).format(
            TableName=table_model.name.capitalize(),
            table_name=table_model.name,
            columns=", ".join(columns),
            placeholders=", ".join(placeholders),
            values=", ".join(columns),
            update_columns=", ".join(update_columns),
            update_set_clause=", ".join(update_columns),
            update_values=", ".join(columns),
        )

        return python_code


# Example usage
if __name__ == "__main__":
    table = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type="number", primaryKey=True, autoIncrement=True, nullable=False),
            FieldModel(name="name", type="string", nullable=False, unique=False),
            FieldModel(name="email", type="string", nullable=False, unique=True),
            FieldModel(name="age", type="number", nullable=True)
        ]
    )

    python_dao_code = PythonDaoGenerator.generate(
        dbms=AllowedDBMS.postgresql,
        table_model=table
    )

    print(python_dao_code)
