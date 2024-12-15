// src/App.tsx
import React from 'react';
import '@/App.css';
import {useConvert} from "./hooks/useXMLToGraphml.ts";
import ThemeToggleButton from "./components/themeToggleButton/ThemeToggleButton.tsx";
import HelpButton from "./components/helpButton/helpButtonAndPopUp.tsx";
import GraphmlOutput from "./components/text-input-output/GraphmlOutput.tsx";
import XmlInput from "./components/text-input-output/XMLInput.tsx";
import {FaCode} from "react-icons/fa";
import AuthorLink from "./components/authorLink/AuthorLink.tsx";


const App: React.FC = () => {
    const [xmlContent, setXmlContent] = React.useState('');
    const {loading, error, graphmlOutput, convert} = useConvert();

    const handleFileUpload = (file: File) => {
        console.log("file", file)
        const fileReader = new FileReader();
        fileReader.onload = (e) => {
            setXmlContent(e.target?.result as string);
        };
        fileReader.readAsText(file);
    };

    const handleConvert = () => {
        convert(xmlContent);
    };

    const handleDownload = () => {
        const blob = new Blob([graphmlOutput], {type: 'application/xml'});
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'output.graphml';
        link.click();
    };

    return (
        <div className="app-container">
            <h1>Generador de Código GraphML</h1>
            <div style={{
                zIndex: 1000
            }}>
                <AuthorLink/>
            </div>
            <div style={{
                zIndex: 1000, position: 'fixed', top: 20, right: 20, display: 'flex', gap: '10px'
            }}>
                <ThemeToggleButton/>
                <HelpButton/>
            </div>
            <div className="form-container">
                <XmlInput
                    xmlContent={xmlContent}
                    onXmlChange={setXmlContent}
                    onFileUpload={handleFileUpload}
                />
                <div style={{
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                    gap: '20px'
                }}>
                    <button onClick={handleConvert} disabled={loading || !xmlContent}>
                        <FaCode size={20}/>
                        {loading ? 'Generando...' : 'Generar'}
                    </button>
                    {error && <p className="error">{error}</p>}

                </div>
                <GraphmlOutput
                    graphmlOutput={graphmlOutput}
                    onDownload={handleDownload}
                />
            </div>
        </div>
    );
};

export default App;
