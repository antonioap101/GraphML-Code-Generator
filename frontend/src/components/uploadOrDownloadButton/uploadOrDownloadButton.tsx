import React from "react";
import { FaUpload, FaDownload } from "react-icons/fa"; // Importa los iconos necesarios
import "./uploadOrDownloadButton.css";

interface UploadOrDownloadButtonProps {
    action: "upload" | "download"; // Define el tipo de acción
    onClick: () => void; // Manejador de clic
    tooltip?: string; // Opción para añadir un texto emergente
}

const UploadOrDownloadButton: React.FC<UploadOrDownloadButtonProps> = ({ action, onClick, tooltip }) => {
    const renderIcon = () => {
        if (action === "upload") return <FaUpload className="action-icon" />;
        if (action === "download") return <FaDownload className="action-icon" />;
    };

    return (
        <div className="action-button" title={tooltip}>
            <button className={`action-label ${action}`} onClick={onClick}>
                {renderIcon()}
            </button>
        </div>
    );
};

export default UploadOrDownloadButton;
