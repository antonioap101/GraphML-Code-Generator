import unittest
from pathlib import Path

from old.parser.json_parser import JSONParser


class TestJSONParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Descubrir la raíz del proyecto dinámicamente
        cls.project_root = Path(__file__).resolve().parent.parent.parent
        cls.examples_dir = f"{cls.project_root}/examples"

    def test_parse_valid_json(self):
        content = '{"root": {"child": {"key": "value"}}}'
        result = JSONParser.parse(content)
        expected = {
            "root": {
                "child": {
                    "key": "value"
                }
            }
        }
        self.assertEqual(result, expected)

    def test_parse_invalid_json(self):
        content = '{"root": {"child": {"key": "value"}'  # Falta un cierre
        with self.assertRaises(ValueError):
            JSONParser.parse(content)

    # Parses from the file examples/example.json
    """
     "root": {
    "node1": {
      "attribute1": "value1",
      "attribute2": "value2",
      "children": [
        {
          "subnode1": {
            "attribute3": "value3"
          }
        },
        {
          "subnode2": {
            "attribute4": "value4"
          }
        }
      ]
    },
    "node2": {
      "attribute5": "value5"
    }
  }
    """

    def test_parse_json_file(self):
        content = JSONParser.parse_from_file(f"{self.examples_dir}/example.json")
        expected = {
            "root": {
                "node1": {
                    "attribute1": "value1",
                    "attribute2": "value2",
                    "children": [
                        {
                            "subnode1": {
                                "attribute3": "value3"
                            }
                        },
                        {
                            "subnode2": {
                                "attribute4": "value4"
                            }
                        }
                    ]
                },
                "node2": {
                    "attribute5": "value5"
                }
            }
        }
        self.assertEqual(content, expected)


if __name__ == "__main__":
    unittest.main()
