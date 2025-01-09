import json
from enum import Enum
from pathlib import Path
from typing import Dict

from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.input_elements.validations import ValidationsEnum

# Define el directorio base del archivo como constante
TEMPLATES_DIR = Path(__file__).resolve().parent


class TemplateType(Enum):
    DAO = "dao"
    CONNECTION = "connection"
    VALIDATIONS = "validations"


class TemplateLoader:
    """
    Carga y gestiona plantillas de generación de código.
    """

    def __init__(self, language: AllowedLanguages):
        self.language = language
        self.index = TemplateLoader.TemplateIndex.load_index()

    @classmethod
    def forLanguage(cls, language: AllowedLanguages) -> "TemplateLoader":
        """
        Crea una instancia de TemplateLoader para un lenguaje específico.
        """
        return cls(language)

    def getConnection(self) -> str:
        """
        Carga la plantilla de conexión.
        """
        return self._load_template(TemplateType.CONNECTION)

    def getDao(self) -> str:
        """
        Carga la plantilla de DAO.
        """
        return self._load_template(TemplateType.DAO)

    def getValidations(self) -> Dict[ValidationsEnum, str]:
        """
        Carga las plantillas estructuradas de validaciones.
        """
        try:
            validations_index = self.index[self.language.value][TemplateType.VALIDATIONS.value]
            validations_templates = {}
            for validation_type, path in validations_index.items():
                template_path = TEMPLATES_DIR / path
                with open(template_path, "r") as file:
                    validations_templates[ValidationsEnum(validation_type)] = file.read()
            return validations_templates
        except KeyError as e:
            raise ValueError(f"Validations templates not found for {self.language}") from e

    def _load_template(self, template_type: TemplateType) -> str:
        """
        Carga la plantilla para un tipo específico.
        """
        try:
            path = self.index[self.language.value][template_type.value]
            template_path = TEMPLATES_DIR / path
            with open(template_path, "r") as file:
                return file.read()
        except KeyError as e:
            raise ValueError(f"Template {template_type.value} not found for {self.language}") from e

    class TemplateIndex:
        templates_path = TEMPLATES_DIR / "index.json"
        _index = None

        @staticmethod
        def load_index(file_path: Path = templates_path) -> dict:
            """
            Carga el índice de plantillas desde un archivo JSON.
            """
            if TemplateLoader.TemplateIndex._index is None:
                with open(file_path, "r") as file:
                    TemplateLoader.TemplateIndex._index = json.load(file)
            return TemplateLoader.TemplateIndex._index


if __name__ == "__main__":
    loader = TemplateLoader.forLanguage(AllowedLanguages.python)
    print(loader.getConnection())
    print(loader.getDao())
    print(loader.getValidations())