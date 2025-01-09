from abc import abstractmethod, ABC

from backend.core.crud.src.parsing.input_elements.connection_parameters import ConnectionParameters
from backend.core.crud.src.parsing.input_elements.table_model import TableModel
from backend.core.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class ConnectionGenerator(ABC):
    # Mapa de generadores de URLs
    _DB_URL_GENERATORS = {
        AllowedDBMS.mysql: lambda cp: f"jdbc:mysql://{cp.host}:{cp.port}/{cp.database_name}",
        AllowedDBMS.postgresql: lambda cp: f"jdbc:postgresql://{cp.host}:{cp.port}/{cp.database_name}",
        AllowedDBMS.sqlite: lambda cp: f"jdbc:sqlite:{cp.database_name}.db",
        AllowedDBMS.oracle: lambda cp: f"jdbc:oracle:thin:@{cp.host}:{cp.port}:{cp.database_name}",
    }

    @staticmethod
    @abstractmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel, connection_params: ConnectionParameters) -> str:
        """
        Genera el código para manejar la conexión a la base de datos y la creación de tablas.

        Args:
            dbms (AllowedDBMS): Tipo de DBMS (mysql, postgresql, etc.).
            table_model (TableModel): Modelo de la tabla.
            connection_params (ConnectionParameters): Parámetros de conexión.
        """
        pass

    @staticmethod
    def generate_db_url(dbms: AllowedDBMS, connection_params: ConnectionParameters) -> str:
        """
        Genera la URL de conexión para el DBMS especificado.

        Args:
            dbms (AllowedDBMS): El tipo de DBMS (mysql, postgresql, etc.).
            connection_params (ConnectionParameters): Parámetros de conexión.
        Returns:
            str: URL de conexión generada.
        Raises:
            ValueError: Si el DBMS no está soportado.
        """
        try:
            url_generator = ConnectionGenerator._DB_URL_GENERATORS[dbms.value]
            return url_generator(connection_params)
        except KeyError:
            raise ValueError(f"ConnectionGenerator -> Unsupported DBMS: {dbms}")
