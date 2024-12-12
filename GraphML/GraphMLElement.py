from typing import Optional

from GraphML.common.Desc import Desc


class GraphMLElement:
    """
    Clase base para todos los elementos de GraphML.
    Proporciona funcionalidades comunes como descripciones y atributos personalizados.
    """

    def __init__(self, desc: Optional[Desc] = None, extra_attrib: Optional[dict] = None):
        """
        Inicializa un elemento GraphML.

        Args:
            desc (Optional[Desc]): Descripción opcional para el elemento.
            extra_attrib (Optional[dict]): Atributos personalizados adicionales.
        """
        self.desc = desc
        self.extra_attrib = extra_attrib or {}

    def to_xml(self) -> str:
        """
        Convierte el elemento a su representación XML.
        Este método será sobrescrito por las subclases.

        Returns:
            str: Representación XML del elemento.
        """
        raise NotImplementedError("Subclases deben implementar `to_xml`.")

    def render_attributes(self) -> str:
        """
        Genera los atributos en formato XML.

        Returns:
            str: Atributos en formato XML.
        """
        return " ".join(f'{key}="{value}"' for key, value in self.extra_attrib.items())
