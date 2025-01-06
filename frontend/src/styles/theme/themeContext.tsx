// src/context/ThemeContext.tsx
import React, {createContext, ReactNode, useContext, useState} from 'react';

type Theme = 'lightTheme' | 'darkTheme';

interface ThemeContextProps {
    theme: Theme;
    toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextProps | undefined>(undefined);

export const ThemeProvider: React.FC<{ children: ReactNode }> = ({children}) => {
    const [theme, setTheme] = useState<Theme>('lightTheme');

    const toggleTheme = () => {
        setTheme((prevTheme) => (prevTheme === 'lightTheme' ? 'darkTheme' : 'lightTheme'));
    };

    return (
        <ThemeContext.Provider value={{theme, toggleTheme}}>
            <div className={`theme ${theme}`}>{children}</div>
        </ThemeContext.Provider>
    );
};

export const useTheme = () => {
    const context = useContext(ThemeContext);
    if (!context) {
        throw new Error('useTheme debe ser usado dentro de un ThemeProvider');
    }
    return context;
};
