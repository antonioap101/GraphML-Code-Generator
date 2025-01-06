import React from "react";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faArrowRotateLeft, faTimes} from "@fortawesome/free-solid-svg-icons";
import styles from "./ConnectionParametersPopUp.module.css"
import sharedStyles from "../sharedPopUpStyles.module.css";
import {ConnectionParameters} from "../../../constants/CRUDCodeGeneratorInput.ts";
import ConnectionParametersForm from "../../connectionParametersForm/ConnectionParametersForm.tsx";


interface ConnectionParametersPopupProps {
    parameters: ConnectionParameters;
    setParameters: (params: ConnectionParameters) => void;
    onClose: () => void;
}

const ConnectionParametersPopup: React.FC<ConnectionParametersPopupProps> = ({
                                                                                 parameters,
                                                                                 setParameters,
                                                                                 onClose,
                                                                             }) => {
    return (
        <div className={sharedStyles.overlay}>
            <div className={styles.popup}>
                <header className={styles.popupHeader}>
                    <h3>Connection Parameters</h3>
                    <div>
                        <button className={styles.resetButton} onClick={() => setParameters({host: "localhost", port: 3000, database_name: "default"})} aria-label="Reset Validations">
                            <FontAwesomeIcon icon={faArrowRotateLeft} size="sm"/>
                        </button>
                        <button className={styles.closeButton} onClick={onClose} aria-label="Close">
                            <FontAwesomeIcon icon={faTimes}/>
                        </button>
                    </div>
                </header>
                <ConnectionParametersForm parameters={parameters} setParameters={setParameters}/>
            </div>
        </div>
    );
};

export default ConnectionParametersPopup;
