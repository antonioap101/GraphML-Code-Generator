import React from "react";
import styles from "./RegexGenerator.module.css";
import {FiltersComponent} from "../../components/regexpFilters/FiltersComponent.tsx";
// import {useApi} from "../../hooks/useAPI.tsx";
// import {useError} from "../../hooks/useError.tsx";

const RegexGenerator: React.FC = () => {


    // const {errorMessage, setError, clearError} = useError();
    // const {loading, apiError, crudOutput, generateCrud} = useApi();


    return (
        <div>
            <h1>Regex Generator</h1>
            <section className={styles.container}>
                <aside className={styles.conditionsSection}>
                <FiltersComponent />
                </aside>
                <aside className={styles.textSection}>

                </aside>
            </section>
        </div>
    );
};

export default RegexGenerator;
