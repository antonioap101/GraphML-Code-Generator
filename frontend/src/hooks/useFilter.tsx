import {createContext, ReactNode, useContext, useState} from "react";
import {v4 as uuidv4} from 'uuid';

// Enums
export enum FilterConditionType {
    TEXT = "TEXT",
    NUMBER = "NUMBER"
}

export enum ConditionOperator {
    STARTS_WITH = "STARTS_WITH",
    NOT_STARTS_WITH = "NOT_STARTS_WITH",
    ENDS_WITH = "ENDS_WITH",
    NOT_ENDS_WITH = "NOT_ENDS_WITH",
    CONTAINS = "CONTAINS",
    NOT_CONTAINS = "NOT_CONTAINS",
    EQUALS = "EQUALS",
    NOT_EQUALS = "NOT_EQUALS",
    GREATER_THAN = "GREATER_THAN",
    LESS_THAN = "LESS_THAN",
}

// Interfaces y clases
interface Serializable {
    toJSON(): any;
}

export class Condition implements Serializable {
    public readonly id: string;

    constructor(
        public field: string,
        public _operator: ConditionOperator,
        public value: string | number | Date,
        public type: FilterConditionType
    ) {
        this.id = uuidv4();
    }


    get operator(): ConditionOperator {
        return this._operator;
    }

    set operator(value: ConditionOperator) {
        this._operator = value;
        switch (value) {
            case ConditionOperator.STARTS_WITH:
            case ConditionOperator.NOT_STARTS_WITH:
            case ConditionOperator.ENDS_WITH:
            case ConditionOperator.NOT_ENDS_WITH:
            case ConditionOperator.CONTAINS:
            case ConditionOperator.NOT_CONTAINS:
            case ConditionOperator.EQUALS:
            case ConditionOperator.NOT_EQUALS:
                this.type = FilterConditionType.TEXT;
                break;
            case ConditionOperator.GREATER_THAN:
            case ConditionOperator.LESS_THAN:
                this.type = FilterConditionType.NUMBER;
                break;
            default:
                throw new Error(`Unsupported operator: ${value}`);
        }
    }


// Regex generation for each operator
    toRegex(): string {
        const escapedValue = typeof this.value === "string"
            ? this.value.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&')  // Escape regex special characters
            : this.value.toString();

        switch (this._operator) {
            case ConditionOperator.STARTS_WITH:
                return `^${escapedValue}`;
            case ConditionOperator.NOT_STARTS_WITH:
                return `^(?!${escapedValue}).*`;
            case ConditionOperator.ENDS_WITH:
                return `${escapedValue}$`;
            case ConditionOperator.NOT_ENDS_WITH:
                return `^(?!.*${escapedValue}$).*`;
            case ConditionOperator.CONTAINS:
                return `${escapedValue}`;
            case ConditionOperator.NOT_CONTAINS:
                return `^(?!.*${escapedValue}).*`;
            case ConditionOperator.EQUALS:
                return `^${escapedValue}$`;
            case ConditionOperator.NOT_EQUALS:
                return `^(?!${escapedValue}).*`;
            case ConditionOperator.GREATER_THAN:
                return `(?<!\\d)\\d{${escapedValue}}.*`;  // For number-specific regex (may require tweaking)
            case ConditionOperator.LESS_THAN:
                return `.*(?!\\d{${escapedValue}}).*`;   // For number-specific regex
            default:
                throw new Error(`Unsupported operator: ${this._operator}`);
        }
    }

    toJSON() {
        return {
            id: this.id,
            field: this.field,
            operator: this._operator,
            value: this.value,
            type: this.type,
        };
    }
}

export class GroupCondition implements Serializable {
    public readonly id: string;
    private _conditions: (Condition | GroupCondition)[] = [];
    private _combinator: "AND" | "OR";

    constructor(combinator: "AND" | "OR") {
        this.id = uuidv4();
        this._combinator = combinator;
        this.conditions = [];
    }

