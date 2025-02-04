import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';

const HomePage: React.FC = () => {
    return (
        <div className="home-container">
            <div className="menu">
                <Link to="/graphml-code-generator">
                    <button>Generador de Código GraphML</button>
                </Link>
                <Link to="/crud-code-generator">
                    <button>Generador de Código CRUD</button>
                </Link>
                <Link to="/regex-generator">
                    <button>Generador de Expresiones Regulares</button>
                </Link>
            </div>
        </div>
    );
};

export default HomePage;
