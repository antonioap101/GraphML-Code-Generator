import json
from enum import Enum
from pathlib import Path

from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages


class TemplateType(Enum):
    DAO = "dao"
    CONNECTION = "connection"


class TemplateLoader:
    class TemplateIndex:
        templates_path = Path(__file__)
        _index = None

        @staticmethod
        def load_index(file_path: str = f"{templates_path}/index.json") -> dict:
            """Loads the template index from a JSON file."""
            if TemplateLoader.TemplateIndex._index is None:
                with open(file_path, "r") as file:
                    TemplateLoader.TemplateIndex._index = json.load(file)
            return TemplateLoader.TemplateIndex._index

        @staticmethod
        def get_template_path(language: AllowedLanguages, template_type: TemplateType) -> str:
            """Gets the path of a template file from the index."""
            index = TemplateLoader.TemplateIndex.load_index()
            try:
                return index[language.value][template_type.value]
            except KeyError as e:
                raise ValueError(f"Template path for {language}.{template_type} not found") from e

    @staticmethod
    def load_template(language: AllowedLanguages, template_type: TemplateType) -> str:
        """
        Loads the content of a template for a given language and template type.
        """
        # Get the template file path
        template_path = TemplateLoader.TemplateIndex.get_template_path(language, template_type)

        # Load the template content
        with open(template_path, "r") as file:
            return file.read()

    @staticmethod
    def format_template(language: AllowedLanguages, template_type: TemplateType, **kwargs) -> str:
        """
        Loads and formats a template by replacing placeholders with provided arguments.
        """
        template = TemplateLoader.load_template(language, template_type)
        return template.format(**kwargs)
