import React, {useEffect} from "react";
import styles from "./FiltersComponent.module.css";
import FilterGroup from "./filterGroup/FilterGroup";
import {useFilterContext} from "../../hooks/useFilter.tsx";

export const FiltersComponent: React.FC = () => {
    const {
        filters,
        addCondition,
        deleteCondition,
        updateCondition,
    } = useFilterContext();

    // Hook that observes the conditions object and updates the filter string
    useEffect(() => {
        console.warn("Filter updated", filters);
    }, [filters]);


    return (
        <div className={styles.container}>
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
