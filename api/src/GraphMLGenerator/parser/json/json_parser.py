import json

from api.src.GraphMLGenerator.parser.parser import Parser


class JSONParser(Parser):
    """Parser para convertir JSON a un diccionario."""

    @staticmethod
    def parse(content: str) -> dict:
        """Convierte JSON en un diccionario."""
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al parsear JSON: {e}")
