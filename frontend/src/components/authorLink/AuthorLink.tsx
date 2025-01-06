// src/components/AuthorLink.tsx
import React from "react";
import {FaUpRightFromSquare} from "react-icons/fa6";


const AuthorLink: React.FC = () => {
    return (
        <footer style={{
            position: 'fixed',
            bottom: 15,
            right: 15,
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            fontSize: '0.9rem',
            color: '#555',
            fontFamily: 'Arial, sans-serif',
        }}>
            <a
                href="https://antapagon.com"
                target="_blank"
                rel="noopener noreferrer"
                style={{
                    textDecoration: 'none',
                    fontWeight: 'bold',
                    color: 'inherit',
                    display: 'flex',
                    alignItems: 'center',
                    gap: 'inherit',
                    transition: 'text-decoration 0.2s ease',
                }}
                onMouseEnter={(e) => {
                    e.currentTarget.style.textDecoration = 'underline';
                }}
                onMouseLeave={(e) => {
                    e.currentTarget.style.textDecoration = 'none';
                }}
            >
                <span>By Antonio Aparicio</span>
                <FaUpRightFromSquare />
            </a>
        </footer>
    );
};

export default AuthorLink;
