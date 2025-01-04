from pydantic import BaseModel


class CustomValidation(BaseModel):
    field: str
    code: str
