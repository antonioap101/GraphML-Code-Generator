import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover("backend.crud.tests")  # Escanea el directorio 'tests'

    runner = unittest.TextTestRunner(verbosity=2)  # Verbosidad para detalles
    runner.run(suite)
