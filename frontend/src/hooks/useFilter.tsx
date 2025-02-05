import { useState } from "react";

// Enums
export enum FilterConditionType {
    TEXT = "TEXT",
    NUMBER = "NUMBER",
    DATE = "DATE",
}

export enum ConditionOperator {
    STARTS_WITH = "STARTS_WITH",
    ENDS_WITH = "ENDS_WITH",
    CONTAINS = "CONTAINS",
    EQUALS = "EQUALS",
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
        public operator: ConditionOperator,
        public value: string | number | Date,
        public type: FilterConditionType = FilterConditionType.TEXT
    ) {
        this.id = crypto.randomUUID();
    }

    toJSON() {
        return {
            id: this.id,
            field: this.field,
            operator: this.operator,
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
        this.id = crypto.randomUUID();
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

    toJSON() {
        return {
            id: this.id,
            combinator: this._combinator,
            conditions: this._conditions.map((condition) => condition.toJSON()),
        };
    }
}

// Hook con mutaciones profundas
export const useFilter = () => {
    const [filters, setFilters] = useState<GroupCondition>(new GroupCondition("AND"));

    const addCondition = (parentGroup: GroupCondition, newCondition: Condition | GroupCondition) => {
        console.warn("Adding new condition", newCondition, "to parent group", parentGroup);

        // Mutamos directamente el grupo padre
        parentGroup.addCondition(newCondition);

        console.warn("Parent group after addition", parentGroup);

        // Forzamos la actualización al clonar todo el estado de la raíz
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


    const resetAll = () => setFilters(new GroupCondition("AND"));

    return {
        filters,
        addCondition,
        deleteCondition,
        updateCondition,
        resetAll
    };
};


