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

