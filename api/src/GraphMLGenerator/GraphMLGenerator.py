from api.src.GraphMLGenerator.GraphML import GraphML
from api.src.GraphMLGenerator.GraphML.formatter.XMLFormatter import XMLFormatter
from api.src.GraphMLGenerator.parser.xml.xml_parser import XMLParser

from api.src.GraphMLGenerator.utils.file_handler import FileHandler


class GraphMLGenerator:
    """
    Clase fachada para la gestión y creación de contenido GraphML.
    Permite recibir contenido XML o JSON y convertirlo a GraphML, además de exportarlo como fichero.
    """

    @staticmethod
    def from_xml(content: str) -> GraphML:
        """
        Convierte contenido XML a un objeto GraphML.

        Args:
            content (str): Contenido del archivo XML como cadena.

        Returns:
            GraphML: Objeto GraphML generado a partir del contenido.
        """
        return XMLParser.parse(content)

    @staticmethod
    def from_file(filepath: str) -> GraphML:
        """
        Lee contenido de un archivo XML y lo convierte a un objeto GraphML.

        Args:
            filepath (str): Ruta del archivo XML.

        Returns:
            GraphML: Objeto GraphML generado a partir del archivo.
        """
        content = FileHandler.read_file(filepath)
        return GraphMLGenerator.from_xml(content)

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
