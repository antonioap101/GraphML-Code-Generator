from typing import List, Optional

from GraphML.GraphMLContainer import GraphMLContainer
from GraphML.common.Desc import Desc
from GraphML.common.ID import ID, IDType
from GraphML.graph.elements import Data
from GraphML.graph.elements.Edge import Edge
from GraphML.graph.elements.Node import Node
from GraphML.graph.elements.external.Locator import Locator
from GraphML.graph.elements.hyperedges.HyperEdge import HyperEdge


class Graph(GraphMLContainer):
    """
    Representa un elemento `<graph>` dentro de GraphML.
    """

    def __init__(
            self,
            graph_id: ID = ID.autogenerate(IDType.GRAPH),
            edge_default: str = "directed",
            desc: Optional[Desc] = None,
            extra_attrib: Optional[dict] = None,
    ):
        """
        Inicializa un grafo.

        Args:
            graph_id (str): Identificador único para el grafo.
            edge_default (str): Indica si las aristas son dirigidas o no (por defecto, "directed").
            desc (Optional[Desc]): Descripción opcional para el grafo.
            extra_attrib (Optional[dict]): Atributos personalizados adicionales.
        """
        super().__init__(desc=desc, extra_attrib=extra_attrib)
        self.graph_id = graph_id
        self.edge_default = edge_default
        self.data_elements: List[Data] = []
        self.nodes: List[Node] = []
        self.edges: List[Edge] = []
        self.hyperedges: List[HyperEdge] = []
        self.locators: List[Locator] = []

    @property
    def keys(self):
        return [data.key for data in self.data_elements] + [data.key for element in self.nodes + self.edges for data in element.data_elements]

    def add_data(self, data: Data):
        """Añade un elemento `<data>`."""
        self.data_elements.append(data)

    def add_node(self, node: Node) -> "Graph":
        """Añade un elemento `<node>`."""
        self.nodes.append(node)
        return self

    def add_nodes(self, nodes: List[Node]) -> "Graph":
        """Añade una lista de elementos `<node>`."""
        self.nodes.extend(nodes)
        return self

    def add_edge(self, edge: Edge) -> "Graph":
        """Añade un elemento `<edge>`."""
        self.edges.append(edge)
        return self

    def add_hyperedge(self, hyperedge: HyperEdge) -> "Graph":
        """Añade un elemento `<hyperedge>`."""
        self.hyperedges.append(hyperedge)
        return self

    def add_locator(self, locator: Locator) -> "Graph":
        """Añade un elemento `<locator>`."""
        self.locators.append(locator)
        return self

    def to_xml(self) -> str:
        """
        Convierte el grafo a su representación XML.

        Returns:
            str: Representación XML del grafo.
        """
        desc_xml = self.desc.to_xml() if self.desc else ""
        extra_attrib = self.render_attributes()
        attributes = f'id="{self.graph_id}" edgedefault="{self.edge_default}"' + (f" {extra_attrib}" if extra_attrib else "")
        data_xml = "".join(data.to_xml() for data in self.data_elements)
        nodes_xml = "".join(node.to_xml() for node in self.nodes)
        edges_xml = "".join(edge.to_xml() for edge in self.edges)
        hyperedges_xml = "".join(hyperedge.to_xml() for hyperedge in self.hyperedges)
        locators_xml = "".join(locator.to_xml() for locator in self.locators)

        return (
                f"<graph" + (f" {attributes}" if attributes else "") + ">" +
                f"{desc_xml}" +
                f"{data_xml}" +
                f"{nodes_xml}" +
                f"{edges_xml}" +
                f"{hyperedges_xml}" +
                f"{locators_xml}" +
                f"</graph>"
        )
