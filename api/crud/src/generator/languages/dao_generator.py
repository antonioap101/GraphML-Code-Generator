from abc import abstractmethod, ABC

from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class DaoGenerator(ABC):
    @staticmethod
    @abstractmethod
    def generate(dbms: AllowedDBMS, table: TableModel):
        """
        Genera el código de una clase DAO en Java basada en los metadatos de la tabla y el DBMS.
        """
        pass
