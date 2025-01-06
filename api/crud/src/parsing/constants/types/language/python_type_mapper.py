from typing import Dict

from api.crud.src.parsing.constants.types.type_mapper import TypeMapper, TypeEnum


class PythonTypeMapper(TypeMapper):
    _mapping: Dict[TypeEnum, str] = {
        TypeEnum.NUMBER: "int",
        TypeEnum.TEXT: "str",
        TypeEnum.BOOLEAN: "bool",
        TypeEnum.FLOAT: "float",
        TypeEnum.DOUBLE: "float",
    }

    def get_mapping(self, type_enum: TypeEnum) -> str:
        if type_enum not in self._mapping:
            raise ValueError(f"TypeEnum {type_enum} is not mapped in Python")
        return self._mapping[type_enum]

    def validate(self):
        for type_enum in TypeEnum:
            if type_enum not in self._mapping:
                raise ValueError(f"TypeEnum {type_enum} is missing in Python mapping")

    def get_comment_indicator(self) -> str:
        return "#"

