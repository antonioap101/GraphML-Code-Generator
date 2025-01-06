// src/components/HelpButton.tsx
import React, {useState} from 'react';

// import './helpButton.module.css';
import styles from "./helpButton.module.css";
import HelpPopUp from "../popUps/helpPopUp/HelpPopUp.tsx";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faQuestionCircle} from "@fortawesome/free-solid-svg-icons";


console.log("STYLES: ", styles);

const HelpButton: React.FC = () => {
    const [isPopupOpen, setIsPopupOpen] = useState(false);

    const togglePopup = () => {
        setIsPopupOpen(!isPopupOpen);
    };

    return (
        <>
            <button
                onClick={togglePopup}
                className={styles.helpButton}
                aria-label="Help"
            >
                <FontAwesomeIcon icon={faQuestionCircle} size="lg"/>
            </button>

            {isPopupOpen && (
                <HelpPopUp onClick={togglePopup} />
            )}
        </>
    );
};

export default HelpButton;
