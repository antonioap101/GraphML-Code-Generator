import React from "react";
import {TypeEnum} from "../../../constants/TypeEnum.ts";
import {FieldModel} from "../../../constants/FieldModel.ts";
import {faTrashAlt} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

interface TableRowProps {
    field: FieldModel;
    index: number;
    isPrimaryKeyDisabled?: boolean;
    onFieldChange: (index: number, key: keyof FieldModel, value: FieldModel[keyof FieldModel]) => void;
    onRemove?: () => void; // Opcional, solo para filas que pueden eliminarse
}

const TableRow: React.FC<TableRowProps> = ({field, index, isPrimaryKeyDisabled, onFieldChange, onRemove}) => {
    return (
        <div className="table-row">
            <div className="table-cell">
                <input
                    type="text"
                    value={field.name}
                    onChange={(e) => onFieldChange(index, "name", e.target.value)}
                    required
                />
            </div>
            <div className="table-cell">
                <select
                    value={field.type.toUpperCase()}
                    onChange={(e) => onFieldChange(index, "type", e.target.value as TypeEnum)}
                >
                    {Object.values(TypeEnum).map((type) => (
                        <option key={type} value={type}>
                            {type.toUpperCase()}
                        </option>
                    ))}
                </select>
            </div>
            <div className="table-cell">
                <input
                    type="checkbox"
                    checked={field.nullable}
                    onChange={(e) => onFieldChange(index, "nullable", e.target.checked)}
                />
            </div>
            <div className="table-cell">
                <input
                    type="checkbox"
                    checked={field.unique}
                    onChange={(e) => onFieldChange(index, "unique", e.target.checked)}
                />
            </div>
            <div className="table-cell">
                <input
                    type="checkbox"
                    checked={field.autoIncrement}
                    onChange={(e) => onFieldChange(index, "autoIncrement", e.target.checked)}
                    disabled={!field.primaryKey}
                />
            </div>
            <div className="table-cell">
                <input
                    type="checkbox"
                    checked={field.primaryKey}
                    onChange={(e) => onFieldChange(index, "primaryKey", e.target.checked)}
                    disabled={isPrimaryKeyDisabled}
                />
            </div>

            <div className="table-cell">
                <button className={"field-button"}
                    disabled={onRemove === undefined}
                    onClick={onRemove}>
                    <FontAwesomeIcon icon={faTrashAlt}/>
                </button>
            </div>

        </div>
    );
};

export default TableRow;
