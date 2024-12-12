from typing import Optional

from GraphML.GraphMLElement import GraphMLElement
from GraphML.common.Desc import Desc
from GraphML.common.ID import ID


class Endpoint(GraphMLElement):
    """
    Representa un elemento `<endpoint>` en GraphML.
    """

    def __init__(
        self,
        node_id: ID,
        port: Optional[str] = None,
        endpoint_type: str = "undir",
        desc: Optional[Desc] = None,
        extra_attrib: Optional[dict] = None,
    ):
        """
        Inicializa un punto final.

        Args:
            node_id (ID): Nodo al que está conectado el punto final.
            port (Optional[str]): Puerto del nodo al que está conectado.
            endpoint_type (str): Tipo de conexión ("in", "out", "undir").
            desc (Optional[Desc]): Descripción opcional del punto final.
            extra_attrib (Optional[dict]): Atributos personalizados adicionales.
        """
        super().__init__(desc, extra_attrib)
        self.node_id = node_id
        self.port = port
        self.endpoint_type = endpoint_type

    def to_xml(self) -> str:
        """
        Convierte el punto final a su representación XML.

        Returns:
            str: Representación XML del punto final.
        """
        desc_xml = f"<desc>{self.desc}</desc>" if self.desc else ""
        attributes = f'node="{self.node_id}" type="{self.endpoint_type}" '
        if self.port:
            attributes += f'port="{self.port}" '
        attributes += self.render_attributes()

        return f"<endpoint {attributes}>{desc_xml}</endpoint>"
