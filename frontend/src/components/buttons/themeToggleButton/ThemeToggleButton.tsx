// src/components/ThemeToggleButton.tsx
import React from 'react';
import styles from './ThemeToggleButton.module.css';
import { FaSun, FaMoon } from 'react-icons/fa';
import {useTheme} from "../../../styles/theme/themeContext.tsx";

const ThemeToggleButton: React.FC = () => {
    const { theme, toggleTheme } = useTheme();

    return (
        <button
            onClick={toggleTheme}
            className={styles.themeToggleButton}
            aria-label="Toggle Theme"
        >
            {theme === 'lightTheme' ? <FaMoon size={24} /> : <FaSun size={24} />}
        </button>
    );
};

export default ThemeToggleButton;
