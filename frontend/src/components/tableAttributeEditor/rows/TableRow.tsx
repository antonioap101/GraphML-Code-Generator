import React, {useState} from "react";
import {TypeEnum} from "../../../constants/TypeEnum.ts";
import {FieldModel} from "../../../constants/CRUDCodeGeneratorInput.ts";
import {faCog, faTrashAlt} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import styles from "../tableAttributeEditor.module.css";
import "./TableRow.css";
import ExtraSettingsPopup from "../../popUps/extraSettingsPopUp/extraSettingsPopUp.tsx"; // Importamos los estilos específicos

interface TableRowProps {
    field: FieldModel;
    index: number;
    onFieldChange: (index: number, key: keyof FieldModel, value: FieldModel[keyof FieldModel]) => void;
    onRemove?: () => void; // Optional, only for rows that can be removed
}

const TableRow: React.FC<TableRowProps> = ({field, index, onFieldChange, onRemove}) => {
    const [isExtraSettingsPopUpOpen, setIsExtraSettingsPopUpOpen] = useState(false);
    return (
        <div className={styles.tableRow}>
            <div className={styles.tableCell}>
                <input
                    type="text"
                    value={field.name}
                    onChange={(e) => onFieldChange(index, "name", e.target.value)}
                    required
                />
            </div>
            <div className={styles.tableCell}>
                <select
                    value={field.type}
                    onChange={(e) => onFieldChange(index, "type", e.target.value as TypeEnum)}
                >
                    {Object.values(TypeEnum).map((type) => (
                        <option key={type} value={type}>
                            {type.toUpperCase()}
                        </option>
                    ))}
                </select>
            </div>
            <div className={styles.tableCell}>
                <input
                    type="checkbox"
                    className={styles.checkbox} // Aplicamos la clase personalizada
                    checked={field.nullable}
                    onChange={(e) => onFieldChange(index, "nullable", e.target.checked)}
                />
            </div>
            <div className={styles.tableCell}>
                <input
                    type="checkbox"
                    className={styles.checkbox} // Aplicamos la clase personalizada
                    checked={field.unique}
                    onChange={(e) => onFieldChange(index, "unique", e.target.checked)}
                />
            </div>
            <div className={styles.tableCell} style={{gap: 5}}>
                {/* Ajustes adicionales */}
                <button
                    className={styles.fieldButton}
                    disabled={index === 0} // Deshabilitar para la primera fila
                    onClick={() => setIsExtraSettingsPopUpOpen(true)}
                >
                    <FontAwesomeIcon icon={faCog}/>
                </button>
                {/* Eliminar fila */}
                <button
                    className={styles.fieldButton}
                    disabled={onRemove === undefined}
                    onClick={onRemove}
                >
                    <FontAwesomeIcon icon={faTrashAlt}/>
                </button>
            </div>
            {/* Mostrar el popup si está abierto */}
            {isExtraSettingsPopUpOpen && (
                <ExtraSettingsPopup
                    field={field}
                    setValidations={(validations) => onFieldChange(index, "validations", validations)}
                    onClose={() => setIsExtraSettingsPopUpOpen(false)}
                />
            )}
        </div>
    );
};

export default TableRow;
