import React, {useState} from "react";
import styles from "./RegexGenerator.module.css";
import {FiltersComponent} from "../../components/regexpFilters/FiltersComponent.tsx";
import RegexHighlighter from "../../components/regexpFilters/regexHighlighterComponent/RegexHighlighterComponent.tsx";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faFilter, faFont, faRotate} from "@fortawesome/free-solid-svg-icons";
import ActionButton from "../../components/buttons/actionButton/ActionButton.tsx";
import crudStyles from "../crud/CRUDCodeGenerator.module.css";
import {useFilterContext} from "../../hooks/useFilter.tsx";
// import {useError} from "../../hooks/useError.tsx";

const RegexGenerator: React.FC = () => {
    // const {errorMessage, setError, clearError} = useError();

    // Estado para guardar el texto a analizar
    const [text, setText] = useState("");
    const {filters, resetAll} = useFilterContext();
    const [loading, setLoading] = useState(false);
    const [regex, setRegex] = useState<RegExp | undefined>(undefined);

    const handleAnalyze = () => {
        setLoading(true);
        console.log("Analyzing... ", text);
        console.log("Filters: ", filters.toJSON());
        console.log("Regex: ", filters.toRegex());
        setRegex(RegExp(filters.toRegex(), "g"));
        setLoading(false);
    }


    const resetFilters = () => {
        resetAll();
        setText("");
        setRegex(undefined);
        setLoading(false);
    }
    return (
        <div>
            <section className={styles.container}>
                <aside className={styles.conditionsSection}>
                    <header className={crudStyles.codeHeader}>
                        <a className={crudStyles.codeLink}>
                            <FontAwesomeIcon icon={faFilter}/>
                            <h2 className={styles.title}>Filter Builder</h2>
                        </a>
                        <ActionButton
                            onClick={resetFilters}
                            disabled={false}
                            loading={false}
                            placeholders={{loading: 'Resetting...', default: 'Reset Filters'}}
                            icon={faRotate}
                            horizontal={true}
                        />
                    </header>
                    <FiltersComponent/>
                </aside>

                {/* Sección donde añadimos el bloque de texto para analizar */}
                <aside className={styles.textSection}>
                    <header className={crudStyles.codeHeader}>
                        <a className={crudStyles.codeLink}>
                            <FontAwesomeIcon icon={faFont}/>
                            <h2 className={styles.title}>Text</h2>
                        </a>
                        <ActionButton
                            onClick={handleAnalyze}
                            disabled={false}
                            loading={loading}
                            placeholders={{loading: 'Analyzing...', default: 'Analyze'}}
                            horizontal={true}/>
                    </header>
                    <RegexHighlighter
                        onInputChange={(text) => {
                            setText(text);
                            handleAnalyze();
                        }}
                        regex={regex?.source || ""}
                    />
                </aside>
            </section>
        </div>
    );
};

export default RegexGenerator;
