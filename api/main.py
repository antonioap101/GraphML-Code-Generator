from api.src.GraphMLGenerator.GraphMLGenerator import GraphMLGenerator

if __name__ == "__main__":
    xml_content = """
    <root>
        <node1 attribute="value">
            <child1 />
        </node1>
    </root>
    """

    # Convertir la cadena XML a un objeto GraphML
    graphml = GraphMLGenerator.from_xml(xml_content)

    # Obtener el XML generado como texto
    graphml_string = GraphMLGenerator.to_string(graphml)
    print(graphml_string)
