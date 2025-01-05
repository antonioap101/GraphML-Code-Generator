from typing import Tuple

from api.crud.src.generator.languages.connection_generator import ConnectionGenerator
from api.crud.src.generator.languages.dao_generator import DaoGenerator
from api.crud.src.generator.languages.java.java_connection_generator import JavaConnectionGenerator
from api.crud.src.generator.languages.java.java_dao_generator import JavaDaoGenerator
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages


# Importa aquí otros generadores (e.g., TypeScript, CSharp) según se implementen

class LanguageGeneratorFactory:
    """
    Fábrica para obtener generadores de código específicos para diferentes lenguajes de programación.
    """

    _generators = {
        AllowedLanguages.java: (JavaConnectionGenerator, JavaDaoGenerator)
        # Añadir otros generadores aquí:
        # AllowedLanguages.typescript: TypeScriptDaoGenerator,
        # AllowedLanguages.csharp: CSharpDaoGenerator,
    }

    @staticmethod
    def get_generators(language: AllowedLanguages) -> Tuple[ConnectionGenerator, DaoGenerator]:
        """
        Obtiene el generador correspondiente para el lenguaje especificado.

        Args:
            language (AllowedLanguages): El lenguaje de programación deseado.

        Returns:
            Generador de código correspondiente al lenguaje.

        Raises:
            ValueError: Si el lenguaje no está soportado.
        """
        if language not in LanguageGeneratorFactory._generators:
            raise ValueError(f"Unsupported language: {language}")
        return LanguageGeneratorFactory._generators[language]
