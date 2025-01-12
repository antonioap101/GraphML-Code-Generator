import React from "react";
import styles from "./validationsPopup.module.css";
import sharedStyles from "../sharedPopUpStyles.module.css";
import {FieldModel, Validation} from "../../../constants/CRUDCodeGeneratorInput";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faArrowRotateLeft, faTimes} from "@fortawesome/free-solid-svg-icons";
import {TypeEnum} from "../../../constants/TypeEnum.ts";
import AceIDEComponent from "../../aceIde/AceIDEComponent.tsx";


interface ValidationsPopupProps {
    language: string;
    field: FieldModel;
    setValidations: (validations: Validation) => void;
    onClose: () => void;
}

const ValidationsPopUp: React.FC<ValidationsPopupProps> = ({language, field, setValidations, onClose}) => {
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
                            type="button"
                            className={styles.resetButton}
                            onClick={() => setValidations({})}
                            aria-label="Reset Validations"
                        >
                            <FontAwesomeIcon icon={faArrowRotateLeft} size="sm"/>
                        </button>
                        <button type="button" className={styles.closeButton} onClick={onClose} aria-label="Close">
                            <FontAwesomeIcon icon={faTimes}/>
                        </button>
                    </div>
                </header>

                {type === TypeEnum.BOOLEAN ? (
                    <div className={styles.noSettings}>
                        <p>No extra settings available for the selected type.</p>
                    </div>
                ) : (
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
                                        min={0}
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
                                        min={0}
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

                        {/* AceIDE for custom code */}
                        <div className={styles.customCodeSection}>
                            <label>Custom Validation Code:</label>
                            <AceIDEComponent
                                code={validations?.customCode || ""}
                                setCode={(newCode) => handleChange("customCode", newCode)}
                                language={language}
                                readonly={false}
                                enableBasicAutocompletion={true}
                            />
                        </div>
                    </form>
                )}
            </div>
        </div>
    );
};

export default ValidationsPopUp;
