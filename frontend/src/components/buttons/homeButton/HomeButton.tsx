import React from 'react';
import {useNavigate} from 'react-router-dom';

import styles from './HomeButton.module.css';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faHome} from "@fortawesome/free-solid-svg-icons";

const HomeButton: React.FC = () => {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/');
    };

    return (
        <button onClick={handleClick} className={styles.homeButton} aria-label="Go to Home">
            <FontAwesomeIcon icon={faHome} size="lg"/>
        </button>
    );
};

export default HomeButton;