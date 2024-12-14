from enum import Enum
from typing import Optional

from api.src.GraphMLGenerator.GraphML.GraphMLElement import GraphMLElement
from api.src.GraphMLGenerator.GraphML.graph.common import Desc
from api.src.GraphMLGenerator.GraphML.graph.common.ID import ID, IDType


class ForType(Enum):
    GRAPH = "graph"
    NODE = "node"
    EDGE = "edge"
    HYPEREDGE = "hyperedge"
    PORT = "port"
    ENDPOINT = "endpoint"
    ALL = "all"


class Key(GraphMLElement):
    """
    Representa un elemento `<key>` en GraphML.
    """

    def __init__(
            self,
            key_id: ID = None,
            for_type: ForType = ForType.ALL,
            desc: Desc = None,
            default_value: Optional[str] = None,
    ):
        """
        Inicializa un elemento de clave.

        Args:
            key_id (ID): Identificador único para la clave.
            for_type (str): Dominio de definición de la clave (por defecto, "all").
            desc (Optional[Desc]): Descripción opcional de la clave.
            default_value (Optional[str]): Valor por defecto para esta clave.
        """
        super().__init__(desc)
        self.key_id = key_id if key_id else ID.autogenerate(IDType.KEY)
        self.for_type = for_type
        self.default_value = default_value

    def to_xml(self) -> str:
        """
        Convierte la clave a su representación XML.

        Returns:
            str: Representación XML de la clave.
        """
        desc_xml = f"<desc>{self.desc}</desc>" if self.desc else ""
        default_xml = f"<default>{self.default_value}</default>" if self.default_value else ""

        attributes = f'id="{self.key_id}" for="{self.for_type.value}"'

        return (
                f"<key {attributes}>" +
                f"{desc_xml}" +
                f"{default_xml}" +
                f"</key>"
        )

    def __str__(self):
        return f"{self.key_id}"
