from typing import List

from pydantic import BaseModel

from backend.core.crud.src.parsing.input_elements.field_model import FieldModel


class TableModel(BaseModel):
    name: str
    fields: List[FieldModel]
