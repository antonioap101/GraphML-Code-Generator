from typing import Tuple

from backend.core.crud.src.generator.languages.connection.connection_generator import ConnectionGenerator
from backend.core.crud.src.generator.languages.dao.dao_generator import DaoGenerator
from backend.core.crud.src.generator.languages.language_generator_factory import LanguageGeneratorFactory
from backend.core.crud.src.parsing.CRUDCodeGeneratorInput import CRUDCodeGeneratorInput
from backend.core.crud.src.parsing.constants.types.type_mapper import TypeMapper


class CRUDCodeGenerator:
    """
    Clase principal para generar el código completo de CRUD, incluyendo conexión, creación de tablas y DAO.
    """

    @staticmethod
    def generate_code(input_data: CRUDCodeGeneratorInput) -> str:
        """
        Genera todo el código basado en los parámetros proporcionados.

        Args:
            input_data (CRUDCodeGeneratorInput): Los datos de entrada para la generación de código.

        Returns:
            str: Código completo generado.
        """

        # Obtener el generador de código para el lenguaje específico
        generators: Tuple[ConnectionGenerator, DaoGenerator] = LanguageGeneratorFactory.get_generators(input_data.language)
        connection_generator, dao_generator = generators

        # Generar el código del DAO
        dao_code = dao_generator.generate(input_data.dbms, input_data.table)

        # Generar el código de la conexión a la base de datos
        db_connection_code = connection_generator.generate(input_data.dbms, input_data.table, input_data.connectionParams)

        # Generar el indicador de comentario
        comment_indicator = TypeMapper.fromLanguage(input_data.language).get_comment_indicator()

        # Combinar todas las partes en un único string de salida
        complete_code = f"""
{comment_indicator} Database Connection Code
{db_connection_code}

{comment_indicator} DAO Code
{dao_code}
    """

        return complete_code.strip()


# Ejemplo de uso
if __name__ == "__main__":
    from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
    from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
    from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
    from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
    from backend.core.crud.src.parsing.input_elements.table_model import TableModel
    from backend.core.crud.src.parsing.input_elements.validations import Validations
    from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters

    input_data = CRUDCodeGeneratorInput(
        language=AllowedLanguages.python,
        dbms=AllowedDBMS.postgresql,
        table=TableModel(
            name="users",
            fields=[
                FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True),
                FieldModel(name="name", type=TypeEnum.TEXT, validations=Validations(minLength=3, maxLength=50)),
                FieldModel(name="email", type=TypeEnum.TEXT, unique=True),
                FieldModel(name="age", type=TypeEnum.NUMBER),
            ],
        ),
        connectionParams=ConnectionParameters(
            host="localhost",
            port=5432,
            database_name="default",
            username="postgres",
            password="1234",
        )
    )

    print(CRUDCodeGenerator.generate_code(input_data))
