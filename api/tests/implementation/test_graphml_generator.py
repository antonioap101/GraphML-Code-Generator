import unittest

from api.src.GraphMLGenerator.GraphMLGenerator import GraphMLGenerator


class TestGraphMLGenerator(unittest.TestCase):
    def test_generate_simple_graph(self):
        data = {
            "node1": {},
            "node2": {}
        }
        result = GraphMLGenerator.generate(data)
        self.assertIn('<node id="n0"><data key="label">node1</data></node>', result)
        self.assertIn('<node id="n1"><data key="label">node2</data></node>', result)
        self.assertTrue(result.startswith('<?xml version="1.0" encoding="UTF-8"?>'))
        self.assertTrue(result.endswith('</graphml>'))

    def test_generate_empty_graph(self):
        data = {}
        result = GraphMLGenerator.generate(data)
        self.assertNotIn('<node', result)  # No debe haber nodos
        self.assertTrue(result.startswith('<?xml version="1.0" encoding="UTF-8"?>'))
        self.assertTrue(result.endswith('</graphml>'))
