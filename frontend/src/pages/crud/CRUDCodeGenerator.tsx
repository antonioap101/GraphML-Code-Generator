import React, {useEffect, useState} from "react";
import DropDownComponent, {DropDownOption} from "../../components/dropDown/DropDownComponent.tsx";
import {AllowedDBMS, dbmsOptions} from "../../constants/AllowedDBMS.tsx";
import {AllowedLanguages, languageExamples, languageOptions} from "../../constants/AllowedLanguages.tsx";
import GenerateButton from "../../components/buttons/generateButton/GenerateButton.tsx";
import AceIDEComponent from "../../components/aceIde/AceIDEComponent.tsx";
import TableAttributeEditor from "../../components/tableAttributeEditor/tableAttributeEditor.tsx";
import {
    ConnectionParameters,
    createCRUDCodeGeneratorInput,
    FieldModel,
} from "../../constants/CRUDCodeGeneratorInput.ts";
import styles from "./CRUDCodeGenerator.module.css";
import {useApi} from "../../hooks/useAPI.tsx";
import CopyButton from "../../components/buttons/copyButton/CopyButton.tsx";

import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCode, faFont, faGear, faLayerGroup, faSignal, faTableList} from "@fortawesome/free-solid-svg-icons";
import ConnectionParametersPopup from "../../components/popUps/conectionParametersPopup/ConnectionParametersPopUp.tsx";
import {TypeEnum} from "../../constants/TypeEnum.ts";

const CRUDCodeGenerator: React.FC = () => {
    const [code, setCode] = useState(languageExamples[AllowedLanguages.Java]);
    const [selectedLanguage, setSelectedLanguage] = useState<DropDownOption>(languageOptions[1]);
    const [selectedDBMS, setSelectedDBMS] = useState<DropDownOption>(dbmsOptions[0]);
    const [connectionParams, setConnectionParams] = useState<ConnectionParameters>({
        host: "localhost",
        port: 3000,
        database_name: "default"
    });
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [activeTab, setActiveTab] = useState("schema"); // Estado para controlar la pestaña activa
    const [tableName, setTableName] = useState(""); // Estado para el nombre de la tabla

    const [localError, setLocalError] = useState<string | null>(null);
    const {loading, error, crudOutput, generateCrud} = useApi();

    const [fields, setFields] = useState<FieldModel[]>([
        {
            name: "id",
            type: TypeEnum.NUMBER,
            primaryKey: true,
            autoIncrement: true,
            nullable: false,
            unique: true,
        },
    ]);


    useEffect(() => {
        if (!error || error === "") setLocalError(null);
        if (error) setLocalError(localError + "\n" + error);
    }, [error]);


    useEffect(() => {
        if (crudOutput && crudOutput.length > 0) {
            setCode(crudOutput);
        } else {
            setCode(languageExamples[selectedLanguage.value as AllowedLanguages]);
        }
    }, [crudOutput, selectedLanguage]);

    const handleLanguageChange = (language: DropDownOption) => {
        setSelectedLanguage(language);
        if (!crudOutput) {
            setCode(languageExamples[language.value as AllowedLanguages]);
        }
    };

    const handleConvert = async () => {
        try {
            console.log("Convert button clicked");
            console.log("Fields:", fields);
            console.log("Params:", connectionParams);

            if (!tableName || tableName.length === 0) {
                throw new Error("Table name is required");
            }

            if (tableName.toLowerCase() == "table") {
                throw new Error(`Table name cannot be ${tableName}`);
            }

            await generateCrud(createCRUDCodeGeneratorInput(
                {name: tableName, fields: fields},
                selectedLanguage.value as AllowedLanguages,
                selectedDBMS.value as AllowedDBMS,
                connectionParams
            ));
        } catch (e: any) {
            setLocalError(e.message);
            console.error("Error generating CRUD code:", e);
        }
    };

    return (
        <div className={styles.container}>

            <section className={styles.mainSection}>
                <aside className={styles.inputSection}>
                    <header className={styles.codeHeader}>
                        <a className={styles.codeLink}>
                            <FontAwesomeIcon icon={faLayerGroup}/>
                            <h2>Data Model</h2>
                        </a>
                        <GenerateButton onClick={handleConvert} disabled={false} loading={loading} horizontal={true}/>
                    </header>

                    <div className={styles.tabs}>
                        <div className={styles.tabTableName}>
                            <FontAwesomeIcon icon={faFont}/>
                            <input
                                type="text"
                                value={tableName}
                                onChange={(e) => setTableName(e.target.value)}
                                className={styles.tableNameInput}
                                placeholder="Enter table name"
                            />
                        </div>
                        <div className={styles.tabButtons}>
                            <button
                                className={`${styles.sectionSelectionButton} ${activeTab === "schema" ? styles.activeTab : ""}`}
                                onClick={() => setActiveTab("schema")}
                            >
                                <FontAwesomeIcon icon={faTableList}/>
                                Schema
                            </button>
                            <button
                                className={`${styles.sectionSelectionButton} ${activeTab === "config" ? styles.activeTab : ""}`}
                                onClick={() => setActiveTab("config")}
                            >
                                <FontAwesomeIcon icon={faGear}/>
                                Config
                            </button>
                        </div>
                    </div>

                    <form className={styles.content}>
                        {activeTab === "schema" && (
                            <section className={styles.tableSection}>
                                <TableAttributeEditor fields={fields} setFields={setFields}/>
                            </section>
                        )}

                        {activeTab === "config" && (
                            <section>
                                <nav className={styles.nav}>
                                    <div style={{display: "flex", gap: "10px"}}>
                                        <DropDownComponent
                                            selectedOption={selectedDBMS}
                                            options={dbmsOptions}
                                            onSelect={setSelectedDBMS}
                                            placeholder="Select DBMS"
                                        />
                                        <DropDownComponent
                                            selectedOption={selectedLanguage}
                                            options={languageOptions}
                                            onSelect={handleLanguageChange}
                                            placeholder="Select Language"
                                        />
                                    </div>
                                    <button
                                        type="button"
                                        className={styles.connectionButton} onClick={() => {
                                        setIsPopupOpen(true)
                                    }}>
                                        <FontAwesomeIcon icon={faSignal}/>
                                    </button>
                                </nav>
                            </section>
                        )}
                    </form>
                </aside>

                <aside className={styles.codeSection}>
                    <header className={styles.codeHeader}>
                        <a className={styles.codeLink}>
                            <FontAwesomeIcon icon={faCode}/>
                            <h2>Code</h2>
                        </a>
                        <CopyButton content={code}/>
                    </header>
                    {localError && <p className="error">{localError}</p>}
                    <AceIDEComponent code={code} setCode={setCode} language={selectedLanguage.value}/>
                </aside>
            </section>

            {isPopupOpen && (
                <ConnectionParametersPopup
                    parameters={connectionParams}
                    setParameters={setConnectionParams}
                    onClose={() => setIsPopupOpen(false)}
                />
            )}
        </div>
    );
};

export default CRUDCodeGenerator;
