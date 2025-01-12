from pydantic import BaseModel

from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.table_model import TableModel


# Define the model
class CRUDCodeGeneratorInput(BaseModel):
    table: TableModel
    language: AllowedLanguages
    dbms: AllowedDBMS
    connectionParams: ConnectionParameters
