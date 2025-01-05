// src/App.tsx
import React from 'react';
import './GraphMLCodeGenerator.css';
import {useConvert} from "../../hooks/useXMLToGraphml.ts";
import GraphmlOutput from "../../components/textInputOutput/GraphmlOutput.tsx";
import XmlInput from "../../components/textInputOutput/XMLInput.tsx";
import GenerateButton from "../../components/buttons/generateButton/GenerateButton.tsx";


const GraphMLCodeGenerator: React.FC = () => {
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
                    <GenerateButton
                        onClick={handleConvert}
                        disabled={loading || !xmlContent}
                        loading={loading}
                    />
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

export default GraphMLCodeGenerator;
