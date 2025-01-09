from abc import ABC, abstractmethod
from typing import List

from backend.core.graphml.src.tokens.Token import Token
from backend.core.graphml.src.utils.file_handler import FileHandler


class Parser(ABC):
    """Interfaz común para parsers de distintos formatos."""

    @staticmethod
    @abstractmethod
    def parse(content: str) -> List[Token]:
        """Convierte un contenido en un diccionario."""
        pass

    @classmethod
    def parse_from_file(cls, filepath: str) -> List[Token]:
        """Lee un archivo y lo parsea utilizando el método `parse`."""
        file = FileHandler.read_file(filepath)
        return cls.parse(file.content)
