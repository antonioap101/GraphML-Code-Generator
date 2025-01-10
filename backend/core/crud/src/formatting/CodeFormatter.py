class CodeFormatter:
    @staticmethod
    def format_code_with_indent(validation_code: str, indent: str) -> str:
        """
        Aplica la indentación especificada a cada línea del código de validación.

        :param validation_code: Código que será formateado.
        :param indent: Cadena que define la indentación (e.g., "    " para cuatro espacios).
        :return: Código con las líneas correctamente indentadas.
        """
        if not validation_code or len(validation_code) == 0:
            return validation_code

        validation_code_lines = validation_code.splitlines()
        # Aplicar la indentación a todas las líneas excepto la primera
        formatted_validation_code = f"{validation_code_lines[0]}\n" + "\n".join(
            f"{indent}{line}" for line in validation_code_lines[1:] if line.strip()
        )
        return formatted_validation_code


if __name__ == "__main__":
    # Ejemplo de uso del CodeFormatter
    validation_code_example = """if (input != null) {
validate(input);
}"""

    indent = "    "  # Cuatro espacios
    formatted_code = CodeFormatter.format_code_with_indent(validation_code_example, indent)
    print("Código con indentación aplicada:")
    print(formatted_code)
