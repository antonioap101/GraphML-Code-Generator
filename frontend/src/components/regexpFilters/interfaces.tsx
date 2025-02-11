import {DropDownOption} from "../dropDown/DropDownComponent.tsx";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faLayerGroup} from "@fortawesome/free-solid-svg-icons";
import {ConditionOperator} from "../../hooks/useFilter.tsx";

export const operatorOptions: DropDownOption[] = [
    {value: ConditionOperator.CONTAINS, label: "Contains", icon: <FontAwesomeIcon icon={faLayerGroup}/>},
    {value: ConditionOperator.NOT_CONTAINS, label: "Does not Contain", icon: <FontAwesomeIcon icon={faLayerGroup}/>},
    {value: ConditionOperator.STARTS_WITH, label: "Starts With", icon: <FontAwesomeIcon icon={faLayerGroup}/>},
    {value: ConditionOperator.NOT_STARTS_WITH, label: "Does not Start With", icon: <FontAwesomeIcon icon={faLayerGroup}/>},
    {value: ConditionOperator.ENDS_WITH, label: "Does not End With", icon: <FontAwesomeIcon icon={faLayerGroup}/>},
    {value: ConditionOperator.NOT_ENDS_WITH, label: "Ends With", icon: <FontAwesomeIcon icon={faLayerGroup}/>},
    {value: ConditionOperator.EQUALS, label: "Equals", icon: <FontAwesomeIcon icon={faLayerGroup}/>},
    {value: ConditionOperator.NOT_EQUALS, label: "Does not Equal", icon: <FontAwesomeIcon icon={faLayerGroup}/>},
    {value: ConditionOperator.GREATER_THAN, label: "Greater Than", icon: <FontAwesomeIcon icon={faLayerGroup}/>},
    {value: ConditionOperator.LESS_THAN, label: "Less Than", icon: <FontAwesomeIcon icon={faLayerGroup}/>}
];