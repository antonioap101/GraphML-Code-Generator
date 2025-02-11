// src/App.tsx
import React from 'react';
import './GraphMLCodeGenerator.css';
import {useApi} from "../../hooks/useAPI.tsx";
import GraphmlOutput from "../../components/textInputOutput/GraphmlOutput.tsx";
import XmlInput from "../../components/textInputOutput/XMLInput.tsx";
import ActionButton from "../../components/buttons/actionButton/ActionButton.tsx";


const GraphMLCodeGenerator: React.FC = () => {
    const [xmlContent, setXmlContent] = React.useState('');
    const {loading, apiError, graphmlOutput, convertXmlToGraphml} = useApi();

    const handleFileUpload = (file: File) => {
        const fileReader = new FileReader();
        fileReader.onload = (e) => {
            setXmlContent(e.target?.result as string);
        };
        fileReader.readAsText(file);
    };

    const handleConvert = () => {
        convertXmlToGraphml(xmlContent);
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
                    <ActionButton
                        placeholders={{loading: 'Converting...', default: 'Convert'}}
                        onClick={handleConvert}
                        disabled={loading || !xmlContent}
                        loading={loading}
                    />
                    {apiError && <p className="error">{apiError}</p>}

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
