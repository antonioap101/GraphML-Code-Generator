import React from "react";
import { FaCode } from "react-icons/fa";
import "./GenerateButton.css";

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
            <FaCode size={20} />
            <span>{loading ? "Generando..." : "Generar"}</span>
        </button>
    );
};

export default GenerateButton;
