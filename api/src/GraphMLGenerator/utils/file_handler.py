class FileHandler:
    """Clase para manejar operaciones de lectura y escritura de archivos."""

    @staticmethod
    def read_file(filepath: str) -> str:
        """Lee el contenido de un archivo."""
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def write_file(filepath: str, content: str):
        """Escribe contenido en un archivo."""
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
