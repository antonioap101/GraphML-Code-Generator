import unittest

if __name__ == "__main__":
    # Descubre y ejecuta todos los tests en el módulo tests/
    loader = unittest.TestLoader()
    suite = loader.discover("tests")  # Escanea el directorio 'tests'

    runner = unittest.TextTestRunner(verbosity=2)  # Verbosidad para detalles
    runner.run(suite)
