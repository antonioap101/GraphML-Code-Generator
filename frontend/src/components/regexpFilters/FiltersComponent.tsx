import React, {useEffect} from "react";
import styles from "./FiltersComponent.module.css";

import FilterGroup from "./filterGroup/FilterGroup";
import {useFilter} from "../../hooks/useFilter.tsx";

export const FiltersComponent: React.FC = () => {
    const {
        filters,
        addCondition,
        deleteCondition,
        updateCondition,
        resetAll,
    } = useFilter();

    // Hook that observes the conditions object and updates the filter string
    useEffect(() => {
        console.warn("Filter updated", filters);
    }, [filters]);


    return (
        <div className={styles.container}>
            <div style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                alignContent: "center",
                marginBottom: "10px"
            }}>
                <h2 className={styles.title}>Filter Builder</h2>
                <button onClick={resetAll} className={styles.resetButton}>
                    Reset
                </button>
            </div>
            <FilterGroup
                parentGroup={filters}
                thisGroup={filters}
                onAddition={addCondition}
                onUpdate={updateCondition}
                onDelete={deleteCondition}
            />
        </div>
    );
};
