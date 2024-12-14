import xml.etree.ElementTree as ET

from api.src.GraphMLGenerator.GraphML.GraphML import GraphML
from api.src.GraphMLGenerator.GraphML.formatter.XMLFormatter import XMLFormatter
from api.src.GraphMLGenerator.GraphML.graph.Graph import Graph
from api.src.GraphMLGenerator.GraphML.graph.common.Desc import Desc
from api.src.GraphMLGenerator.GraphML.graph.elements.edge.Edge import Edge
from api.src.GraphMLGenerator.GraphML.graph.elements.node.Node import Node
from api.src.GraphMLGenerator.parser.parser import Parser


class XMLParser(Parser):
    """Parser para convertir XML a una estructura de GraphML."""

    @staticmethod
    def parse(content: str) -> GraphML:
        """
        Convierte el XML a un objeto GraphML.

        Args:
            content (str): Contenido del archivo XML como cadena.

        Returns:
            GraphML: Objeto GraphML generado a partir del XML.
        """
        try:
            root_element: ET.Element = ET.fromstring(content)
            # Print the whole XML tree
            print("XML tree:")  # , ET.tostring(root_element, encoding="unicode"))
            for elem in root_element.iter():
                print("ELEM: ", elem.tag, "ATTRIB: ", elem.attrib, "TEXT:", elem.text.strip() if elem.text else "", "TAIL:",
                      elem.tail.strip() if elem.tail else "")
            graph = XMLParser._elements_to_graph(root_element)
            return GraphML(graphs=[graph])
        except ET.ParseError as e:
            raise ValueError(f"Error al parsear XML: {e}")

    @staticmethod
    def _elements_to_graph(element: ET.Element, parent_node: Node = None, graph: Graph = None) -> Graph:
        """
        Convierte un elemento de ElementTree en un grafo.

        Args:
            element (ET.Element): Elemento XML a convertir.
            parent_node (Optional[Node]): Nodo padre al que se conectará el nodo actual.
            graph (Optional[Graph]): Grafo al que se añadirán los nodos y aristas.

        Returns:
            Graph: Grafo construido a partir del XML.
        """
        if graph is None:
            graph = Graph()

        # Crear un nodo para el elemento actual
        current_node = Node(desc=Desc(content=element.tag))
        graph.add_node(current_node)

        # Si hay un nodo padre, crear una arista entre el padre y el nodo actual
        if parent_node:
            edge = Edge(source=parent_node.node_id, target=current_node.node_id)
            graph.add_edge(edge)

        # Procesar los hijos recursivamente
        for child in element:
            XMLParser._elements_to_graph(child, parent_node=current_node, graph=graph)

        return graph


if __name__ == "__main__":
    # Pasar argumentos de prueba si es necesario

    graphml = XMLParser.parse_from_file("../../examples/example.xml")
    print(XMLFormatter.format(graphml.to_xml()))
