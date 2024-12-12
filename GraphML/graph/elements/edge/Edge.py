from typing import Optional, List

from GraphML.GraphMLElement import GraphMLElement
from GraphML.graph.common import Desc
from GraphML.graph.common.ID import ID, IDType
from GraphML.graph.elements.data.Data import Data
from GraphML.graph.elements.port.Port import Port


class Edge(GraphMLElement):
    """
    Representa un elemento `<edge>` en un grafo de GraphML.
    <!ELEMENT edge (desc?,data*,graph?)>
    <!ATTLIST edge
              id         ID           #IMPLIED
              source     IDREF        #REQUIRED
              sourceport NMTOKEN      #IMPLIED
              target     IDREF        #REQUIRED
              targetport NMTOKEN      #IMPLIED
              directed   (true|false) #IMPLIED
    >
    """

    def __init__(
            self,
            source: ID,
            target: ID,
            edge_id: ID = ID.autogenerate(IDType.EDGE),
            source_port: Port = None,
            target_port: Port = None,
            directed: Optional[bool] = None,
            desc: Desc = None,
            data_elements: List[Data] = [],
    ):
        """
        Inicializa una arista.

        Args:
            source (ID): Nodo origen de la arista.
            target (ID): Nodo destino de la arista.
            edge_id (Optional[ID]): Identificador único para la arista.
            source_port (Optional[Port]): Puerto de origen de la arista.
            target_port (Optional[Port]): Puerto de destino de la arista.
            directed (Optional[bool]): Indica si la arista es dirigida (por defecto, sigue la configuración del grafo).
            desc (Optional[Desc]): Descripción opcional de la arista.
        """
        super().__init__(desc)
        self.edge_id = edge_id
        self.source = source
        self.target = target
        self.source_port = source_port
        self.target_port = target_port
        self.directed = directed
        self.data_elements = data_elements

    def to_xml(self) -> str:
        """
        Convierte la arista a su representación XML.

        Returns:
            str: Representación XML de la arista.
        """
        desc_xml = f"<desc>{self.desc}</desc>" if self.desc else ""

        attributes = f'id="{self.edge_id}"'
        attributes += f' source="{self.source}" target="{self.target}"'
        attributes += f' sourceport="{self.source_port}"' if self.source_port else ""
        attributes += f' targetport="{self.target_port}"' if self.target_port else ""
        attributes += f' directed="{str(self.directed).lower()}"' if self.directed is not None else ""

        return (
                f"<edge {attributes}>" +
                f"{desc_xml}" +
                f"</edge>"
        )
