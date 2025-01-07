from typing import Optional

from pydantic import BaseModel

from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.components.connection_parameters import ConnectionParameters
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages


# Define the model
class CRUDCodeGeneratorInput(BaseModel):
    table: TableModel
    language: AllowedLanguages
    dbms: AllowedDBMS
    connectionParams: ConnectionParameters
