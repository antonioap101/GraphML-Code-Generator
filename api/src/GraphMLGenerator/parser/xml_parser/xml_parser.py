import xml.etree.ElementTree as ET
from typing import List

from api.src.GraphMLGenerator.parser.parser import Parser
from api.src.GraphMLGenerator.tokens.Token import Token


class XMLParser(Parser):
    """Parser para convertir XML a una lista de Tokens."""

    @staticmethod
    def parse(content: str) -> List[Token]:
        """
        Convierte el XML a una lista de tokens.

        Args:
            content (str): Contenido del archivo XML como cadena.

        Returns:
            List[Token]: Lista de tokens generados a partir del XML.
        """
        try:
            root_element = ET.fromstring(content)
            return XMLParser._element_to_tokens(root_element)
        except ET.ParseError as e:
            raise ValueError(f"Error al parsear XML: {e}")

    @staticmethod
    def _element_to_tokens(element: ET.Element) -> List[Token]:
        """
        Convierte un elemento XML a una lista de Tokens.

        Args:
            element (ET.Element): Elemento XML a convertir.

        Returns:
            List[Token]: Lista de tokens generados a partir del elemento.
        """
        token = Token(
            tag=element.tag,
            attrib=element.attrib,
            text=element.text.strip() if element.text else None,
            tail=element.tail.strip() if element.tail else None,
            children=[XMLParser._element_to_tokens(child)[0] for child in element]
        )
        return [token]
