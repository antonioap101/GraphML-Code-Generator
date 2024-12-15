import React from "react";
import ActionButton from "../fileUploadButton/actionButton.tsx";
import "./input-output-styles.css"

interface XmlInputProps {
    xmlContent: string;
    onXmlChange: (value: string) => void;
    onFileUpload: (file: File) => void;
}

const XmlInput: React.FC<XmlInputProps> = ({xmlContent, onXmlChange, onFileUpload}) => {
    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files[0]) {
            onFileUpload(event.target.files[0]);
        }
    };

    return (
        <div style={{width: '100%', position: 'relative'}}>
            <div className="textarea-container">
                <textarea
                    value={xmlContent}
                    onChange={(e) => onXmlChange(e.target.value)}
                    placeholder="Escribe o pega aquí el contenido XML..."
                />
                <div className="upload-button">
                    <ActionButton
                        action="upload"
                        onClick={() => document.getElementById("file-input")?.click()}
                        tooltip="Subir archivo XML"
                    />
                </div>
                <input
                    id="file-input"
                    type="file"
                    accept=".xml"
                    style={{display: "none"}}
                    onChange={handleFileChange}
                />
            </div>
        </div>
    );
};

export default XmlInput;
