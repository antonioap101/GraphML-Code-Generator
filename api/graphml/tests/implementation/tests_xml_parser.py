import unittest
from pathlib import Path

from api.graphml.src.parser.xml_parser.xml_parser import XMLParser


class TestXMLParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Descubrir la raíz del proyecto dinámicamente
        cls.project_root = Path(__file__).resolve().parent.parent.parent
        cls.examples_dir = f"{cls.project_root}/examples"

    def test_valid_xml(self):
        content = """
        <graph type="directed">
            <node id="n1">Node 1</node>
            <node id="n2">Node 2</node>
            <edge source="n1" target="n2">Edge from n1 to n2</edge>
        </graph>
        """
        tokens = XMLParser.parse(content)
        self.assertEqual(len(tokens), 1)
        root_token = tokens[0]

        # Root token assertions
        self.assertEqual(root_token.tag, "graph")
        self.assertEqual(root_token.attrib, {"type": "directed"})
        self.assertEqual(root_token.text, None)
        self.assertEqual(len(root_token.children), 3)

        # First child (node n1)
        child1 = root_token.children[0]
        self.assertEqual(child1.tag, "node")
        self.assertEqual(child1.attrib, {"id": "n1"})
        self.assertEqual(child1.text, "Node 1")
        self.assertEqual(len(child1.children), 0)

        # Second child (node n2)
        child2 = root_token.children[1]
        self.assertEqual(child2.tag, "node")
        self.assertEqual(child2.attrib, {"id": "n2"})
        self.assertEqual(child2.text, "Node 2")
        self.assertEqual(len(child2.children), 0)

        # Third child (edge)
        child3 = root_token.children[2]
        self.assertEqual(child3.tag, "edge")
        self.assertEqual(child3.attrib, {"source": "n1", "target": "n2"})
        self.assertEqual(child3.text, "Edge from n1 to n2")
        self.assertEqual(len(child3.children), 0)

    def test_parse_invalid_xml(self):
        content = "<root><child key='value'>Text</child>"
        with self.assertRaises(ValueError):
            XMLParser.parse(content)

    def test_invalid_xml_missing_closing_tag(self):
        content = """
           <graph type="directed">
               <node id="n1">Node 1
               <node id="n2">Node 2</node>
           </graph>
           """
        with self.assertRaises(ValueError) as context:
            XMLParser.parse(content)
        self.assertIn("Error al parsear XML", str(context.exception))

    def test_invalid_xml_no_root_element(self):
        content = """
           <?xml_parser version="1.0"?>
           <!-- This is a comment -->
           """
        with self.assertRaises(ValueError) as context:
            XMLParser.parse(content)
        self.assertIn("Error al parsear XML", str(context.exception))

    def test_valid_xml_with_nested_elements(self):
        content = """
           <root>
               <parent id="p1">
                   <child id="c1">Child 1 text</child>
                   <child id="c2">
                       <subchild id="sc1">Subchild 1 text</subchild>
                   </child>
               </parent>
           </root>
           """
        tokens = XMLParser.parse(content)
        self.assertEqual(len(tokens), 1)
        root_token = tokens[0]

        # Root token assertions
        self.assertEqual(root_token.tag, "root")
        self.assertEqual(root_token.attrib, {})
        self.assertEqual(len(root_token.children), 1)

        # Parent token
        parent = root_token.children[0]
        self.assertEqual(parent.tag, "parent")
        self.assertEqual(parent.attrib, {"id": "p1"})
        self.assertEqual(len(parent.children), 2)

        # First child
        child1 = parent.children[0]
        self.assertEqual(child1.tag, "child")
        self.assertEqual(child1.attrib, {"id": "c1"})
        self.assertEqual(child1.text, "Child 1 text")
        self.assertEqual(len(child1.children), 0)

        # Second child
        child2 = parent.children[1]
        self.assertEqual(child2.tag, "child")
        self.assertEqual(child2.attrib, {"id": "c2"})
        self.assertEqual(len(child2.children), 1)

        # Subchild
        subchild = child2.children[0]
        self.assertEqual(subchild.tag, "subchild")
        self.assertEqual(subchild.attrib, {"id": "sc1"})
        self.assertEqual(subchild.text, "Subchild 1 text")
        self.assertEqual(len(subchild.children), 0)
