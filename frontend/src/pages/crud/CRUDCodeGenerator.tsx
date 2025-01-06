import React, {useEffect, useState} from "react";
import DropDownComponent, {DropDownOption} from "../../components/dropDown/DropDownComponent.tsx";
import {AllowedDBMS, dbmsOptions} from "../../constants/AllowedDBMS.tsx";
import {AllowedLanguages, languageExamples, languageOptions} from "../../constants/AllowedLanguages.tsx";
import GenerateButton from "../../components/buttons/generateButton/GenerateButton.tsx";
import AceIDEComponent from "../../components/aceIde/AceIDEComponent.tsx";
import TableAttributeEditor from "../../components/tableAttributeEditor/tableAttributeEditor.tsx";
import {TypeEnum} from "../../constants/TypeEnum";
import {
    ConnectionParameters,
    createCRUDCodeGeneratorInput,
    FieldModel
} from "../../constants/CRUDCodeGeneratorInput.ts";
import styles from "./CRUDCodeGenerator.module.css";
import {useApi} from "../../hooks/useXMLToGraphml.tsx";
import CopyButton from "../../components/buttons/copyButton/CopyButton.tsx";
import ConnectionParametersForm from "../../components/connectionParametersForm/ConnectionParametersForm.tsx";

const CRUDCodeGenerator: React.FC = () => {
    const [code, setCode] = useState(languageExamples[AllowedLanguages.Java]);
    const [selectedLanguage, setSelectedLanguage] = useState<DropDownOption>(languageOptions[1]);
    const [selectedDBMS, setSelectedDBMS] = useState<DropDownOption>(dbmsOptions[0]);
    const [connectionParams, setConnectionParams] = useState<ConnectionParameters | undefined>(undefined);


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
                (connectionParams !== undefined) ? connectionParams : {host: "", port: 0, database_name: ""},
            ));
        } catch (e) {
            console.error("Error generating CRUD code:", e);
        }
    };

    return (
        <div className={styles.container}>
            <header>
                <h1>CRUD Code Generator</h1>
            </header>
            <nav className={styles.nav}>
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
                <GenerateButton onClick={handleConvert} disabled={false} loading={loading} horizontal={true}/>
            </nav>
            <section className={styles.mainSection}>
                <section className={styles.inputSection}>
                    <section className={styles.tableSection}>
                        <h3>Table Structure</h3>
                        <TableAttributeEditor fields={fields} setFields={setFields}/>
                    </section>
                    <section className={styles.connectionParams}>
                        <h3>Connection Parameters</h3>
                        <ConnectionParametersForm parameters={connectionParams} setParameters={setConnectionParams}/>
                    </section>
                </section>
                <aside className={styles.codeSection}>
                    <header style={{display: "flex", justifyContent: "center"}}>
                        <h3>Code</h3>
                        <CopyButton content={code}/>
                    </header>
                    {error && <p className={styles.error}>{error}</p>} {/* Mostrar error si existe */}
                    <AceIDEComponent code={code} setCode={setCode} language={selectedLanguage.value}/>
                </aside>
            </section>
        </div>
    );
};

export default CRUDCodeGenerator;
