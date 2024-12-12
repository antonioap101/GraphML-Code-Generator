import re


def NMTOKEN(func):
    """
    Decorador para validar que el valor de un atributo cumpla con las restricciones de NMTOKEN.
    """

    def wrapper(instance, value):
        # Expresión regular para NMTOKEN: alfanumérico y caracteres permitidos (-, ., _, :)
        if not re.fullmatch(r"[A-Za-z0-9._:-]+", value):
            raise ValueError(f"The value '{value}' is not a valid NMTOKEN.")
        func(instance, value)

    return wrapper
