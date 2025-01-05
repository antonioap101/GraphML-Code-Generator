import React from 'react';
import {useNavigate} from 'react-router-dom';
import {FaHome} from 'react-icons/fa';
import styles from './HomeButton.module.css';

const HomeButton: React.FC = () => {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/');
    };

    return (
        <button onClick={handleClick} className={styles.homeButton} aria-label="Go to Home">
            <FaHome size={24}/>
        </button>
    );
};

export default HomeButton;