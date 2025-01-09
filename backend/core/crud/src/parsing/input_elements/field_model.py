from typing import Optional

from pydantic import BaseModel

from backend.core.crud.src.parsing.constants.types.type_mapper import TypeEnum
from backend.core.crud.src.parsing.input_elements.validations import Validations


class FieldModel(BaseModel):
    name: str
    type: TypeEnum
    primaryKey: Optional[bool] = False
    autoIncrement: Optional[bool] = False
    nullable: Optional[bool] = True
    unique: Optional[bool] = False
    validations: Optional[Validations]

    def __init__(self, name: str, type: TypeEnum, primaryKey: Optional[bool] = False,
                 autoIncrement: Optional[bool] = False, nullable: Optional[bool] = True,
                 unique: Optional[bool] = False, validations: Optional[Validations] = None):
        super().__init__(name=name, type=type, primaryKey=primaryKey, autoIncrement=autoIncrement,
                         nullable=nullable, unique=unique, validations=validations)
        # Validar las validaciones para el tipo del campo
        if self.validations:
            self.validations.validate_for_type(self.type)


if __name__ == '__main__':
    # Crear un campo con validaciones permitidas
    validations = Validations(minLength=5, maxLength=10)
    field = FieldModel(name="campo", type=TypeEnum.TEXT, validations=validations)
    print(field)

    # Crear un campo con validaciones no permitidas
    validations = Validations(minValue=5, maxValue=10)
    try:
        field = FieldModel(name="campo", type=TypeEnum.NUMBER, validations=validations)
        print(field)
    except ValueError as e:
        print(e)
