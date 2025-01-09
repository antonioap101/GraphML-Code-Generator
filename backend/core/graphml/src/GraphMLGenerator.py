from typing import List, Optional

from backend.core.graphml.src.GraphML.GraphML import GraphML
from backend.core.graphml.src.GraphML.formatter.XMLFormatter import XMLFormatter
from backend.core.graphml.src.GraphML.graph.Graph import Graph

from backend.core.graphml.src.GraphML.graph.common.Desc import Desc
from backend.core.graphml.src.GraphML.graph.common.ID import ID
from backend.core.graphml.src.GraphML.graph.elements.data.Data import Data
from backend.core.graphml.src.GraphML.graph.elements.edge.Edge import Edge
from backend.core.graphml.src.GraphML.graph.elements.key.Key import Key
from backend.core.graphml.src.GraphML.graph.elements.node.Node import Node
from backend.core.graphml.src.parser.json_parser.json_parser import JSONParser
from backend.core.graphml.src.parser.xml_parser.xml_parser import XMLParser
from backend.core.graphml.src.tokens.Token import Token
from backend.core.graphml.src.utils.file import File
from backend.core.graphml.src.utils.file_handler import FileHandler


class GraphMLGenerator:
    """
    Clase fachada para la gestión y creación de contenido GraphML.
    Permite recibir contenido XML o JSON y convertirlo a GraphML, además de exportarlo como fichero.
    """

    class TokenScanner:
        """
        Clase interna para procesar tokens y construir un objeto Graph.
        """

        @staticmethod
        def scan(tokens: List[Token], parent_node: Optional[Node] = None, graph: Optional[Graph] = None) -> Graph:
            """
            Convierte una lista de tokens en un objeto Graph.

            Args:
                tokens (List[Token]): Lista de tokens generados por un parser.
                parent_node (Optional[Node]): Nodo padre al que se conectarán los nodos actuales.
                graph (Optional[Graph]): Grafo al que se añadirán los nodos y aristas.

            Returns:
                Graph: Grafo construido a partir de los tokens.
            """
            if graph is None:
                graph = Graph()

            for token in tokens:
                # Crear un nodo para el token actual
                current_node = Node(desc=Desc(content=token.tag))

                if token.attrib:
                    current_node.add_data(Data(key=Key.for_node(ID("attributes")), pcdata=token.attrib))
                if token.text:
                    current_node.add_data(Data(key=Key.for_node(ID("text")), pcdata=token.text))
                if token.tail:
                    current_node.add_data(Data(key=Key.for_node(ID("tail")), pcdata=token.tail))

                graph.add_node(current_node)

                # Si hay un nodo padre, crear una arista entre el padre y el nodo actual
                if parent_node:
                    edge = Edge(source=parent_node.node_id, target=current_node.node_id)
                    graph.add_edge(edge)

                # Procesar los hijos recursivamente
                if token.children:
                    GraphMLGenerator.TokenScanner.scan(token.children, parent_node=current_node, graph=graph)

            return graph

    parser_map = {
        "xml": XMLParser,
        "json": JSONParser
    }

    @staticmethod
    def from_tokens(tokens: List[Token]) -> GraphML:
        """
        Convierte un flujo de tokens en un objeto GraphML.

        Args:
            tokens (List[Token]): Lista de tokens generados por un parser.

        Returns:
            GraphML: Objeto GraphML generado a partir de los tokens.
        """
        graph = GraphMLGenerator.TokenScanner.scan(tokens)
        return GraphML(graphs=[graph])

    @staticmethod
    def from_file(filepath: str) -> GraphML:
        """
        Lee contenido de un archivo y lo convierte a un objeto GraphML.

        Args:
            filepath (str): Ruta del archivo.

        Returns:
            GraphML: Objeto GraphML generado a partir del archivo.
        """
        file: File = FileHandler.read_file(filepath)
        parser = GraphMLGenerator.parser_map.get(file.extension)
        if parser is None:
            raise ValueError(f"No se encontró un parser para la extensión '{file.extension}'")
        tokens = parser.parse(file.content)
        return GraphMLGenerator.from_tokens(tokens)

    @staticmethod
    def from_string(content: str, format: str) -> GraphML:
        """
        Convierte contenido en una cadena a un objeto GraphML.

        Args:
            content (str): Contenido en formato XML o JSON.
            format (str): Formato del contenido ("xml_parser" o "json_parser").

        Returns:
            GraphML: Objeto GraphML generado a partir del contenido.
        """
        parser = GraphMLGenerator.parser_map.get(format)
        if parser is None:
            raise ValueError(f"No se encontró un parser para el formato '{format}'")
        tokens = parser.parse(content)
        return GraphMLGenerator.from_tokens(tokens)

    @staticmethod
    def to_file(graphml: GraphML, output_filepath: str, format_output: bool = True) -> None:
        """
        Exporta un objeto GraphML a un archivo.

        Args:
            graphml (GraphML): Objeto GraphML a exportar.
            output_filepath (str): Ruta de salida para el archivo GraphML.
            format_output (bool): Indica si el XML debe ser formateado para legibilidad.
        """
        xml_content = graphml.to_xml()
        if format_output:
            xml_content = XMLFormatter.format(xml_content)
        FileHandler.write_file(output_filepath, xml_content)

    @staticmethod
    def to_string(graphml: GraphML, format_output: bool = True) -> str:
        """
        Convierte un objeto GraphML a una cadena XML.

        Args:
            graphml (GraphML): Objeto GraphML a convertir.
            format_output (bool): Indica si el XML debe ser formateado para legibilidad.

        Returns:
            str: Representación XML del GraphML.
        """
        xml_content = graphml.to_xml()
        return XMLFormatter.format(xml_content) if format_output else xml_content


if __name__ == "__main__":
    graphml = GraphMLGenerator.from_file("backend/examples/example.xml")

    print(graphml.to_xml())
