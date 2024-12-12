from abc import ABC, abstractmethod

from GraphML.graph.elements.node.Node import Node
from old.utils.file_handler import FileHandler


class Parser(ABC):
    """Interfaz común para parsers de distintos formatos."""

    @staticmethod
    @abstractmethod
    def parse(content: str) -> Node:
        """Convierte un contenido en un diccionario."""
        pass

    @classmethod
    def parse_from_file(cls, filepath: str) -> Node:
        """Lee un archivo y lo parsea utilizando el método `parse`."""
        content = FileHandler.read_file(filepath)
        return cls.parse(content)
