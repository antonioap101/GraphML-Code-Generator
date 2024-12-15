class File:
    """Class to represent a file with its properties."""

    def __init__(self, name: str, content: str, extension: str):
        """
        Initialize a file object.

        Args:
            name (str): Name of the file without extension.
            content (str): Content of the file.
            extension (str): Extension of the file (e.g., .txt, .json_parser).
        """
        self.name = name
        self.content = content
        self.extension = extension

    def get_full_name(self) -> str:
        """Get the full name of the file, including its extension."""
        return f"{self.name}.{self.extension}"

    def __repr__(self) -> str:
        """Return a string representation of the file object."""
        return f"File(name='{self.name}', extension='{self.extension}')"
