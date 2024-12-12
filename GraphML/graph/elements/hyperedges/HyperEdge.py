from typing import Optional

from GraphML.GraphMLContainer import GraphMLContainer
from GraphML.common.Desc import Desc


class HyperEdge(GraphMLContainer):
    """
    Representa un elemento `<hyperedge>` en GraphML.
    """

    def __init__(self, hyperedge_id: Optional[str] = None, desc: Optional[Desc] = None, extra_attrib: Optional[dict] = None):
        """
        Inicializa una hiper-arista.

        Args:
            hyperedge_id (Optional[str]): Identificador único para la hiper-arista.
            desc (Optional[Desc]): Descripción opcional de la hiper-arista.
            extra_attrib (Optional[dict]): Atributos personalizados adicionales.
        """
        super().__init__(desc, extra_attrib)
        self.hyperedge_id = hyperedge_id

    def to_xml(self) -> str:
        """
        Convierte la hiper-arista a su representación XML.

        Returns:
            str: Representación XML de la hiper-arista.
        """
        desc_xml = f"<desc>{self.desc}</desc>" if self.desc else ""
        attributes = f'id="{self.hyperedge_id}" ' if self.hyperedge_id else ""
        attributes += self.render_attributes()
        children_xml = "".join(child.to_xml() for child in self.children)

        return f"<hyperedge {attributes}>{desc_xml}{children_xml}</hyperedge>"
