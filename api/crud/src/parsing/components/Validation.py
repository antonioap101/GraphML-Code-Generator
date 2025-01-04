from typing import Optional

from pydantic import BaseModel


class Validation(BaseModel):
    minLength: Optional[int]
    maxLength: Optional[int]
    pattern: Optional[str]
    min: Optional[int]
    max: Optional[int]
