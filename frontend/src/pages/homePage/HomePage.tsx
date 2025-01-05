import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';

const HomePage: React.FC = () => {
    return (
        <div className="home-container">
            <h1>Generadores de Código</h1>
            <div className="menu">
                <Link to="/graphml-code-generator">
                    <button>Generador de Código GraphML</button>
                </Link>
                <Link to="/crud-code-generator">
                    <button>Generador de Código CRUD</button>
                </Link>
            </div>
        </div>
    );
};

export default HomePage;
