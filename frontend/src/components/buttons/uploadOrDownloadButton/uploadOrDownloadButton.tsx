import React from "react";
import {FaDownload, FaUpload} from "react-icons/fa"; // Importa los iconos necesarios
import "./uploadOrDownloadButton.css";

interface UploadOrDownloadButtonProps {
    action: "upload" | "download"; // Define el tipo de acción
    onClick: () => void; // Manejador de clic
    tooltip?: string; // Opción para añadir un texto emergente
}

const UploadOrDownloadButton: React.FC<UploadOrDownloadButtonProps> = ({action, onClick, tooltip}) => {
    const renderIcon = () => {
        if (action === "upload") return <FaUpload className="action-icon"/>;
        if (action === "download") return <FaDownload className="action-icon"/>;
    };

    return (
        <button className={`action-label ${action}`} onClick={onClick} title={tooltip}>
            {renderIcon()}
        </button>
    );
};

export default UploadOrDownloadButton;
