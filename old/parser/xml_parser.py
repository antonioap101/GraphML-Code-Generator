import xml.etree.ElementTree as ET

from old.node.node import Node
from old.parser.parser import Parser


class XMLParser(Parser):
    """Parser para convertir XML a una estructura de nodos."""

    @staticmethod
    def parse(content: str) -> Node:
        """
        Convierte el XML a un árbol de nodos.

        Args:
            content (str): Contenido del archivo XML como cadena.

        Returns:
            Node: Nodo raíz del árbol generado.
        """
        try:
            root_element: ET.Element = ET.fromstring(content)
            return XMLParser._element_to_node(root_element)
        except ET.ParseError as e:
            raise ValueError(f"Error al parsear XML: {e}")

    @staticmethod
    def _element_to_node(element: ET.Element) -> Node:
        """
        Convierte un elemento de ElementTree en un nodo.

        Args:
            element (ET.Element): Elemento XML a convertir.

        Returns:
            Node: Nodo correspondiente al elemento.
        """
        # Crear el nodo actual
        node = Node(tag=element.tag, attributes=element.attrib, text=element.text)

        # Añadir hijos al nodo actual
        for child in element:
            node.add_child(XMLParser._element_to_node(child))

        return node
