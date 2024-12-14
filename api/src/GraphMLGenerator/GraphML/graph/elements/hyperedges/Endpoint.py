from enum import Enum
from typing import Optional

from api.src.GraphMLGenerator.GraphML.GraphMLElement import GraphMLElement
from api.src.GraphMLGenerator.GraphML.graph.common import Desc, ID
from api.src.GraphMLGenerator.GraphML.graph.common.NMTOKEN import NMTOKEN


class EndpointType(Enum):
    IN = "in"
    OUT = "out"
    UNDIR = "undir"


class Endpoint(GraphMLElement):
    """
    Representa un elemento `<endpoint>` en GraphML.
    """

    def __init__(
            self,
            node_id: ID,
            desc: Optional[Desc] = None,
            port: Optional[str] = None,
            endpoint_type: EndpointType = EndpointType.UNDIR,
    ):
        """
        Inicializa un punto final.

        Args:
            node_id (ID): Nodo al que está conectado el punto final.
            port (Optional[str]): Puerto del nodo al que está conectado.
            endpoint_type (str): Tipo de conexión ("in", "out", "undir").
            desc (Optional[Desc]): Descripción opcional del punto final.
        """
        super().__init__(desc)
        self.node_id = node_id
        self.__port = None
        self.port = port
        self.endpoint_type = endpoint_type

    @property
    def port(self) -> Optional[str]:
        """
        Obtiene el puerto del punto final.

        Returns:
            Optional[str]: Puerto del punto final.
        """
        return self.__port

    @NMTOKEN
    @port.setter
    def port(self, port: Optional[str]) -> None:
        """
        Establece el puerto del punto final.

        Args:
            port (Optional[str]): Puerto del punto final.
        """
        self.__port = port

    def to_xml(self) -> str:
        """
        Convierte el punto final a su representación XML.

        Returns:
            str: Representación XML del punto final.
        """
        desc_xml = f"<desc>{self.desc}</desc>" if self.desc else ""
        attributes = f'node="{self.node_id}" type="{self.endpoint_type.value}" '
        if self.port:
            attributes += f'port="{self.port}" '

        return f"<endpoint {attributes}>{desc_xml}</endpoint>"
