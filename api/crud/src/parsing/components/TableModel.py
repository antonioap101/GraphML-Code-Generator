from typing import List

from pydantic import BaseModel

from api.crud.src.parsing.components.FieldModel import FieldModel


class TableModel(BaseModel):
    name: str
    fields: List[FieldModel]
