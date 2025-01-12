from enum import Enum
from typing import ClassVar, Dict


class IDType(Enum):
    """
    Enumeración para los tipos de elementos con IDs en GraphML.
    """
    NODE = "node"
    EDGE = "edge"
    GRAPH = "graph"
    HYPEREDGE = "hyperedge"
    KEY = "key"


class ID:
    """
    Generador de IDs únicos para elementos GraphML.
    """

    # Contadores compartidos entre todas las instancias
    counters: ClassVar[Dict[IDType, int]] = {id_type: 0 for id_type in IDType}

    def __init__(self, value: str):
        """
        Inicializa un ID.

        Args:
            value (str): Valor del ID.
        """
        self.value = value

    @staticmethod
    def autogenerate(element_type: IDType) -> 'ID':
        """
        Genera automáticamente un ID único para un tipo de elemento.

        Args:
            element_type (IDType): Tipo de elemento para el que se genera el ID.

        Returns:
            ID: Instancia de ID generada automáticamente.
        """

        if element_type not in ID.counters:
            raise ValueError(f"Tipo de elemento desconocido: {element_type}")

        ID.counters[element_type] += 1
        return ID(f"{element_type.value[0]}{ID.counters[element_type]}")

    def __str__(self) -> str:
        """
        Representa el ID como una cadena.

        Returns:
            str: Valor del ID.
        """
        return self.value

    def __eq__(self, other):
        if not isinstance(other, ID):
            return False
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.value)