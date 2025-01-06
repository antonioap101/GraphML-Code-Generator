from abc import ABC, abstractmethod
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class SQLGenerator(ABC):
    """
        Clase abstracta (interfaz común) SQLGenerator para generar consultas CRUD en SQL.
    """

    def __init__(self, table: TableModel, dbms: AllowedDBMS):
        self.table = table
        self.dbms = dbms

    @abstractmethod
    def generate_create_table(self) -> str:
        """Genera la consulta CREATE TABLE."""
        pass

    @abstractmethod
    def generate_insert(self) -> str:
        """Genera la consulta INSERT."""
        pass

    @abstractmethod
    def generate_select(self) -> str:
        """Genera la consulta SELECT."""
        pass

    @abstractmethod
    def generate_update(self) -> str:
        """Genera la consulta UPDATE."""
        pass

    @abstractmethod
    def generate_delete(self) -> str:
        """Genera la consulta DELETE."""
        pass
