import argparse

from old.generator.graphml_generator import GraphMLGenerator
from old.parser.json_parser import JSONParser
from old.parser.xml_parser import XMLParser
from old.utils.file_handler import FileHandler


def main(args=None):
    # Configuración del analizador de argumentos
    parser = argparse.ArgumentParser(description="Generador de GraphML a partir de XML o JSON.")
    parser.add_argument(
        "-i", "--input_file",
        type=str,
        help="Ruta del archivo de entrada en formato XML o JSON."
    )
    parser.add_argument(
        "-o", "--output_file",
        type=str,
        help="Ruta del archivo de salida en formato GraphML."
    )
    args = parser.parse_args(args)

    # Si no se proporcionan los argumentos, preguntar al usuario
    input_file = args.input_file or input("Introduce la ruta del archivo de entrada (XML o JSON): ").strip()
    output_file = args.output_file or input("Introduce la ruta para guardar el archivo GraphML: ").strip()

    try:
        # Determinar el tipo de entrada según la extensión del archivo
        if input_file.endswith(".xml"):
            parsed_data = XMLParser.parse_from_file(input_file)
        elif input_file.endswith(".json"):
            parsed_data = JSONParser.parse_from_file(input_file)
        else:
            raise ValueError("El archivo de entrada debe ser de tipo XML o JSON.")

        # Generar GraphML
        graphml_content = GraphMLGenerator.generate(parsed_data)
        FileHandler.write_file(output_file, graphml_content)

        print(f"GraphML generado exitosamente en: {output_file}")

    except Exception as e:
        print(f"Error durante el proceso: {e}")


if __name__ == "__main__":
    # Pasar argumentos de prueba si es necesario
    args = ["-i", "examples/example.json", "-o", "examples/output.graphml"]  # Comentarlo si se quiere interactivo
    # args = None  # Cambiar a `args` definido arriba para pasar argumentos directamente
    main(args)
