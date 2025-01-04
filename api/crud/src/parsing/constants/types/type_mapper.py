# Enum Types allowed for input fields for the table (generic, not python specific = INTEGER, STRING, BOOLEAN)
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class TypeEnum(str, Enum):
    NUMBER = "number"
    TEXT = "string"
    BOOLEAN = "boolean"
    FLOAT = "float"
    DOUBLE = "double"


class TypeMapper(ABC):
    @abstractmethod
    def get_mapping(self, type_enum: TypeEnum) -> str:
        """Devuelve el mapeo para un tipo específico."""
        pass

    @abstractmethod
    def validate(self):
        """Valida que todos los TypeEnum están mapeados."""
        pass


# class TypeMapping:
#     def __init__(self, mysql: str, postgresql: str, sqlite: str, oracle: str):
#         self.mysql = mysql
#         self.postgresql = postgresql
#         self.sqlite = sqlite
#         self.oracle = oracle
#
#
# SQL_TYPE_MAPPING: Dict[TypeEnum, TypeMapping] = {
#     TypeEnum.NUMBER: TypeMapping(
#         mysql="INT",
#         postgresql="INTEGER",
#         sqlite="INTEGER",
#         oracle="NUMBER"
#     ),
#     TypeEnum.TEXT: TypeMapping(
#         mysql="VARCHAR({length})",
#         postgresql="CHARACTER VARYING({length})",
#         sqlite="TEXT",
#         oracle="VARCHAR2({length})"
#     ),
#     TypeEnum.BOOLEAN: TypeMapping(
#         mysql="TINYINT(1)",
#         postgresql="BOOLEAN",
#         sqlite="BOOLEAN",
#         oracle="NUMBER(1)"
#     ),
#     TypeEnum.FLOAT: TypeMapping(
#         mysql="FLOAT",
#         postgresql="REAL",
#         sqlite="REAL",
#         oracle="FLOAT"
#     ),
#     TypeEnum.DOUBLE: TypeMapping(
#         mysql="DOUBLE",
#         postgresql="DOUBLE PRECISION",
#         sqlite="REAL",
#         oracle="DOUBLE PRECISION"
#     )
# }
