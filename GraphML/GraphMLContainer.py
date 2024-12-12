from typing import Optional, List

from GraphML.GraphMLElement import GraphMLElement
from GraphML.graph.common import Desc


class GraphMLContainer(GraphMLElement):
    """
    Clase base para elementos que pueden contener otros elementos en GraphML.
    """

    def __init__(self, desc: Optional[Desc] = None, children: Optional[List[GraphMLElement]] = None):
        """
        Inicializa un contenedor GraphML.

        Args:
            desc (Optional[Desc]): Descripción opcional para el elemento.
        """
        super().__init__(desc)
        self.children: List[GraphMLElement] = children or []

    def add_child(self, child: GraphMLElement):
        """
        Añade un hijo al contenedor.

        Args:
            child (GraphMLElement): Elemento hijo a añadir.
        """
        self.children.append(child)

    def to_xml(self) -> str:
        """
        Convierte el contenedor y sus hijos a su representación XML.

        Returns:
            str: Representación XML del contenedor.
        """
        children_xml = "".join(child.to_xml() for child in self.children)
        desc_xml = self.desc.to_xml() if self.desc else ""
        return f"{desc_xml}{children_xml}"
