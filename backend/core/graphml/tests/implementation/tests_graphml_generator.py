import unittest

from backend.core.graphml.src.GraphMLGenerator import GraphMLGenerator


class TestGraphMLGenerator(unittest.TestCase):

    def test_valid_xml_basic(self):
        """Prueba con un XML básico y válido."""
        xml_content = """
        <root>
            <node id="1">
                <child>Hello, World!</child>
            </node>
        </root>
        """
        graphml = GraphMLGenerator.from_string(xml_content, "xml")
        graphml_string = GraphMLGenerator.to_string(graphml)
        self.assertIn("<node id=", graphml_string)
        self.assertIn("Hello, World!", graphml_string)

    def test_valid_xml_with_attributes(self):
        """Prueba con un XML más complejo con múltiples nodos y atributos."""
        xml_content = """
        <root>
            <node id="1" type="start">
                <child id="2">Start Node</child>
            </node>
            <node id="3" type="end">
                <child id="4">End Node</child>
            </node>
        </root>
        """
        graphml = GraphMLGenerator.from_string(xml_content, "xml")
        graphml_string = GraphMLGenerator.to_string(graphml)
        print("GraphML string:", graphml_string)
        self.assertIn("\'type\': \'start\'", graphml_string)
        self.assertIn("<node id=\"n4\"", graphml_string)

    def test_invalid_xml_malformed(self):
        """Prueba con un XML malformado."""
        xml_content = """
        <root>
            <node id="1">
                <child>Hello, World!
            </node>
        """
        with self.assertRaises(Exception):
            GraphMLGenerator.from_string(xml_content, "xml")


if __name__ == "__main__":
    unittest.main()
