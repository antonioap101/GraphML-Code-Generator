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
import {useApi} from "../../hooks/useXMLToGraphml.tsx";
import CopyButton from "../../components/buttons/copyButton/CopyButton.tsx";

import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCode, faSignal, faTable} from "@fortawesome/free-solid-svg-icons";
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
    const [isPopupOpen, setIsPopupOpen] = useState(false); // Estado para manejar el popup

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

    // Efecto para sincronizar cambios en crudOutput
    useEffect(() => {
        if (crudOutput && crudOutput.length > 0) {
            setCode(crudOutput); // Si hay un CRUD generado, úsalo
        } else {
            setCode(languageExamples[selectedLanguage.value as AllowedLanguages]);
        }
    }, [crudOutput, selectedLanguage]); // Dependencia del lenguaje seleccionado y del CRUD generado

    const handleLanguageChange = (language: DropDownOption) => {
        setSelectedLanguage(language);
        // Actualiza el código de ejemplo al cambiar el lenguaje si no hay CRUD generado
        if (!crudOutput) {
            setCode(languageExamples[language.value as AllowedLanguages]);
        }
    };

    const handleConvert = async () => {
        try {
            console.log("Convert button clicked");
            console.log("Fields:", fields); // Access the rows from TableAttributeEditor here
            console.log("Params:", connectionParams); // Access the rows from TableAttributeEditor here

            await generateCrud(createCRUDCodeGeneratorInput(
                {name: "table", fields},
                selectedLanguage.value as AllowedLanguages,
                selectedDBMS.value as AllowedDBMS,
                connectionParams
            ));
        } catch (e) {
            console.error("Error generating CRUD code:", e);
        }
    };


    return (
        <div className={styles.container}>

            <section className={styles.mainSection}>
                <aside className={styles.inputSection}>
                    <header className={styles.codeHeader}>
                        <a className={styles.codeLink}>
                            <FontAwesomeIcon icon={faTable}/>
                            <h2>Table Details</h2>
                        </a>
                        <GenerateButton onClick={handleConvert} disabled={false} loading={loading} horizontal={true}/>
                    </header>
                    <form className={styles.content}>
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
                                    type="button" /* Avoid that the button submits the form */
                                    className={styles.connectionButton} onClick={() => {
                                    setIsPopupOpen(true)
                                }}>
                                    <FontAwesomeIcon icon={faSignal}/>
                                </button>
                            </nav>
                        </section>
                        <section className={styles.tableSection}>
                            <TableAttributeEditor fields={fields} setFields={setFields}/>
                        </section>
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
                    {error && <p className="error">{error}</p>}
                    <AceIDEComponent code={code} setCode={setCode} language={selectedLanguage.value}/>
                </aside>
            </section>

            {/* Popup para Connection Parameters */}
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
