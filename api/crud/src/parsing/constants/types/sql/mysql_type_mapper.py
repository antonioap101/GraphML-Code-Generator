from typing import Dict

from api.crud.src.parsing.constants.types.type_mapper import TypeMapper, TypeEnum


class MySQLTypeMapper(TypeMapper):
    _mapping: Dict[TypeEnum, str] = {
        TypeEnum.NUMBER: "INT",
        TypeEnum.TEXT: "VARCHAR({length})",
        TypeEnum.BOOLEAN: "TINYINT(1)",
        TypeEnum.FLOAT: "FLOAT",
        TypeEnum.DOUBLE: "DOUBLE",
    }

    def get_mapping(self, type_enum: TypeEnum) -> str:
        if type_enum not in self._mapping:
            raise ValueError(f"TypeEnum {type_enum} is not mapped in MySQL")
        return self._mapping[type_enum]

    def validate(self):
        for type_enum in TypeEnum:
            if type_enum not in self._mapping:
                raise ValueError(f"TypeEnum {type_enum} is missing in MySQL mapping")
