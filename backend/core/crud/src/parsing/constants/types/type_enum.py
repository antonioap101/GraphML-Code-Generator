from enum import Enum


class TypeEnum(str, Enum):
    NUMBER = "number"
    TEXT = "string"
    BOOLEAN = "boolean"
    FLOAT = "float"
    DOUBLE = "double"


# Configuración para lenguajes
LANGUAGE_TYPE_MAPPINGS = {
    "java": {
        "type_mapping": {
            TypeEnum.NUMBER: "int",
            TypeEnum.TEXT: "String",
            TypeEnum.BOOLEAN: "boolean",
            TypeEnum.FLOAT: "float",
            TypeEnum.DOUBLE: "double",
        },
        "comment_indicator": "//",
    },
    "csharp": {
        "type_mapping": {
            TypeEnum.NUMBER: "int",
            TypeEnum.TEXT: "string",
            TypeEnum.BOOLEAN: "bool",
            TypeEnum.FLOAT: "float",
            TypeEnum.DOUBLE: "double",
        },
        "comment_indicator": "//",
    },
    "python": {
        "type_mapping": {
            TypeEnum.NUMBER: "int",
            TypeEnum.TEXT: "str",
            TypeEnum.BOOLEAN: "bool",
            TypeEnum.FLOAT: "float",
            TypeEnum.DOUBLE: "float",
        },
        "comment_indicator": "#",
    },
    "typescript": {
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

# Configuración para DBMS
DBMS_TYPE_MAPPINGS = {
    "mysql": {
        "type_mapping": {
            TypeEnum.NUMBER: "INT",
            TypeEnum.TEXT: "VARCHAR({length})",
            TypeEnum.BOOLEAN: "TINYINT(1)",
            TypeEnum.FLOAT: "FLOAT",
            TypeEnum.DOUBLE: "DOUBLE",
        },
        "comment_indicator": "--",
    },
    "postgresql": {
        "type_mapping": {
            TypeEnum.NUMBER: "INTEGER",
            TypeEnum.TEXT: "CHARACTER VARYING({length})",
            TypeEnum.BOOLEAN: "BOOLEAN",
            TypeEnum.FLOAT: "REAL",
            TypeEnum.DOUBLE: "DOUBLE PRECISION",
        },
        "comment_indicator": "--",
    },
    "sqlite": {
        "type_mapping": {
            TypeEnum.NUMBER: "INTEGER",
            TypeEnum.TEXT: "TEXT",
            TypeEnum.BOOLEAN: "BOOLEAN",
            TypeEnum.FLOAT: "REAL",
            TypeEnum.DOUBLE: "REAL",
        },
        "comment_indicator": "--",
    },
    "oracle": {
        "type_mapping": {
            TypeEnum.NUMBER: "NUMBER",
            TypeEnum.TEXT: "VARCHAR2({length})",
            TypeEnum.BOOLEAN: "NUMBER",
            TypeEnum.FLOAT: "REAL",
            TypeEnum.DOUBLE: "DOUBLE PRECISION",
        },
        "comment_indicator": "--",
    },
}
