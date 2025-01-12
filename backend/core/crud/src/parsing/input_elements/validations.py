from enum import Enum
from typing import Optional, Set

from pydantic import BaseModel

from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum


class ValidationsEnum(str, Enum):
    minLength = "minLength"
    maxLength = "maxLength"
    pattern = "pattern"
    minValue = "minValue"
    maxValue = "maxValue"
    customCode = "customCode"


# Definir las validaciones permitidas por tipo con minValue y maxValue
VALIDATIONS_BY_TYPE = {
    TypeEnum.TEXT: {ValidationsEnum.minLength, ValidationsEnum.maxLength, ValidationsEnum.pattern, ValidationsEnum.customCode},
    TypeEnum.NUMBER: {ValidationsEnum.minValue, ValidationsEnum.maxValue, ValidationsEnum.customCode},
    TypeEnum.FLOAT: {ValidationsEnum.minValue, ValidationsEnum.maxValue, ValidationsEnum.customCode},
    TypeEnum.DOUBLE: {ValidationsEnum.minValue, ValidationsEnum.maxValue, ValidationsEnum.customCode},
    TypeEnum.BOOLEAN: {ValidationsEnum.customCode},  # No admite validaciones adicionales
}

class Validations(BaseModel):
    minLength: Optional[int]
    maxLength: Optional[int]
    pattern: Optional[str]
    minValue: Optional[int]
    maxValue: Optional[int]
    customCode: Optional[str]

    def validate_for_type(self, type_enum: TypeEnum):
        # Obtener validaciones permitidas para el tipo
        allowed_validations: Set[ValidationsEnum] = VALIDATIONS_BY_TYPE.get(type_enum, set())

        # Verificar que cada atributo definido esté permitido
        for field_name, value in self.dict().items():
            if value is not None and ValidationsEnum(field_name) not in allowed_validations:
                raise ValueError(f"'{field_name}' no es una validación permitida para el tipo {type_enum}")