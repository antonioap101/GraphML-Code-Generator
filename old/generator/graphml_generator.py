from old.node.node import Node


class GraphMLGenerator:
    """Clase para generar GraphML a partir de un árbol de nodos."""

    @staticmethod
    def generate(root: Node) -> str:
        """
        Genera GraphML basado en la estructura del árbol de nodos.

        Args:
            root (Node): Nodo raíz del árbol generado por el parser.

        Returns:
            str: Contenido en formato GraphML.
        """
        graphml = ['<?xml version="1.0" encoding="UTF-8"?>']
        graphml.append('<graphml xmlns="http://graphml.graphdrawing.org/xmlns">')
        graphml.append('<graph id="G" edgedefault="directed">')

        nodes = []
        edges = []
        GraphMLGenerator._traverse_tree(root, nodes, edges)

        graphml.extend(nodes)
        graphml.extend(edges)

        graphml.append('</graph>')
        graphml.append('</graphml>')

        return "".join(graphml)

    @staticmethod
    def _traverse_tree(node: Node, nodes: list, edges: list, parent_id: str = None, node_id_counter: dict = None):
        """
        Recorre el árbol de nodos y genera nodos y aristas para GraphML.

        Args:
            node (Node): Nodo actual a procesar.
            nodes (list): Lista acumulativa de nodos en formato GraphML.
            edges (list): Lista acumulativa de aristas en formato GraphML.
            parent_id (ID): ID del nodo padre.
            node_id_counter (dict): Contador para asignar IDs únicos a los nodos.
        """
        if node_id_counter is None:
            node_id_counter = {"current_id": 0}

        # Asignar un ID único al nodo actual
        node_id = f"n{node_id_counter['current_id']}"
        node_id_counter["current_id"] += 1

        # Crear nodo en GraphML
        attributes = " ".join(f'{key}="{value}"' for key, value in node.attributes.items())
        label = f"{node.tag}" if not attributes else f"{node.tag} ({attributes})"
        nodes.append(f'<node id="{node_id}"><data key="label">{label}</data></node>')

        # Crear arista si tiene un nodo padre
        if parent_id is not None:
            edges.append(f'<edge source="{parent_id}" target="{node_id}" />')

        # Recorrer hijos del nodo actual
        for child in node.children:
            GraphMLGenerator._traverse_tree(child, nodes, edges, parent_id=node_id, node_id_counter=node_id_counter)


if __name__ == "__main__":
    # Crear un ejemplo de árbol de nodos
    from old.node.node import Node

    root = Node(
        "test",
        children=[
            Node(
                "top",
                attributes={"xxx": "Hello world!"},
                children=[
                    Node("nested", text="He"),
                    Node("nested", text="World"),
                    Node("nested", text="Again")
                ]
            ),
            Node(
                "mid",
                attributes={"xxx": "Hello world!"},
                children=[
                    Node("nested", text="Hello"),
                    Node("more", text="false"),
                    Node("even", text="2")
                ]
            ),
            Node("cat")
        ]
    )

    # Generar GraphML
    graphml_content = GraphMLGenerator.generate(root)
    print(graphml_content)
