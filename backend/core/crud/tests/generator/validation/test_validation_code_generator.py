import unittest

from backend.core.crud.src.generator.validation.validation_code_generator import ValidationCodeGenerator
from backend.core.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from backend.core.crud.src.parsing.constants.types.type_enum import TypeEnum
from backend.core.crud.src.parsing.input_elements.field_model import FieldModel
from backend.core.crud.src.parsing.input_elements.validations import Validations


class TestValidationCodeGenerator(unittest.TestCase):

    def setUp(self):
        self.fields = [
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
                    maxValue=100,
                    customCode="if (age < 18) {\n    throw new Error('Age must be at least 18');\n}"
                )
            )
        ]

    def test_python_validation_code(self):
        generator = ValidationCodeGenerator.fromLanguage(AllowedLanguages.python)
        code = generator.forFields(self.fields)

        expected_code = (
            "if len(username) < 3:\n"
            "    raise ValueError(f\"username must be at least 3 characters long\")\n"
            "if len(username) > 20:\n"
            "    raise ValueError(f\"username must be less than 20 characters\")\n"
            "import re\n"
            "if not re.match(r\"^[a-zA-Z0-9_]+$\", username):\n"
            "    raise ValueError(f\"username does not match the pattern ^[a-zA-Z0-9_]+$\")\n"
            "if age < 0:\n"
            "    raise ValueError(f\"age must be greater than 0\")\n"
            "if age > 100:\n"
            "    raise ValueError(f\"age must be less than or equal to 100\")\n"
            "// Custom Code for age\n"
            "if (age < 18) {\n"
            "    throw new Error('Age must be at least 18');\n"
            "}"
        )

        self.assertEqual(code.strip(), expected_code.strip())

    def test_no_validations(self):
        generator = ValidationCodeGenerator.fromLanguage(AllowedLanguages.python)
        no_validation_field = FieldModel(
            name="noValidationField",
            type=TypeEnum.TEXT,
            validations=None
        )
        code = generator.forField(no_validation_field)
        self.assertEqual(code, "")

    def test_custom_code_only(self):
        generator = ValidationCodeGenerator.fromLanguage(AllowedLanguages.python)
        custom_code_field = FieldModel(
            name="customField",
            type=TypeEnum.NUMBER,
            validations=Validations(
                customCode="if customField == 42: raise ValueError('The answer cannot be 42')"
            )
        )
        code = generator.forField(custom_code_field)
        expected_code = (
            "// Custom Code for customField\n"
            "if customField == 42: raise ValueError('The answer cannot be 42')"
        )
        self.assertEqual(code.strip(), expected_code.strip())

    def test_empty_fields(self):
        generator = ValidationCodeGenerator.fromLanguage(AllowedLanguages.python)
        code = generator.forFields([])
        self.assertEqual(code, "")


if __name__ == "__main__":
    unittest.main()
