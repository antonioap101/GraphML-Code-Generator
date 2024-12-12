from typing import List, Optional

from GraphML.GraphMLContainer import GraphMLContainer
from GraphML.common.Desc import Desc
from GraphML.graph.elements.Data import Data


class Port(GraphMLContainer):
    """
    Representa un elemento `<port>` en GraphML.
    """

    def __init__(
        self,
        port_name: str,
        desc: Optional[Desc] = None,
        extra_attrib: Optional[dict] = None,
    ):
        """
        Inicializa un puerto.

        Args:
            port_name (str): Nombre único del puerto dentro del nodo.
            desc (Optional[Desc]): Objeto `Desc` opcional para describir el puerto.
            extra_attrib (Optional[dict]): Atributos personalizados adicionales.
        """
        super().__init__(desc=desc, extra_attrib=extra_attrib)
        self.port_name = port_name
        self.data_elements: List[Data] = []
        self.sub_ports: List[Port] = []

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
        attributes = f'name="{self.port_name}" {self.render_attributes()}'

        # Renderizar datos y sub-puertos
        data_xml = "".join(data.to_xml() for data in self.data_elements)
        sub_ports_xml = "".join(sub_port.to_xml() for sub_port in self.sub_ports)

        return f"<port {attributes}>{desc_xml}{data_xml}{sub_ports_xml}</port>"
