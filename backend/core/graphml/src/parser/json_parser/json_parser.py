import json
from typing import List

from backend.core.graphml.src.parser.parser import Parser
from backend.core.graphml.src.tokens.Token import Token


class JSONParser(Parser):
    """Parser para convertir JSON a una lista de Tokens."""

    @staticmethod
    def parse(content: str) -> List[Token]:
        """
        Convierte el contenido JSON en una lista de tokens.

        Args:
            content (str): Contenido JSON como cadena.

        Returns:
            List[Token]: Lista de tokens generados a partir del JSON.
        """
        try:
            data = json.loads(content)
            return JSONParser._json_to_tokens(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al parsear JSON: {e}")

    @staticmethod
    def _json_to_tokens(data: dict) -> List[Token]:
        """
        Convierte un diccionario JSON en una lista de Tokens.

        Args:
            data (dict): Diccionario JSON.

        Returns:
            List[Token]: Lista de tokens generados.
        """
        if not isinstance(data, dict) or "tag" not in data:
            raise ValueError("Formato JSON inválido: falta el campo 'tag'.")

        def convert_to_token(element: dict) -> Token:
            if not isinstance(element, dict) or "tag" not in element:
                raise ValueError("Formato JSON inválido: cada elemento debe tener un campo 'tag'.")
            tag = element["tag"]
            attrib = element.get("attrib", {})
            text = element.get("text", None)
            tail = element.get("tail", None)
            children = [convert_to_token(child) for child in element.get("children", [])]
            return Token(tag=tag, attrib=attrib, text=text, tail=tail, children=children)

        return [convert_to_token(data)]
