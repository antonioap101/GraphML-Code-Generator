import React, { createContext, useContext, useState, ReactNode } from "react";

// Tipo para los errores
type ErrorContextType = {
    errorMessage: string | null;
    setError: (message: string) => void;
    clearError: () => void;
};

// Contexto de errores
const ErrorContext = createContext<ErrorContextType | undefined>(undefined);

// Proveedor de errores
export const ErrorProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [errorMessage, setErrorMessage] = useState<string | null>(null);

    const setError = (message: string) => setErrorMessage(message);
    const clearError = () => setErrorMessage(null);

    return (
        <ErrorContext.Provider value={{ errorMessage, setError, clearError }}>
            {children}
        </ErrorContext.Provider>
    );
};

// Hook personalizado para usar el contexto de errores
export const useError = (): ErrorContextType => {
    const context = useContext(ErrorContext);
    if (!context) {
        throw new Error("useError debe ser usado dentro de un ErrorProvider");
    }
    return context;
};
