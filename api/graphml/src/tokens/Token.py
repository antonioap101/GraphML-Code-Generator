from abc import ABC, abstractmethod


class Token:
    """
    Clase base para representar un token del flujo de datos.
    Compatible con el formato de ElementTree.
    """
    def __init__(self, tag: str, attrib: dict = None, text: str = None, tail: str = None, children: list = None):
        self.tag = tag
        self.attrib = attrib if attrib else {}
        self.text = text or None
        self.tail = tail or None
        self.children = children if children else []
