from typing import Optional

from GraphML.GraphMLElement import GraphMLElement
from GraphML.graph.common import Desc
from GraphML.graph.common.ID import ID, IDType


class HyperEdge(GraphMLElement):
    """
    Representa un elemento `<hyperedge>` en GraphML.
    """

    def __init__(self, hyperedge_id: ID = ID.autogenerate(IDType.HYPEREDGE), desc: Desc = None):
        """
        Inicializa una hiper-arista.

        Args:
            hyperedge_id (Optional[str]): Identificador único para la hiper-arista.
            desc (Optional[Desc]): Descripción opcional de la hiper-arista.
        """
        super().__init__(desc)
        self.hyperedge_id = hyperedge_id

    def to_xml(self) -> str:
        """
        Convierte la hiper-arista a su representación XML.

        Returns:
            str: Representación XML de la hiper-arista.
        """
        desc_xml = f"<desc>{self.desc}</desc>" if self.desc else ""
        attributes = f'id="{self.hyperedge_id}" ' if self.hyperedge_id else ""
        children_xml = "".join(child.to_xml() for child in self.children)

        return f"<hyperedge {attributes}>{desc_xml}{children_xml}</hyperedge>"
