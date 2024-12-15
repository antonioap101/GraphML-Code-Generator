// src/components/ThemeToggleButton.tsx
import React from 'react';
import './ThemeToggleButton.css';
import { FaSun, FaMoon } from 'react-icons/fa';
import {useTheme} from "../../theme/themeContext.tsx";

const ThemeToggleButton: React.FC = () => {
    const { theme, toggleTheme } = useTheme();

    return (
        <button
            onClick={toggleTheme}
            className="theme-toggle-button"
            aria-label="Toggle Theme"
        >
            {theme === 'light' ? <FaMoon size={24} /> : <FaSun size={24} />}
        </button>
    );
};

export default ThemeToggleButton;
