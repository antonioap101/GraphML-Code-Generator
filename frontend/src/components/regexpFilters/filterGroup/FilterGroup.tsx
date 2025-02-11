import React from "react";
import styles from "./FilterGroup.module.css";
import {Condition, ConditionOperator, FilterConditionType, GroupCondition} from "../../../hooks/useFilter.tsx";
import DropdownComponent, {DropDownOption} from "../../dropDown/DropDownComponent";
import FilterCondition from "../filterCondition/FilterCondition";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faFolder, faPlus, faTrash} from "@fortawesome/free-solid-svg-icons";

type FilterGroupProps = {
    parentGroup: GroupCondition;
    thisGroup: GroupCondition;
    onAddition: (parentGroup: GroupCondition, newCondition: Condition | GroupCondition) => void;
    onUpdate: (parentGroup: GroupCondition, newCondition: Condition | GroupCondition) => void;
    onDelete: (parentGroup: GroupCondition, newCondition: Condition | GroupCondition) => void;
};

const FilterGroup: React.FC<FilterGroupProps> = ({parentGroup, thisGroup, onAddition, onUpdate, onDelete}) => {
    const combinatorOptions: DropDownOption[] = [
        {value: "AND", label: "AND", icon: <FontAwesomeIcon icon={faPlus}/>},
        {value: "OR", label: "OR", icon: <FontAwesomeIcon icon={faFolder}/>},
    ];

    const handleUpdate = (option: DropDownOption) => {
        thisGroup.combinator = option.value as "AND" | "OR";
        onUpdate(parentGroup, thisGroup);
    };

    const handleAddCondition = (newCondition: Condition | GroupCondition) => {
        onAddition(thisGroup, newCondition);
    };

    const handleDelete = (condition: Condition | GroupCondition) => {
        onDelete(parentGroup, condition);
    }

    return (
        <div className={styles.filterGroup}>
            <div className={styles.combinatorRow}>
                <DropdownComponent
                    selectedOption={combinatorOptions.find((option) => option.value === parentGroup.combinator)}
                    options={combinatorOptions}
                    onSelect={handleUpdate}
                    placeholder="Select Combinator"
                />
            </div>

            <div className={styles.conditionsContainer}>
                {thisGroup.conditions.map((condition, index) => (
                    <div key={index} className={styles.conditionRow}>
                        {condition instanceof GroupCondition ? (
                            <FilterGroup
                                parentGroup={thisGroup}
                                thisGroup={condition}
                                onAddition={onAddition}
                                onUpdate={onUpdate}
                                onDelete={onDelete}
                            />
                        ) : (
                            <FilterCondition
                                parentGroup={thisGroup}
                                condition={condition}
                                onUpdate={onUpdate}
                                onDelete={onDelete}
                            />
                        )}
                    </div>
                ))
                }
            </div>


            <div className={styles.buttonGroup}>
                <button
                    onClick={() => handleAddCondition(new Condition("", ConditionOperator.EQUALS, "", FilterConditionType.TEXT))}
                    className={styles.groupButton}>
                    <FontAwesomeIcon icon={faPlus}/> Add Condition
                </button>
                <button
                    onClick={() => handleAddCondition(new GroupCondition("AND"))}
                    className={styles.groupButton}>
                    <FontAwesomeIcon icon={faFolder}/> Add Group
                </button>
                {(thisGroup !== parentGroup) &&
                    (<button
                        onClick={() => handleDelete(thisGroup)}
                        className={styles.groupButton}>
                        <FontAwesomeIcon icon={faTrash}/> Delete Group
                    </button>)
                }
            </div>
        </div>
    );
};

export default FilterGroup;
