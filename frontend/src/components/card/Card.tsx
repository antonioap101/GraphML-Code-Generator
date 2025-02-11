import styles from "./Card.module.css";

export const Card = ({ children, className = "" }) => (
    <div className={`${styles.card} ${styles.cardWrapper} ${className}`}>
        {children}
    </div>
);

export const CardContent = ({ children }) => (
    <div className={styles.cardContent}>
        {children}
    </div>
);