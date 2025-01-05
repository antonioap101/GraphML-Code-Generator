import React, {useState} from 'react';
import DropDownComponent, {DropDownOption} from "../../components/dropDown/DropDownComponent.tsx";
import {dbmsOptions} from "../../constants/AllowedDBMS.tsx";
import {AllowedLanguages, languageExamples, languageOptions} from "../../constants/AllowedLanguages.tsx";
import GenerateButton from "../../components/buttons/generateButton/GenerateButton.tsx";
import AceIDEComponent from "../../components/aceIde/AceIDEComponent.tsx";
import TableAttributeEditor from "../../components/tableAttributeEditor/tableAttributeEditor.tsx";
import styles from "./CRUDCodeGenerator.module.css";

const CRUDCodeGenerator: React.FC = () => {
    const [code, setCode] = useState(languageExamples[AllowedLanguages.Java]);
    const [selectedLanguage, setSelectedLanguage] = useState<DropDownOption>(languageOptions[1]);
    const [selectedDBMS, setSelectedDBMS] = useState<DropDownOption>(dbmsOptions[0]);

    const handleLanguageChange = (language: DropDownOption) => {
        setSelectedLanguage(language);
        setCode(languageExamples[language.value as AllowedLanguages]);
    };

    const handleConvert = () => {
        console.log("Convert button clicked");
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
                <GenerateButton onClick={handleConvert} disabled={false} loading={false} horizontal={true} />
            </nav>
            <section className={styles.mainSection}>
                <section className={styles.outputSection}>
                    <h3>Output</h3>
                    <TableAttributeEditor />
                </section>
                <aside className={styles.codeSection}>
                    <h3>Code</h3>
                    <AceIDEComponent code={code} setCode={setCode} language={selectedLanguage.label} />
                </aside>
            </section>
        </div>
    );
};

export default CRUDCodeGenerator;