from api.src.GraphMLGenerator.GraphML.GraphMLElement import GraphMLElement


class Locator(GraphMLElement):
    """
    Representa un elemento `<locator>` en GraphML.
    """

    def __init__(self, href: str):
        """
        Inicializa un localizador.

        Args:
            href (str): URL o referencia al recurso externo.
        """
        super().__init__()
        self.href = href

    def to_xml(self) -> str:
        """
        Convierte el localizador a su representación XML.

        Returns:
            str: Representación XML del localizador.
        """
        attributes = (f'xlink:xlink="http://www.w3.org/TR/2000/PR-xlink-20001220" '
                      f'xlink:href="{self.href}" '
                      f'xlink:type="simple"')

        return f"<locator {attributes}></locator>"
