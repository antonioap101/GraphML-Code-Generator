from typing import Optional

from pydantic import BaseModel

from api.crud.src.parsing.components.TableModel import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages


# Define the model
class CRUDGeneratorInput(BaseModel):
    table: TableModel
    language: AllowedLanguages
    dbms: AllowedDBMS
    customCode: Optional[dict] = None

    @staticmethod  # With strings that convert to the corresponding enum types
    def create(table: TableModel, language: str, dbms: str, custom_code: Optional[dict] = None):
        return CRUDGeneratorInput(table, AllowedLanguages(language), AllowedDBMS(dbms), custom_code)
