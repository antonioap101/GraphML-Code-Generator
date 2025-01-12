// TableAttributeEditor.tsx
import React from "react";
import styles from "./tableAttributeEditor.module.css";
import {TypeEnum} from "../../constants/TypeEnum";
import {FieldModel} from "../../constants/CRUDCodeGeneratorInput.ts";
import TableRow from "./rows/TableRow.tsx";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faArrowRotateLeft, faPlus} from "@fortawesome/free-solid-svg-icons";

interface TableAttributeEditorProps {
    language: string;
    fields: FieldModel[];
    setFields: (fields: FieldModel[]) => void;
}

const TableAttributeEditor: React.FC<TableAttributeEditorProps> = ({language, fields, setFields}) => {
    const handleFieldChange = <K extends keyof FieldModel>(
        index: number,
        key: K,
        value: FieldModel[K]
    ) => {
        const updatedFields = [...fields];
        updatedFields[index][key] = value;
        setFields(updatedFields);
    };

    const addField = () => {
        setFields([
            ...fields,
            {name: "", type: TypeEnum.TEXT, nullable: true, unique: false, primaryKey: false, autoIncrement: false},
        ]);
    };

    const removeField = (index: number) => {
        const updatedFields = fields.filter((_, i) => i !== index);
        setFields(updatedFields);
    };

    return (
        <div className={styles.tableAttributeEditor}>
            <header className={styles.tableHeader}>
                <div className={styles.tableCell}>Name</div>
                <div className={styles.tableCell}>Type</div>
                <div className={styles.tableCell}>Nullable</div>
                <div className={styles.tableCell}>Unique</div>
                <div className={styles.tableCell}>
                    <button className={styles.fieldButton} onClick={addField}>
                        <FontAwesomeIcon icon={faPlus}/>
                    </button>
                    <button className={styles.fieldButton} onClick={() => setFields([])}>
                        <FontAwesomeIcon icon={faArrowRotateLeft}/>
                    </button>

                </div>
            </header>
            {fields.map((field, index) => (
                <TableRow
                    key={index}
                    field={field}
                    language={language}
                    index={index}
                    onFieldChange={handleFieldChange}
                    onRemove={index > 0 ? () => removeField(index) : undefined}
                />
            ))}
        </div>
    );
};

export default TableAttributeEditor;
