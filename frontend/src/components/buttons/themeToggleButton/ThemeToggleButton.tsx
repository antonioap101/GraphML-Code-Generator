// src/input_elements/ThemeToggleButton.tsx
import React from 'react';
import styles from './ThemeToggleButton.module.css';

import {useTheme} from "../../../styles/theme/themeContext.tsx";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faMoon, faSun} from "@fortawesome/free-solid-svg-icons";

const ThemeToggleButton: React.FC = () => {
    const { theme, toggleTheme } = useTheme();

    return (
        <button
            onClick={toggleTheme}
            className={styles.themeToggleButton}
            aria-label="Toggle Theme"
        >
            {theme === 'lightTheme' ? <FontAwesomeIcon icon={faMoon} size="lg"/> : <FontAwesomeIcon icon={faSun} size="lg"/>}
        </button>
    );
};

export default ThemeToggleButton;