    get conditions(): (Condition | GroupCondition)[] {
        return this._conditions;
    }

    set conditions(value: (Condition | GroupCondition)[]) {
        this._conditions = value;
    }

    get combinator(): "AND" | "OR" {
        return this._combinator;
    }

    set combinator(value: "AND" | "OR") {
        this._combinator = value;
    }

    addCondition(condition: Condition | GroupCondition): void {
        this._conditions.push(condition);
    }

    updateCondition(updatedCondition: Condition | GroupCondition): void {
        const index = this._conditions.findIndex(cond => cond.id === updatedCondition.id);
        if (index !== -1) {
            this._conditions[index] = updatedCondition;
        }
    }

    deleteCondition(targetId: string): void {
        const index = this._conditions.findIndex(cond => cond.id === targetId);
        if (index !== -1) {
            this._conditions.splice(index, 1);
        }
    }

    clone(): GroupCondition {
        const clone = new GroupCondition(this._combinator);
        clone.conditions = this._conditions.map((condition) => {
            if (condition instanceof Condition) {
                return new Condition(condition.field, condition.operator, condition.value, condition.type);
            } else {
                return condition.clone();
            }
        });
        return clone;
    }

    toRegex(): string {
        const regexParts = this._conditions.map(condition => {
            if (condition instanceof Condition) {
                return condition.toRegex();
            } else {
                return condition.toRegex();  // Recursively handle nested groups
            }
        });

        // Combine regex parts based on the combinator
        const separator = this._combinator === "AND" ? "" : "|";  // AND means concatenation, OR means alternation
        return `(?:${regexParts.join(separator)})`;
    }

    toJSON() {
        return {
            id: this.id,
            combinator: this._combinator,
            conditions: this._conditions.map((condition) => condition.toJSON()),
        };
    }
}

// The provider to wrap the app or components needing access to the filter context
export const FilterProvider = ({children}: { children: ReactNode }) => {
    const [filters, setFilters] = useState<GroupCondition>(new GroupCondition("AND"));

    const addCondition = (parentGroup: GroupCondition, newCondition: Condition | GroupCondition) => {
        console.warn("Adding new condition", newCondition, "to parent group", parentGroup);
        parentGroup.addCondition(newCondition);
        setFilters(filters.clone());
    };


    const deleteCondition = (parentGroup: GroupCondition, target: Condition | GroupCondition) => {
        console.warn("Deleting condition", target);
        parentGroup.deleteCondition(target.id);
        setFilters(filters.clone());
    };

    const updateCondition = (parentGroup: GroupCondition, updatedCondition: Condition | GroupCondition) => {
        console.warn("Updating condition", updatedCondition);
        parentGroup.updateCondition(updatedCondition);
        setFilters(filters.clone());
    };


    const resetAll = () => {
        console.warn("Resetting all filters");
        setFilters(new GroupCondition("AND"));

        console.warn("Filters after reset", filters);
    }

    return (
        <FilterContext.Provider
            value={{
                filters,
                addCondition,
                deleteCondition,
                updateCondition,
                resetAll,
            }}
        >
            {children}
        </FilterContext.Provider>
    );
};

interface FilterContextType {
    filters: GroupCondition;
    addCondition: (parentGroup: GroupCondition, newCondition: Condition | GroupCondition) => void;
    deleteCondition: (parentGroup: GroupCondition, target: Condition | GroupCondition) => void;
    updateCondition: (parentGroup: GroupCondition, updatedCondition: Condition | GroupCondition) => void;
    resetAll: () => void;
}

// Create the context with a default value
const FilterContext = createContext<FilterContextType | undefined>(undefined);

// Custom hook to use the FilterContext
export const useFilterContext = (): FilterContextType => {
    const context = useContext(FilterContext);
    if (!context) {
        throw new Error("useFilterContext must be used within a FilterProvider");
    }
    return context;
};