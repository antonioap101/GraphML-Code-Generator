// src/components/HelpButton.tsx
import React, {useState} from 'react';
import {FaQuestionCircle} from 'react-icons/fa';
// import './helpButton.module.css';
import styles from "./helpButton.module.css";
import HelpPopUp from "../popUps/helpPopUp/HelpPopUp.tsx";


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
                <FaQuestionCircle size={24} />
            </button>

            {isPopupOpen && (
                <HelpPopUp onClick={togglePopup} />
            )}
        </>
    );
};

export default HelpButton;
