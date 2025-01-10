import styles from "./ErrorPopUp.module.css";
import sharedStyles from "../sharedPopUpStyles.module.css";
import {useError} from "../../../hooks/useError.tsx";


const ErrorPopUp = () => {
    const { errorMessage, clearError } = useError();

    // Si no hay un mensaje de error, no renderizar nada
    if (!errorMessage) return null;

    return (
        <div className={sharedStyles.overlay} onClick={clearError}>
            <div className={styles.popupContent} onClick={(e) => e.stopPropagation()}>
                <h2>Error</h2>
                <p>{errorMessage}</p>
                <button onClick={clearError}>Cerrar</button>
            </div>
        </div>
    );
};

export default ErrorPopUp;
