import React from 'react';

interface ThemedDivProps {
    children: React.ReactNode; // Contenido del componente
    className?: string; // Clases CSS adicionales
    style?: React.CSSProperties; // Estilos en línea
}

const ThemedDiv: React.FC<ThemedDivProps> = ({ children, className = '', style }) => {
    return (
        <div
            className={`themed-div ${className}`}
            style={{
                backgroundColor: 'var(--color-background)',
                color: 'var(--color-text)',
                ...style,
            }}
            data-themed="true" // Identificador para aplicar exclusiones
        >
            {children}
        </div>
    );
};

export default ThemedDiv;
