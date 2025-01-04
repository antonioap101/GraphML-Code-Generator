from typing import Optional

from pydantic import BaseModel

from api.crud.src.parsing.components.Validation import Validation
from api.crud.src.parsing.constants.types.type_mapper import TypeEnum


class FieldModel(BaseModel):
    name: str
    type: TypeEnum
    primaryKey: Optional[bool] = False
    autoIncrement: Optional[bool] = False
    nullable: Optional[bool] = True
    unique: Optional[bool] = False
    validations: Optional[Validation]

    @staticmethod
    def create(name: str, type: str, primaryKey: Optional[bool] = False, autoIncrement: Optional[bool] = False, nullable: Optional[bool] = True,
               unique: Optional[bool] = False, validations: Optional[Validation] = None):
        return FieldModel(name, TypeEnum(type), primaryKey, autoIncrement, nullable, unique, validations)
