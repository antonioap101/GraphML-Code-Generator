class Desc:
    """
    Representa un elemento `<desc>` en GraphML.
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
