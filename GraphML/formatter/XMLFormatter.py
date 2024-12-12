class XMLFormatter:
    """
    Clase estática para formatear cadenas XML añadiendo saltos de línea después de cada `>`
    para mejorar la legibilidad.
    """

    @staticmethod
    def format(xml_content: str) -> str:
        """
        Añade saltos de línea después de cada `>` en una cadena XML.

        Args:
            xml_content (str): Cadena XML sin formatear.

        Returns:
            str: Cadena XML formateada con saltos de línea.
        """
        # Separar con saltos de línea después de cada `>`
        lines = xml_content.replace('>', '>\n')

        # Replace each > followed by a character different thant \n with >\n
        lines = lines.replace('</', '\n</').splitlines()

        # Remove all empty lines
        lines = [line.strip() for line in lines if line.strip()]

        # Eliminar espacios extra y ajustar indentación
        formatted_lines = []
        indent_level = 0

        for line in lines:
            if line.startswith("</"):
                indent_level -= 1

            formatted_lines.append("    " * max(indent_level, 0) + line)

            if line.startswith("<") and not line.startswith("</"):
                indent_level += 1
                continue

        return "\n".join(formatted_lines)


# Ejemplo de uso
if __name__ == "__main__":
    raw_xml = """<?xml version="1.0" encoding="UTF-8"?><root><child attribute="value">Text</child><child>Another</child></root>"""
    formatted_xml = XMLFormatter.format(raw_xml)
    print(formatted_xml)
