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


if __name__ == "__main__":
    from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
    from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
    from backend.core.crud.src.parsing.input_elements.validations import Validations
    from backend.core.crud.src.generator.languages.dao.typescript.typescript_dao_generator import TypeScriptDaoGenerator
    from backend.core.crud.src.generator.languages.dao.python.python_dao_generator import PythonDaoGenerator
    from backend.core.crud.src.generator.languages.dao.java.java_dao_generator import JavaDaoGenerator
    from backend.core.crud.src.generator.languages.dao.csharp.csharp_dao_generator import CSharpDaoGenerator

    table_model = TableModel(
        name="users",
        fields=[
            FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True),
            FieldModel(name="name", type=TypeEnum.TEXT, validations=Validations(minLength=3, maxLength=20, pattern=r"^[a-zA-Z ]+$")
                       ),
            FieldModel(name="email", type=TypeEnum.TEXT),
            FieldModel(name="age", type=TypeEnum.NUMBER, validations=Validations(minValue=0, maxValue=150,
                                                                                 customCode="if (age < 18) {\n    throw new Error('Age must be at least 18');\n}")),
        ]
    )

    # Generar el código DAO en TypeScript
    ts_dao_code = TypeScriptDaoGenerator.generate(AllowedDBMS.mysql, table_model)
    print(ts_dao_code)

    # Generar el código DAO en Python
    python_dao_code = PythonDaoGenerator.generate(AllowedDBMS.mysql, table_model)
    print(python_dao_code)

    # Generar el código DAO en Java
    java_dao_code = JavaDaoGenerator.generate(AllowedDBMS.mysql, table_model)
    print(java_dao_code)

    # Generar el código DAO en C#
    csharp_dao_code = CSharpDaoGenerator.generate(AllowedDBMS.mysql, table_model)
    print(csharp_dao_code)
