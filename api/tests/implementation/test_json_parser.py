import unittest

from api.src.GraphMLGenerator.parser.json_parser.json_parser import JSONParser


class TestJSONParser(unittest.TestCase):

    def test_valid_json(self):
        content = """
        {
          "tag": "graph",
          "attrib": { "type": "directed" },
          "text": "Graph content",
          "tail": null,
          "children": [
            {
              "tag": "node",
              "attrib": { "id": "n1" },
              "text": "Node 1",
              "tail": null,
              "children": []
            },
            {
              "tag": "node",
              "attrib": { "id": "n2" },
              "text": "Node 2",
              "tail": null,
              "children": []
            }
          ]
        }
        """
        tokens = JSONParser.parse(content)
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].tag, "graph")
        self.assertEqual(tokens[0].children[0].tag, "node")
        self.assertEqual(tokens[0].children[0].attrib["id"], "n1")

    def test_invalid_json(self):
        invalid_content = """
        {
          "tag": "graph",
          "attrib": { "type": "directed" },
          "text": "Graph content",
          "children": [
            {
              "tag": "node",
              "attrib": "invalid"
            }
          ]
        """
        with self.assertRaises(ValueError) as context:
            JSONParser.parse(invalid_content)
