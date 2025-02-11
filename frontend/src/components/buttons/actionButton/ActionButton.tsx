import React from "react";

import "./ActionButton.css";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faPlay} from "@fortawesome/free-solid-svg-icons";

interface GenerateButtonProps {
    onClick: () => void;
    disabled: boolean;
    loading: boolean;
    placeholders: {default: string, loading: string};
    icon?: any;
    horizontal?: boolean; // Nuevo prop opcional
}

const ActionButton: React.FC<GenerateButtonProps> = ({
                                                           onClick,
                                                           disabled,
                                                           loading,
                                                           placeholders,
                                                           icon=faPlay,
                                                           horizontal = true, // Por defecto es horizontal
                                                       }) => {
    return (
        <button
            onClick={onClick}
            disabled={disabled}
            className={`generate-button ${horizontal ? "horizontal" : "vertical"}`}
        >
            <FontAwesomeIcon icon={icon} size="lg"/>
            <span>{loading ? `${placeholders.loading}...` : `${placeholders.default}`}</span>
        </button>
    );
};

export default ActionButton;
