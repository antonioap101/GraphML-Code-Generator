from typing import List


class Node:
    """Clase que representa un nodo en el árbol generado del XML."""

    def __init__(self, tag: str, attributes: dict = None, text: str = None, children: List["Node"] = None):
        self.tag = tag
        self.attributes = attributes or {}
        self.text = text.strip() if text else None
        self.children = children or []

    def add_child(self, child: 'Node'):
        """Añade un nodo hijo a este nodo."""
        self.children.append(child)

    def __repr__(self):
        """Representación legible del nodo."""
        attributes = f" {self.attributes}" if self.attributes else ""
        text = f": '{self.text}'" if self.text else ""
        return f"<Node tag='{self.tag}'{attributes}{text}>"
