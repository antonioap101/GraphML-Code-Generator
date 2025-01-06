import React from "react";

import "./GenerateButton.css";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faPlay} from "@fortawesome/free-solid-svg-icons";

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
            <FontAwesomeIcon icon={faPlay} size="lg"/>
            <span>{loading ? "Generating..." : "Generate"}</span>
        </button>
    );
};

export default GenerateButton;
