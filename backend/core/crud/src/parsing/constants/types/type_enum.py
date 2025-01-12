from enum import Enum


class TypeEnum(str, Enum):
    NUMBER = "number"
    TEXT = "string"
    BOOLEAN = "boolean"
    FLOAT = "float"
    DOUBLE = "double"

