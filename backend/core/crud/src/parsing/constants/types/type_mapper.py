from typing import Dict

from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum


class TypeMapper:
    """
    Clase genérica para manejar mapeos de tipos para lenguajes y DBMS.
    """

    _language_type_mappings: Dict[AllowedLanguages, Dict] = {
        AllowedLanguages.java: {
            "type_mapping": {
                TypeEnum.NUMBER: "int",
                TypeEnum.TEXT: "String",
                TypeEnum.BOOLEAN: "boolean",
                TypeEnum.FLOAT: "float",
                TypeEnum.DOUBLE: "double",
            },
            "comment_indicator": "//",
        },
        AllowedLanguages.csharp: {
            "type_mapping": {
                TypeEnum.NUMBER: "int",
                TypeEnum.TEXT: "string",
                TypeEnum.BOOLEAN: "bool",
                TypeEnum.FLOAT: "float",
                TypeEnum.DOUBLE: "double",
            },
            "comment_indicator": "//",
        },
        AllowedLanguages.python: {
            "type_mapping": {
                TypeEnum.NUMBER: "int",
                TypeEnum.TEXT: "str",
                TypeEnum.BOOLEAN: "bool",
                TypeEnum.FLOAT: "float",
                TypeEnum.DOUBLE: "float",
            },
            "comment_indicator": "#",
        },
        AllowedLanguages.typescript: {
            "type_mapping": {
                TypeEnum.NUMBER: "number",
                TypeEnum.TEXT: "string",
                TypeEnum.BOOLEAN: "boolean",
                TypeEnum.FLOAT: "number",
                TypeEnum.DOUBLE: "number",
            },
            "comment_indicator": "//",
        },
    }

    _dbms_type_mappings: Dict[AllowedDBMS, Dict] = {
        AllowedDBMS.mysql: {
            "type_mapping": {
                TypeEnum.NUMBER: "INT",
                TypeEnum.TEXT: "VARCHAR(250)",
                TypeEnum.BOOLEAN: "TINYINT(1)",
                TypeEnum.FLOAT: "FLOAT",
                TypeEnum.DOUBLE: "DOUBLE",
            },
            "comment_indicator": "--",
        },
        AllowedDBMS.postgresql: {
            "type_mapping": {
                TypeEnum.NUMBER: "INTEGER",
                TypeEnum.TEXT: "VARCHAR(250)",
                TypeEnum.BOOLEAN: "BOOLEAN",
                TypeEnum.FLOAT: "REAL",
                TypeEnum.DOUBLE: "DOUBLE PRECISION",
            },
            "comment_indicator": "--",
        },
        AllowedDBMS.sqlite: {
            "type_mapping": {
                TypeEnum.NUMBER: "INTEGER",
                TypeEnum.TEXT: "TEXT",
                TypeEnum.BOOLEAN: "BOOLEAN",
                TypeEnum.FLOAT: "REAL",
                TypeEnum.DOUBLE: "REAL",
            },
            "comment_indicator": "--",
        },
        AllowedDBMS.oracle: {
            "type_mapping": {
                TypeEnum.NUMBER: "NUMBER",
                TypeEnum.TEXT: "VARCHAR2(250)",
                TypeEnum.BOOLEAN: "NUMBER",
                TypeEnum.FLOAT: "REAL",
                TypeEnum.DOUBLE: "DOUBLE PRECISION",
            },
            "comment_indicator": "--",
        },
    }

    def __init__(self, type_mapping: Dict[TypeEnum, str], comment_indicator: str):
        self._type_mapping = type_mapping
        self._comment_indicator = comment_indicator

    @classmethod
    def fromLanguage(cls, language: AllowedLanguages) -> "TypeMapper":
        """
        Crea un TypeMapper basado en un lenguaje de programación.
        """
        if language not in cls._language_type_mappings:
            raise ValueError(f"Lenguaje no soportado: {language}")
        config = cls._language_type_mappings[language]
        return cls(config["type_mapping"], config["comment_indicator"])

    @classmethod
    def fromDBMS(cls, dbms: AllowedDBMS) -> "TypeMapper":
        """
        Crea un TypeMapper basado en un DBMS.
        """
        if dbms not in cls._dbms_type_mappings:
            raise ValueError(f"DBMS no soportado: {dbms}")
        config = cls._dbms_type_mappings[dbms]
        return cls(config["type_mapping"], config["comment_indicator"])

    def map(self, type_enum: TypeEnum) -> str:
        """
        Mapea un TypeEnum al tipo correspondiente en el lenguaje o DBMS.
        """
        if type_enum not in self._type_mapping:
            raise ValueError(f"TypeEnum {type_enum} no está mapeado.")
        return self._type_mapping[type_enum]

    def get_comment_indicator(self) -> str:
        """
        Obtiene el indicador de comentarios.
        """
        return self._comment_indicator


if __name__ == "__main__":
    # Crear un TypeMapper para Java
    java_mapper = TypeMapper.fromLanguage(AllowedLanguages.java)
    print(java_mapper.map(TypeEnum.NUMBER))  # int
    print(java_mapper.get_comment_indicator())  # //

    # Crear un TypeMapper para MySQL
    mysql_mapper = TypeMapper.fromDBMS(AllowedDBMS.mysql)
    print(mysql_mapper.map(TypeEnum.NUMBER))  # INT
    print(mysql_mapper.get_comment_indicator())  # --

