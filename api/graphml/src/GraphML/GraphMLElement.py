from typing import Optional

from api.graphml.src.GraphML.graph.common.Desc import Desc


class GraphMLElement:
    """
    Clase base para todos los elementos de GraphML.
    Proporciona funcionalidades comunes como descripciones y atributos personalizados.
    """

    def __init__(self, desc: Optional[Desc] = None):
        """
        Inicializa un elemento GraphML.

        Args:
            desc (Optional[Desc]): Descripción opcional para el elemento.
        """
        self.desc = desc

    def to_xml(self) -> str:
        """
        Convierte el elemento a su representación XML.
        Este método será sobrescrito por las subclases.

        Returns:
            str: Representación XML del elemento.
        """
        raise NotImplementedError("Subclases deben implementar `to_xml`.")
