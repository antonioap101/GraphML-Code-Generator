from typing import List

from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.templates.template_loader import TemplateLoader


class ValidationCodeGenerator:
    """
    Generador de código de validaciones basado en las plantillas para distintos lenguajes.
    """

    def __init__(self, language: AllowedLanguages):
        self.language = language
        self.templates = TemplateLoader.forLanguage(language).getValidations()

    @classmethod
    def fromLanguage(cls, language: AllowedLanguages) -> "ValidationCodeGenerator":
        """
        Crea una instancia de ValidationCodeGenerator para un lenguaje específico.
        """
        return cls(language)

    def forField(self, field_model: FieldModel) -> str:
        """
        Genera el código de validación para un campo específico.
        """
        if not field_model.validations:
            return ""

        validation_code_parts = []

        # Iterar sobre cada tipo de validación y generar el código correspondiente
        for validation_type, template in self.templates.items():
            validation_value = getattr(field_model.validations, validation_type.value, None)
            if validation_value is not None:
                validation_code_parts.append(
                    template.format(FieldName=field_model.name, **{validation_type.value: validation_value})
                )

        return "\n".join(validation_code_parts)

    def forFields(self, fields: List[FieldModel]) -> str:
        """
        Genera el código de validaciones para una lista de campos.
        """
        return "\n".join(self.forField(field) for field in fields if field.validations)


if __name__ == "__main__":
    from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
    from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
    from backend.core.crud.src.parsing.input_elements.validations import Validations
    from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum

    fields = [
        FieldModel(
            name="username",
            type=TypeEnum.TEXT,
            validations=Validations(
                minLength=3,
                maxLength=20,
                pattern=r"^[a-zA-Z0-9_]+$",
            )
        ),
        FieldModel(
            name="age",
            type=TypeEnum.NUMBER,
            validations=Validations(
                minValue=0,
                maxValue=100
            )
        )
    ]

    # java_validation_code = ValidationCodeGenerator.fromLanguage(AllowedLanguages.java).forFields(fields)
    # print(java_validation_code)
    # python_validation_code = ValidationCodeGenerator.fromLanguage(AllowedLanguages.python).forFields(fields)
    # print(python_validation_code)
    csharp_validation_code = ValidationCodeGenerator.fromLanguage(AllowedLanguages.csharp).forFields(fields)
    print(csharp_validation_code)
    # typescript_validation_code = ValidationCodeGenerator.fromLanguage(AllowedLanguages.typescript).forFields(fields)
    # print(typescript_validation_code)
