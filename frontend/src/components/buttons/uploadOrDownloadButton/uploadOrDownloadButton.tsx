import React from "react";

import "./uploadOrDownloadButton.css";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faDownload, faUpload} from "@fortawesome/free-solid-svg-icons";

interface UploadOrDownloadButtonProps {
    action: "upload" | "download"; // Define el tipo de acción
    onClick: () => void; // Manejador de clic
    tooltip?: string; // Opción para añadir un texto emergente
}

const UploadOrDownloadButton: React.FC<UploadOrDownloadButtonProps> = ({action, onClick, tooltip}) => {
    const renderIcon = () => {
        if (action === "upload") return <FontAwesomeIcon icon={faUpload} className="action-icon"/>;
        if (action === "download") return <FontAwesomeIcon icon={faDownload} className="action-icon"/>;
    };

    return (
        <button className={`action-label ${action}`} onClick={onClick} title={tooltip}>
            {renderIcon()}
        </button>
    );
};

export default UploadOrDownloadButton;
