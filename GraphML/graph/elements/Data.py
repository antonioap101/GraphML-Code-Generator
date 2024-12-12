from typing import Any, Optional

from GraphML.GraphMLElement import GraphMLElement
from GraphML.graph.elements.Key import Key


class Data(GraphMLElement):
    """
    Representa un elemento `<data>` en GraphML.

    <!ELEMENT data  (#PCDATA)>
    <!ATTLIST data
          key      IDREF        #REQUIRED
          id       ID           #IMPLIED
    >
    · key (required): The key specifies the kind of data entered here. The value of key must be the id of one of the key elements of graphml.
    · id (optional): An optional id for the data.
    """

    def __init__(self, key: Key, pcdata: Any):
        """
        Inicializa un elemento de datos.

        Args:
            key (Key): Clave asociada a los datos.
            pcdata (Any): Valor de los datos (puede ser texto, números, etc.).
        """
        super().__init__()
        self.key = key
        self.pcdata = pcdata

    def to_xml(self) -> str:
        """
        Convierte los datos a su representación XML.

        Returns:
            str: Representación XML de los datos.
        """

        attributes = f'key="{self.key}"'

        # Convertir `pcdata` a string para incluirlo en el XML
        pcdata_str = str(self.pcdata)

        # return f"<data {attributes}>{pcdata_str}</data>"
        return (
                f"<data {attributes}>"
                f"{pcdata_str}" +
                f"</data>"
        )
