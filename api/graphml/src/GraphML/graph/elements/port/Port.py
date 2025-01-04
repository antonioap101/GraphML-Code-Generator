from typing import List, Optional

from api.graphml.src.GraphML.GraphMLElement import GraphMLElement
from api.graphml.src.GraphML.graph.common.Desc import Desc
from api.graphml.src.GraphML.graph.common.NMTOKEN import NMTOKEN
from api.graphml.src.GraphML.graph.elements.data.Data import Data


class Port(GraphMLElement):
    """
    Representa un elemento `<port>` en GraphML.
    """

    def __init__(
            self,
            port_name: str,
            desc: Desc = None,
    ):
        """
        Inicializa un puerto.

        Args:
            port_name (str): Nombre único del puerto dentro del nodo.
            desc (Optional[Desc]): Objeto `Desc` opcional para describir el puerto.
        """
        super().__init__(desc=desc)
        self.__port_name = None
        self.port_name = port_name
        self.data_elements: List[Data] = []
        self.sub_ports: List[Port] = []

    @property
    def port_name(self) -> str:
        """
        Obtiene el nombre del puerto.

        Returns:
            str: Nombre del puerto.
        """
        return self.__port_name

    @NMTOKEN
    @port_name.setter
    def port_name(self, port_name: str) -> None:
        """
        Establece el nombre del puerto.

        Args:
            port_name (str): Nombre del puerto.
        """
        self.__port_name = port_name

    def add_data(self, data: Data):
        """
        Añade un elemento de datos al puerto.

        Args:
            data (Data): Elemento de datos a añadir.
        """
        self.data_elements.append(data)

    def add_sub_port(self, sub_port: 'Port'):
        """
        Añade un sub-puerto al puerto actual.

        Args:
            sub_port (Port): Sub-puerto a añadir.
        """
        self.sub_ports.append(sub_port)

    def to_xml(self) -> str:
        """
        Convierte el puerto a su representación XML.

        Returns:
            str: Representación XML del puerto.
        """
        desc_xml = self.desc.to_xml() if self.desc else ""
        attributes = f'name="{self.port_name}"'

        # Renderizar datos y sub-puertos
        data_xml = "".join(data.to_xml() for data in self.data_elements)
        sub_ports_xml = "".join(sub_port.to_xml() for sub_port in self.sub_ports)

        return f"<port {attributes}>{desc_xml}{data_xml}{sub_ports_xml}</port>"
