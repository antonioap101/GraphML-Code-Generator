from typing import List, Optional

from GraphML.GraphMLContainer import GraphMLContainer
from GraphML.common.Desc import Desc
from GraphML.graph.Graph import Graph
from GraphML.graph.elements.Data import Data
from GraphML.graph.elements.Key import Key


class GraphML(GraphMLContainer):
    """
    Representa el elemento raíz `<graphml>` en un archivo GraphML.
    """

    def __init__(
            self,
            graphs: List[Graph] = None,
            desc: Optional[Desc] = None,
            extra_attrib: Optional[dict] = None,
    ):
        """
        Inicializa el elemento raíz GraphML.

        Args:
            desc (Optional[Desc]): Descripción opcional para el archivo GraphML.
            extra_attrib (Optional[dict]): Atributos personalizados adicionales.
        """
        super().__init__(desc=desc, extra_attrib=extra_attrib)
        self.graphs: List[Graph] = graphs or []
        self.keys: List[Key] = []
        self.data_elements: List[Data] = []

    def add_key(self, key: Key):
        """Añade un elemento `<key>`."""
        self.keys.append(key)

    def add_graph(self, graph: Graph):
        """Añade un elemento `<graph>`."""
        self.graphs.append(graph)
        # Add all keys from the graph to the list of keys
        self.keys.extend(graph.keys)

    def add_data(self, data: Data):
        """Añade un elemento `<data>`."""
        self.data_elements.append(data)

    def to_xml(self) -> str:
        """
        Convierte el elemento GraphML a su representación XML.

        Returns:
            str: Representación XML del archivo GraphML.
        """
        desc_xml = self.desc.to_xml() if self.desc else ""
        attributes = self.render_attributes()
        keys_xml = "".join(key.to_xml() for key in self.keys)
        graphs_xml = "".join(graph.to_xml() for graph in self.graphs)
        data_xml = "".join(data.to_xml() for data in self.data_elements)

        return (
                f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>" +
                f"<graphml" + (f" {attributes}" if attributes else "") + ">" +
                f"{desc_xml}" +
                f"{keys_xml}" +
                f"{data_xml}" +
                f"{graphs_xml}" +
                f"</graphml>"
        )
