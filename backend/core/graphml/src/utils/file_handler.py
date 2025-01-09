import os
from backend.core.graphml.src.utils.file import File


class FileHandler:
    """Class to handle file read and write operations."""

    @staticmethod
    def read_file(filepath: str) -> File:
        """
        Read the content of a file and return a File object.

        Args:
            filepath (str): Path to the file.

        Returns:
            File: An object representing the file.
        """
        name, extension = os.path.splitext(os.path.basename(filepath))
        extension = extension.lstrip('.')

        # Read the file content
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Return a File object
        return File(name=name, content=content, extension=extension)

    @staticmethod
    def write_file(filepath: str, content: str):
        """
        Write content to a file.

        Args:
            filepath (str): Path to the file.
            content (str): Content to write to the file.
        """
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
