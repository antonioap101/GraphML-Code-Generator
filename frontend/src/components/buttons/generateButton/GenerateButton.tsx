import React from "react";

import "./GenerateButton.css";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCode} from "@fortawesome/free-solid-svg-icons";

interface GenerateButtonProps {
    onClick: () => void;
    disabled: boolean;
    loading: boolean;
    horizontal?: boolean; // Nuevo prop opcional
}

const GenerateButton: React.FC<GenerateButtonProps> = ({
                                                           onClick,
                                                           disabled,
                                                           loading,
                                                           horizontal = true, // Por defecto es horizontal
                                                       }) => {
    return (
        <button
            onClick={onClick}
            disabled={disabled}
            className={`generate-button ${horizontal ? "horizontal" : "vertical"}`}
        >
            <FontAwesomeIcon icon={faCode} size="lg"/>
            <span>{loading ? "Generando..." : "Generar"}</span>
        </button>
    );
};

export default GenerateButton;
