import React, {useState} from "react";
import DropdownComponent, {DropDownOption} from "../../dropDown/DropDownComponent";
import {Condition, ConditionOperator, GroupCondition} from "../../../hooks/useFilter.tsx";
import {operatorOptions} from "../interfaces";
import styles from "./FilterCondition.module.css";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faTrash} from "@fortawesome/free-solid-svg-icons";

type ConditionProps = {
    parentGroup: GroupCondition;
    condition: Condition;
    onUpdate: (parentGroup: GroupCondition, updatedCondition: Condition | GroupCondition) => void;
    onDelete: (parentGroup: GroupCondition, updatedCondition: Condition | GroupCondition) => void;
};

const FilterCondition: React.FC<ConditionProps> = ({parentGroup, condition, onUpdate, onDelete}) => {
    const [selectedOperator, setSelectedOperator] = useState<DropDownOption>(
        operatorOptions.find((option) => option.value === condition.operator) || operatorOptions[0]
    );


    const handleValueChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        condition.value = e.target.value;
        onUpdate(parentGroup, condition);
    }

    const handleOptionSelect = (option: DropDownOption) => {
        setSelectedOperator(option);
        condition.operator = option.value as ConditionOperator;
        onUpdate(parentGroup, condition);
    }

    const handleDelete = () => {
        onDelete(parentGroup, condition);
    }

    return (
        <div className={styles.filterCondition}>
            <DropdownComponent
                selectedOption={selectedOperator}
                options={operatorOptions}
                onSelect={handleOptionSelect}
            />

            <input
                type="text"
                value={String(condition.value)}
                onChange={handleValueChange}
                placeholder="Value"
                className={styles.inputField}
            />

            <button onClick={handleDelete} className={styles.deleteButton}>
                <FontAwesomeIcon icon={faTrash}/>
            </button>
        </div>
    );
};

export default FilterCondition;
