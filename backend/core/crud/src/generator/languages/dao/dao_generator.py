from abc import abstractmethod, ABC

from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.input_elements.table_model import TableModel


class DaoGenerator(ABC):
    @staticmethod
    @abstractmethod
    def generate(dbms: AllowedDBMS, table: TableModel):
        """
        Genera el código de una clase DAO en Java basada en los metadatos de la tabla y el DBMS.
        """
        pass

    @staticmethod
    def format_validation_code_indent(dao_template, validation_code):
        if not validation_code or len(validation_code) == 0:
            return validation_code
        # Determine the indentation level for ValidationCode
        base_indent = dao_template.split("{ValidationCode}")[0].splitlines()[-1]
        validation_code_lines = validation_code.splitlines()
        # Apply the calculated indentation to each line of ValidationCode
        formatted_validation_code = f"{validation_code_lines[0]}\n" + "\n".join(
            f"{base_indent}{line}" for line in validation_code_lines[1:] if line.strip())
        return formatted_validation_code


if __name__ == "__main__":
    from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
    from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
    from backend.core.crud.src.parsing.input_elements.validations import Validations
    from backend.core.crud.src.generator.languages.dao.typescript.typescript_dao_generator import TypeScriptDaoGenerator

    table_model = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True),
            FieldModel(name="name", type=TypeEnum.TEXT, validations=Validations(minLength=3, maxLength=20, pattern=r"^[a-zA-Z ]+$")
                       ),
            FieldModel(name="email", type=TypeEnum.TEXT),
            FieldModel(name="age", type=TypeEnum.NUMBER)
        ]
    )

    # Generar el código DAO en TypeScript
    ts_dao_code = TypeScriptDaoGenerator.generate(AllowedDBMS.mysql, table_model)
    print(ts_dao_code)

    # # Generar el código DAO en Python
    # python_dao_code = PythonDaoGenerator.generate(AllowedDBMS.mysql, table_model)
    # print(python_dao_code)
    #
    # # Generar el código DAO en Java
    # java_dao_code = JavaDaoGenerator.generate(AllowedDBMS.mysql, table_model)
    # print(java_dao_code)
    #
    # # Generar el código DAO en C#
    # csharp_dao_code = CSharpDaoGenerator.generate(AllowedDBMS.mysql, table_model)
    # print(csharp_dao_code)
