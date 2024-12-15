import unittest
from pathlib import Path

from api.src.GraphMLGenerator.parser.xml.xml_parser import XMLParser


class TestXMLParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Descubrir la raíz del proyecto dinámicamente
        cls.project_root = Path(__file__).resolve().parent.parent.parent
        cls.examples_dir = f"{cls.project_root}/examples"

    def test_parse_valid_xml(self):
        content = "<root><child key='value'>Text</child></root>"
        result = XMLParser.parse(content)
        expected = {
            "root": {
                "attributes": {},
                "children": [{
                    "child": {
                        "attributes": {"key": "value"},
                        "children": [],
                        "text": "Text",
                    }
                }],
                "text": None,
            }
        }
        self.assertEqual(result, expected)

    def test_parse_invalid_xml(self):
        content = "<root><child key='value'>Text</child>"
        with self.assertRaises(ValueError):
            XMLParser.parse(content)

    def test_parse_xml_file(self):
        content = XMLParser.parse_from_file(f"{self.examples_dir}/example.xml")
        expected = {
            "root": {
                "attributes": {},
                "children": [{
                    "node1": {
                        "attributes": {"attribute1": "value1", "attribute2": "value2"},
                        "children": [
                            {
                                "subnode1": {
                                    "attributes": {"attribute3": "value3"},
                                    "children": [],
                                    "text": None,
                                }
                            },
                            {
                                "subnode2": {
                                    "attributes": {"attribute4": "value4"},
                                    "children": [],
                                    "text": None,
                                }
                            }
                        ],
                        "text": None,
                    }
                }, {
                    "node2": {
                        "attributes": {"attribute5": "value5"},
                        "children": [],
                        "text": None,
                    }
                }],
                "text": None
            }
        }
        self.assertEqual(content, expected)
