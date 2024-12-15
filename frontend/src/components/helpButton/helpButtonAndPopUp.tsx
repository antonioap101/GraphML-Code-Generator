// src/components/HelpButton.tsx
import React, { useState } from 'react';
import { FaQuestionCircle } from 'react-icons/fa';
import './helpButton.css';

const HelpButton: React.FC = () => {
    const [isPopupOpen, setIsPopupOpen] = useState(false);

    const togglePopup = () => {
        setIsPopupOpen(!isPopupOpen);
    };

    return (
        <>
            <button
                onClick={togglePopup}
                className="help-button"
                aria-label="Help"
            >
                <FaQuestionCircle size={24} />
            </button>

            {isPopupOpen && (
                <div className="popup-overlay" onClick={togglePopup}>
                    <div className="popup-content" onClick={(e) => e.stopPropagation()}>
                        <h2>Cómo utilizar la aplicación</h2>
                        <p>Sigue los pasos para convertir tu XML a GraphML:</p>
                        <ol>
                            <li>Escribe o pega el contenido XML en el área de texto.</li>
                            <li>O carga un archivo XML usando el botón de selección.</li>
                            <li>Haz clic en "Convertir" para generar el GraphML.</li>
                            <li>Puedes descargar el resultado como un archivo .graphml.</li>
                        </ol>
                        <p>Ejemplo de XML:</p>
                        <pre>
                            {`<root>
    <node1 attribute1="value1" attribute2="value2">
        <children>
            <subnode1 attribute3="value3">ABC</subnode1>
            <subnode2 attribute4="value4"/>
        </children>
    </node1>
    <node2 attribute5="value5"/>
</root>
                            `}
                        </pre>
                        <button onClick={togglePopup} className="close-popup-button">Cerrar</button>
                    </div>
                </div>
            )}
        </>
    );
};

export default HelpButton;
