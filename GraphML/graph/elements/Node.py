from typing import List, Optional

from GraphML.GraphMLContainer import GraphMLContainer
from GraphML.common.Desc import Desc
from GraphML.common.ID import ID, IDType
from GraphML.graph.elements.Data import Data
from GraphML.graph.elements.Port import Port
from GraphML.graph.elements.external.Locator import Locator


class Node(GraphMLContainer):
    """
    Representa un elemento `<node>` dentro de un grafo en GraphML.
    <!ELEMENT node (desc?,(((data|port)*,graph?)|locator))>
    <!ATTLIST node id ID #REQUIRED>
    """

    def __init__(
            self,
            node_id: ID = ID.autogenerate(IDType.NODE),
            desc: Optional[Desc] = None,
            extra_attrib: Optional[dict] = None,
    ):
        """
        Inicializa un nodo.

        Args:
            node_id (ID): Identificador único para el nodo.
            desc (Optional[Desc]): Objeto `Desc` opcional para describir el nodo.
            extra_attrib (Optional[dict]): Atributos personalizados adicionales.
        """
        from GraphML.graph.Graph import Graph  # Evitar dependencia circular
        super().__init__(desc=desc, extra_attrib=extra_attrib)
        self.node_id = node_id
        self.data_elements: List[Data] = []
        self.ports: List[Port] = []
        self.graph: Optional[Graph] = None
        self.locator: Optional[Locator] = None

    def add_data(self, data: Data) -> "Node":
        """
        Añade un elemento `<data>` al nodo.

        Args:
            data (Data): Elemento `Data` a añadir.
        """
        self.data_elements.append(data)
        return self

    def add_port(self, port: Port) -> "Node":
        """
        Añade un elemento `<port>` al nodo.

        Args:
            port (Port): Elemento `Port` a añadir.
        """
        self.ports.append(port)
        return self

    def set_graph(self, graph: "Graph") -> "Node":
        """
        Asigna un subgrafo al nodo. No puede coexistir con un `locator`.

        Args:
            graph (Graph): Subgrafo a asignar.
        """
        if self.locator:
            raise ValueError("Un nodo no puede tener un subgrafo y un locator al mismo tiempo.")
        self.graph = graph
        return self

    def set_locator(self, locator: Locator) -> "Node":
        """
        Asigna un locator al nodo. No puede coexistir con un subgrafo.

        Args:
            locator (Locator): Locator a asignar.
        """
        if self.graph or (self.ports or self.data_elements):
            raise ValueError("Un nodo no puede tener un locator y un subgrafo al mismo tiempo.")
        self.locator = locator
        return self

    def to_xml(self) -> str:
        """
        Convierte el nodo a su representación XML.

        Returns:
            str: Representación XML del nodo.
        """
        desc_xml = self.desc.to_xml() if self.desc else ""
        extra_attrib = self.render_attributes()
        attributes = f'id="{self.node_id}"' + (f" {extra_attrib}" if extra_attrib else "")

        # Renderizar elementos contenidos
        data_xml = "".join(data.to_xml() for data in self.data_elements)
        ports_xml = "".join(port.to_xml() for port in self.ports)
        graph_or_locator_xml = self.graph.to_xml() if self.graph else self.locator.to_xml() if self.locator else ""

        return (
                f"<node {attributes}>"
                f"{desc_xml}" +
                f"{data_xml}" +
                f"{ports_xml}" +
                f"{graph_or_locator_xml}" +
                f"</node>"
        )
