import unittest

from api.crud.src.generator.languages.factory.language_generator_factory import LanguageGeneratorFactory
from api.crud.src.generator.languages.java.java_dao_generator import JavaDaoGenerator
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages


class TestLanguageGeneratorFactory(unittest.TestCase):
    def test_get_java_generator(self):
        generator = LanguageGeneratorFactory.get_generators(AllowedLanguages.java)
        self.assertEqual(generator, JavaDaoGenerator)

    def test_get_unsupported_language(self):
        with self.assertRaises(ValueError) as context:
            LanguageGeneratorFactory.get_generators("unsupported_language")
        self.assertEqual(str(context.exception), "Unsupported language: unsupported_language")


if __name__ == "__main__":
    unittest.main()
