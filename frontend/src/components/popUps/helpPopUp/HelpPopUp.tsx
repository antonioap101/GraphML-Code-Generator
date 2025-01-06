import {useLocation} from "react-router-dom";
import styles from "./HelpPopUp.module.css";
import sharedStyles from "../sharedPopUpStyles.module.css";

const HelpPopUp = (props: { onClick: () => void }) => {
    const location = useLocation();

    // Definir el contenido dinámico según la ruta
    const helpContent: Record<string, { title: string; steps: string[]; example?: string }> = {
        "/crud-code-generator": {
            title: "Cómo utilizar el CRUD Code Generator",
            steps: [
                "Selecciona el DBMS y el lenguaje de programación.",
                "Agrega los atributos de la tabla en el generador.",
                "Haz clic en 'Generar' para obtener el código.",
                "Copia o descarga el resultado generado.",
            ],
            example: "",
        },
        "/graphml-code-generator": {
            title: "Cómo utilizar el GraphML Code Generator",
            steps: [
                "Escribe o pega el contenido XML en el área de texto.",
                "Carga un archivo XML usando el botón de selección.",
                "Haz clic en 'Convertir' para generar el GraphML.",
                "Descarga el resultado como un archivo .graphml.",
            ],
            example: `<root>
  <node1 attribute1="value1" attribute2="value2">
    <children>
      <subnode1 attribute3="value3">ABC</subnode1>
      <subnode2 attribute4="value4"/>
    </children>
  </node1>
  <node2 attribute5="value5"/>
</root>`,
        },
    };

    // Obtener el contenido basado en la ruta
    const content = helpContent[location.pathname] || {
        title: "Ayuda no disponible",
        steps: ["No se encontró información de ayuda para esta sección."],
    };

    return (
        <div className={sharedStyles.overlay} onClick={props.onClick}>
            <div className={styles.popupContent} onClick={(e) => e.stopPropagation()}>
                <h2>{content.title}</h2>
                <p>Sigue los pasos:</p>
                <ol>
                    {content.steps.map((step, index) => (
                        <li key={index}>{step}</li>
                    ))}
                </ol>
                {content.example && (
                    <>
                        <p>Ejemplo:</p>
                        <pre>{content.example}</pre>
                    </>
                )}
                <button onClick={props.onClick}>
                    Cerrar
                </button>
            </div>
        </div>
    );
};

export default HelpPopUp;
