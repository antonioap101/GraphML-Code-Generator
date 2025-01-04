import os

from api.graphml.src.GraphMLGenerator import GraphMLGenerator

if __name__ == "__main__":
    xml_content = """
    <root>
        <node1 attribute="value">
            <child1 />
            <child2>
                content
            </child2>
        </node1>
    </root>
    """
    # Obtener el directorio del archivo actual (main.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Directorio actual: {current_dir}")
    # Convertir la cadena XML a un objeto GraphML
    # graphml = GraphMLGenerator.from_xml(xml_content)
    graphml = GraphMLGenerator.from_file(current_dir + "/examples/example.xml_parser")

    # Obtener el XML generado como texto
    graphml_string = GraphMLGenerator.to_string(graphml=graphml, format_output=False)
    print(graphml_string)
