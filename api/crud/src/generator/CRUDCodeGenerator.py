from typing import Tuple

from api.crud.src.generator.languages.connection_generator import ConnectionGenerator
from api.crud.src.generator.languages.dao_generator import DaoGenerator
from api.crud.src.generator.languages.factory.language_generator_factory import LanguageGeneratorFactory
from api.crud.src.parsing.CRUDCodeGeneratorInput import CRUDCodeGeneratorInput


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

        # Combinar todas las partes en un único string de salida
        complete_code = f"""
        // Database Connection Code
        {db_connection_code}

        // DAO Code
        {dao_code}
        """

        return complete_code.strip()
