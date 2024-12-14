class Desc:
    """
    Representa un elemento `<desc>` en GraphML.

    <!ELEMENT desc (#PCDATA)>
    desc elements should contain meta information useful for human readers of a graphml document.
    For example, they may contain a specification of the level of sophistication of the contained graph.
    Another example would be a brief description of the data associated with a particular key.
    Attributes: None
    """

    def __init__(self, content: str):
        """
        Inicializa un elemento de descripción.

        Args:
            content (str): La descripción del elemento.
        """
        self.content = content

    def to_xml(self) -> str:
        """
        Convierte el elemento de descripción a su representación XML.

        Returns:
            str: Representación XML del elemento `<desc>`.
        """
        return f"<desc>{self.content}</desc>"
