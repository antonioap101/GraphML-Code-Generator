from typing import List, Optional, Set

from backend.core.graphml.src.GraphML.GraphMLElement import GraphMLElement
from backend.core.graphml.src.GraphML.graph.common.Desc import Desc
from backend.core.graphml.src.GraphML.graph.elements.data.Data import Data
from backend.core.graphml.src.GraphML.graph.elements.key.Key import Key
from backend.core.graphml.src.GraphML.graph.Graph import Graph


# FIXME: Must make sure IDs are unique for each element that has an ID attribute
class GraphML(GraphMLElement):
    """
    Representa el elemento raíz `<graphml>` en un archivo GraphML.
    """

    def __init__(
            self,
            graphs: List[Graph] = None,
            desc: Desc = None,
    ):
        """
        Inicializa el elemento raíz GraphML.

        Args:
            desc (Optional[Desc]): Descripción opcional para el archivo GraphML.
        """
        super().__init__(desc=desc)
        self.graphs: List[Graph] = []
        self.keys: Set[Key] = set()  # Usamos un conjunto para las claves
        self.data_elements: List[Data] = []
        if graphs:
            self.add_graphs(graphs)

    def add_key(self, key: Key) -> "GraphML":
        """Añade un elemento `<key>` solo si su ID es único."""
        self.keys.add(key)
        return self

    def add_graph(self, graph: Graph) -> "GraphML":
        """Añade un elemento `<graph>`."""
        self.graphs.append(graph)
        # Añade todas las claves del gráfico, verificando unicidad
        for key in graph.keys:
            self.add_key(key)
        return self

    def add_graphs(self, graphs: List[Graph]) -> "GraphML":
        """Añade varios elementos `<graph>`."""
        for graph in graphs:
            self.add_graph(graph)
        return self

    def add_data(self, data: Data) -> "GraphML":
        """Añade un elemento `<data>`."""
        self.data_elements.append(data)
        return self

    def to_xml(self) -> str:
        """
        Convierte el elemento GraphML a su representación XML.

        Returns:
            str: Representación XML del archivo GraphML.
        """
        desc_xml = self.desc.to_xml() if self.desc else ""
        keys_xml = "".join(key.to_xml() for key in self.keys)
        graphs_xml = "".join(graph.to_xml() for graph in self.graphs)
        data_xml = "".join(data.to_xml() for data in self.data_elements)

        return (
                f"<?xml_parser version=\"1.0\" encoding=\"UTF-8\"?>" +
                f'<graphml xmlns="http://graphml.graphdrawing.org/xmlns">' +
                f"{desc_xml}" +
                f"{keys_xml}" +
                f"{data_xml}" +
                f"{graphs_xml}" +
                f"</graphml>"
        )
