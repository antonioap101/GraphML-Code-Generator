// src/components/popUps/ExtraSettingsPopup.tsx
import React from "react";
import styles from "./ExtraSettingsPopup.module.css";
import sharedStyles from "../sharedPopUpStyles.module.css";
import {FieldModel, Validation} from "../../../constants/CRUDCodeGeneratorInput";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faArrowRotateLeft, faTimes} from "@fortawesome/free-solid-svg-icons";
import {TypeEnum} from "../../../constants/TypeEnum.ts";

interface ExtraSettingsPopupProps {
    field: FieldModel;
    setValidations: (validations: Validation) => void;
    onClose: () => void;
}

const ExtraSettingsPopup: React.FC<ExtraSettingsPopupProps> = ({field, setValidations, onClose}) => {
    const {validations, type} = field;

    const handleChange = (key: keyof Validation, value: string | number | undefined) => {
        setValidations({
            ...validations,
            [key]: value,
        });
    };

    return (
        <div className={sharedStyles.overlay}>
            <div className={styles.popup}>
                <header className={styles.header}>
                    <h3>Field Validations ({type})</h3>
                    <div>
                        <button
                            className={styles.resetButton}
                            onClick={() => setValidations({})}
                            aria-label="Reset Validations"
                        >
                            <FontAwesomeIcon icon={faArrowRotateLeft} size="sm" />
                        </button>
                        <button className={styles.closeButton} onClick={onClose} aria-label="Close">
                            <FontAwesomeIcon icon={faTimes} />
                        </button>
                    </div>
                </header>

                {type === TypeEnum.BOOLEAN ? (
                    // If the type is BOOLEAN, show a message
                    <div className={styles.noSettings}>
                        <p>No extra settings available for the selected type.</p>
                    </div>
                ) : (
                    // If the type is not BOOLEAN, show validation inputs
                    <form className={styles.form}>
                        <label>
                            Pattern:
                            <input
                                type="text"
                                value={validations?.pattern || ""}
                                onChange={(e) => handleChange("pattern", e.target.value)}
                            />
                        </label>

                        {type === TypeEnum.TEXT && (
                            <>
                                <label>
                                    Min Length:
                                    <input
                                        type="number"
                                        value={validations?.minLength || ""}
                                        onChange={(e) =>
                                            handleChange(
                                                "minLength",
                                                e.target.value ? parseInt(e.target.value, 10) : undefined
                                            )
                                        }
                                    />
                                </label>
                                <label>
                                    Max Length:
                                    <input
                                        type="number"
                                        value={validations?.maxLength || ""}
                                        onChange={(e) =>
                                            handleChange(
                                                "maxLength",
                                                e.target.value ? parseInt(e.target.value, 10) : undefined
                                            )
                                        }
                                    />
                                </label>
                            </>
                        )}

                        {(type === TypeEnum.NUMBER || type === TypeEnum.FLOAT || type === TypeEnum.DOUBLE) && (
                            <>
                                <label>
                                    Min Value:
                                    <input
                                        type="number"
                                        value={validations?.min || ""}
                                        onChange={(e) =>
                                            handleChange(
                                                "min",
                                                e.target.value ? parseInt(e.target.value, 10) : undefined
                                            )
                                        }
                                    />
                                </label>
                                <label>
                                    Max Value:
                                    <input
                                        type="number"
                                        value={validations?.max || ""}
                                        onChange={(e) =>
                                            handleChange(
                                                "max",
                                                e.target.value ? parseInt(e.target.value, 10) : undefined
                                            )
                                        }
                                    />
                                </label>
                            </>
                        )}
                    </form>
                )}
            </div>
        </div>
    );
};

export default ExtraSettingsPopup;
