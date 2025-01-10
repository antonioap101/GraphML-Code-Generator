import json
from enum import Enum
from pathlib import Path
from typing import Dict

from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.input_elements.validations import ValidationsEnum

# Define el directorio base del archivo como constante
TEMPLATES_DIR = Path(__file__).resolve().parent


class TemplateType:
    class SQL(Enum):
        PLACEHOLDER = "placeholder"
        AUTO_INCREMENT = "auto_increment"
        CREATE_TABLE = "create_table"
        INSERT = "insert"
        SELECT = "select"
        UPDATE = "update"
        DELETE = "delete"

    class LANGUAGE(Enum):
        CONNECTION = "connection"
        DAO = "dao"
        VALIDATIONS = "validations"

    SQL = SQL
    LANGUAGE = LANGUAGE


class TemplateLoader:
    """
    Carga y gestiona plantillas de generación de código.
    """

    def __init__(self, language: AllowedLanguages = None, dbms: AllowedDBMS = None):
        self.language = language
        self.dbms = dbms
        self.index = TemplateLoader.TemplateIndex.load_index()

    @classmethod
    def forLanguage(cls, language: AllowedLanguages) -> "TemplateLoader":
        """
        Crea una instancia de TemplateLoader para un lenguaje específico.
        """
        return cls(language=language)

    @classmethod
    def forDBMS(cls, dbms: AllowedDBMS) -> "TemplateLoader":
        """
        Crea una instancia de TemplateLoader para un DBMS específico.
        """
        return cls(dbms=dbms)

    def getConnection(self) -> str:
        """
        Carga la plantilla de conexión.
        """
        return self._load_template("languages", self.language.value, TemplateType.LANGUAGE.CONNECTION)

    def getDao(self) -> str:
        """
        Carga la plantilla de DAO.
        """
        return self._load_template("languages", self.language.value, TemplateType.LANGUAGE.DAO)

    def getValidations(self) -> Dict[ValidationsEnum, str]:
        """
        Carga las plantillas estructuradas de validaciones.
        """
        try:
            validations_index = self.index["languages"][self.language.value][TemplateType.LANGUAGE.VALIDATIONS.value]
            validations_templates = {}
            for validation_type, path in validations_index.items():
                template_path = TEMPLATES_DIR / path
                with open(template_path, "r") as file:
                    validations_templates[ValidationsEnum(validation_type)] = file.read()
            return validations_templates
        except KeyError as e:
            raise ValueError(f"Validations templates not found for {self.language}") from e

    def getSQLTemplate(self, sql_type: TemplateType.SQL) -> str:
        """
        Carga una plantilla SQL específica (e.g., create_table, insert).
        """
        try:
            sql_index = self.index["sql"][self.dbms.value]
            template_path = TEMPLATES_DIR / sql_index[sql_type.value]
            with open(template_path, "r") as file:
                return file.read()
        except KeyError as e:
            raise ValueError(f"SQL template '{sql_type}' not found for {self.dbms}") from e

    def getPlaceholder(self) -> str:
        """
        Carga la plantilla del placeholder para el DBMS actual.
        """
        return self.getSQLTemplate(TemplateType.SQL.PLACEHOLDER)

    def getAutoIncrementKeyword(self) -> str:
        """
        Carga la plantilla de auto_increment_keyword para el DBMS actual.
        """
        return self.getSQLTemplate(TemplateType.SQL.AUTO_INCREMENT)

    def _load_template(self, section: str, key: str, template_type: TemplateType) -> str:
        """
        Carga la plantilla para un tipo específico.
        """
        try:
            path = self.index[section][key][template_type.value]
            template_path = TEMPLATES_DIR / path
            with open(template_path, "r") as file:
                return file.read()
        except KeyError as e:
            raise ValueError(f"Template {template_type.value} not found in section '{section}' for key '{key}'") from e

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
    # Ejemplo de uso para lenguajes
    loader_lang = TemplateLoader.forLanguage(AllowedLanguages.python)
    print(loader_lang.getConnection())
    print(loader_lang.getDao())
    print(loader_lang.getValidations())

    loader_dbms = TemplateLoader.forDBMS(AllowedDBMS.mysql)
    print(loader_dbms.getSQLTemplate(TemplateType.SQL.CREATE_TABLE))
    print(loader_dbms.getSQLTemplate(TemplateType.SQL.INSERT))
