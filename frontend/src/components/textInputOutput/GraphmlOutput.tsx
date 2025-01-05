import React from 'react';
import UploadOrDownloadButton from "../uploadOrDownloadButton/uploadOrDownloadButton.tsx";


interface GraphmlOutputProps {
    graphmlOutput: string;
    onDownload: () => void;
}

const GraphmlOutput: React.FC<GraphmlOutputProps> = ({graphmlOutput, onDownload}) => {
    return (
        <div className="textarea-container">
            <textarea value={graphmlOutput} readOnly placeholder="El resultado en GraphML aparecerá aquí..."/>
            <div className="download-button">
                <UploadOrDownloadButton action="download" onClick={onDownload} tooltip="Descargar como .graphml"/>
            </div>
        </div>
    );
};

export default GraphmlOutput;
