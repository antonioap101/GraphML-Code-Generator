from typing import Any, Optional

from GraphML.GraphMLElement import GraphMLElement
from GraphML.graph.elements.Key import Key


class Data(GraphMLElement):
    """
    Representa un elemento `<data>` en GraphML.
    """

    def __init__(self, key: Key, pcdata: Any, extra_attrib: Optional[dict] = None):
        """
        Inicializa un elemento de datos.

        Args:
            key (Key): Clave asociada a los datos.
            pcdata (Any): Valor de los datos (puede ser texto, números, etc.).
            extra_attrib (Optional[dict]): Atributos personalizados adicionales.
        """
        super().__init__(None, extra_attrib)
        self.key = key
        self.pcdata = pcdata

    def to_xml(self) -> str:
        """
        Convierte los datos a su representación XML.

        Returns:
            str: Representación XML de los datos.
        """
        extra_attrib_str = self.render_attributes()
        attributes = f'key="{self.key}"' + (f" {extra_attrib_str}" if extra_attrib_str else "")

        # Convertir `pcdata` a string para incluirlo en el XML
        pcdata_str = str(self.pcdata)

        # return f"<data {attributes}>{pcdata_str}</data>"
        return (
            f"<data {attributes}>"
            f"{pcdata_str}" +
            f"</data>"
        )
