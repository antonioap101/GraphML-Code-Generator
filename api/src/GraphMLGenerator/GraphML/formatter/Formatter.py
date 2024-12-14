from abc import ABCMeta, abstractmethod


class Formatter(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def format(xml_content):
        """
        Añade saltos de línea después de cada `>` en una cadena XML.

        Args:
            xml_content (str): Cadena XML sin formatear.

        Returns:
            str: Cadena XML formateada con saltos de línea.
        """
        pass
