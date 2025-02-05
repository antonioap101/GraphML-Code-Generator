import {DropDownOption} from "../dropDown/DropDownComponent.tsx";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faFont, faMagnifyingGlass} from "@fortawesome/free-solid-svg-icons";
import {ConditionOperator} from "../../hooks/useFilter.tsx";

export const operatorOptions: DropDownOption[] = [
    {value: ConditionOperator.CONTAINS, label: "Contains", icon: <FontAwesomeIcon icon={faMagnifyingGlass}/>},
    {value: ConditionOperator.STARTS_WITH, label: "Starts With", icon: <FontAwesomeIcon icon={faFont}/>},
    {value: ConditionOperator.ENDS_WITH, label: "Ends With", icon: <FontAwesomeIcon icon={faFont}/>},
    {value: ConditionOperator.EQUALS, label: "Equals", icon: <FontAwesomeIcon icon={faFont}/>},
];