from typing import Dict

from api.crud.src.parsing.constants.types.type_mapper import TypeMapper, TypeEnum


class JavaTypeMapper(TypeMapper):
    _mapping: Dict[TypeEnum, str] = {
        TypeEnum.NUMBER: "int",
        TypeEnum.TEXT: "String",
        TypeEnum.BOOLEAN: "boolean",
        TypeEnum.FLOAT: "float",
        TypeEnum.DOUBLE: "double",
    }

    def get_mapping(self, type_enum: TypeEnum) -> str:
        if type_enum not in self._mapping:
            raise ValueError(f"TypeEnum {type_enum} is not mapped in Java")
        return self._mapping[type_enum]

    def validate(self):
        for type_enum in TypeEnum:
            if type_enum not in self._mapping:
                raise ValueError(f"TypeEnum {type_enum} is missing in Java mapping")
