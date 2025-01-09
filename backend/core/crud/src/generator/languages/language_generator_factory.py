from typing import Tuple

from backend.core.crud.src.generator.languages.connection.connection_generator import ConnectionGenerator
from backend.core.crud.src.generator.languages.dao.csharp.csharp_connection_generator import CSharpConnectionGenerator
from backend.core.crud.src.generator.languages.dao.csharp.csharp_dao_generator import CSharpDaoGenerator
from backend.core.crud.src.generator.languages.dao.dao_generator import DaoGenerator
from backend.core.crud.src.generator.languages.dao.java.java_connection_generator import JavaConnectionGenerator
from backend.core.crud.src.generator.languages.dao.java.java_dao_generator import JavaDaoGenerator
from backend.core.crud.src.generator.languages.dao.python.python_connection_generator import PythonConnectionGenerator
from backend.core.crud.src.generator.languages.dao.python.python_dao_generator import PythonDaoGenerator
from backend.core.crud.src.generator.languages.dao.typescript.typescript_connection_generator import TypeScriptConnectionGenerator
from backend.core.crud.src.generator.languages.dao.typescript.typescript_dao_generator import TypeScriptDaoGenerator
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages


class LanguageGeneratorFactory:
    """
    Fábrica para obtener generadores de código específicos para diferentes lenguajes de programación.
    """

    _generators = {
        AllowedLanguages.java: (JavaConnectionGenerator, JavaDaoGenerator),
        AllowedLanguages.csharp: (CSharpConnectionGenerator, CSharpDaoGenerator),
        AllowedLanguages.typescript: (TypeScriptConnectionGenerator, TypeScriptDaoGenerator),
        AllowedLanguages.python: (PythonConnectionGenerator, PythonDaoGenerator)
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
            raise ValueError(f"LanguageGeneratorFactory -> Unsupported language: {language}")
        return LanguageGeneratorFactory._generators[language]
