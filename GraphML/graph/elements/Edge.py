from typing import Optional, List

from GraphML.GraphMLElement import GraphMLElement
from GraphML.common.Desc import Desc
from GraphML.common.ID import ID, IDType
from GraphML.graph.elements.Data import Data


class Edge(GraphMLElement):
    """
    Representa un elemento `<edge>` en un grafo de GraphML.
    """

    def __init__(
            self,
            source: ID,
            target: ID,
            edge_id: ID = ID.autogenerate(IDType.EDGE),
            directed: Optional[bool] = None,
            desc: Optional[Desc] = None,
            data_elements: List[Data] = [],
            extra_attrib: Optional[dict] = None,
    ):
        """
        Inicializa una arista.

        Args:
            source (ID): Nodo origen de la arista.
            target (ID): Nodo destino de la arista.
            edge_id (Optional[ID]): Identificador único para la arista.
            directed (Optional[bool]): Indica si la arista es dirigida (por defecto, sigue la configuración del grafo).
            desc (Optional[Desc]): Descripción opcional de la arista.
            extra_attrib (Optional[dict]): Atributos personalizados adicionales.
        """
        super().__init__(desc, extra_attrib)
        self.edge_id = edge_id
        self.source = source
        self.target = target
        self.directed = directed
        self.data_elements = data_elements

    def to_xml(self) -> str:
        """
        Convierte la arista a su representación XML.

        Returns:
            str: Representación XML de la arista.
        """
        desc_xml = f"<desc>{self.desc}</desc>" if self.desc else ""
        extra_attributes = self.render_attributes()
        attributes = f'id="{self.edge_id}"'
        attributes += f' source="{self.source}" target="{self.target}"'
        attributes += f' directed="{str(self.directed).lower()}"' if self.directed is not None else ""
        attributes += f" {extra_attributes}" if extra_attributes else ""

        return (
                f"<edge {attributes}>" +
                f"{desc_xml}" +
                f"</edge>"
        )
