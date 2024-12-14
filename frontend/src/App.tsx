import React, { useState } from 'react';
import './App.css';

const App: React.FC = () => {
    const [xmlContent, setXmlContent] = useState('');
    const [graphmlOutput, setGraphmlOutput] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files[0]) {
            const fileReader = new FileReader();
            fileReader.onload = (e) => {
                setXmlContent(e.target?.result as string);
            };
            fileReader.readAsText(event.target.files[0]);
        }
    };

    const handleConvert = async () => {
        setLoading(true);
        setError('');
        try {
            const response = await fetch('/convert/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ xml_content: xmlContent }),
            });
            const data = await response.json();
            if (response.ok) {
                setGraphmlOutput(data.graphml);
            } else {
                setError(data.detail || 'Error al convertir el archivo.');
            }
        } catch (error) {
            setError("Error de conexión con el servidor.");
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    const handleDownload = () => {
        const blob = new Blob([graphmlOutput], { type: 'application/xml' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'output.graphml';
        link.click();
    };

    return (
        <div className="app-container">
            <h1>Convertidor XML a GraphML</h1>
            <div className="form-container">
                <textarea
                    value={xmlContent}
                    onChange={(e) => setXmlContent(e.target.value)}
                    placeholder="Escribe o pega aquí el contenido XML..."
                />
                <input type="file" accept=".xml" onChange={handleFileUpload} />
                <button onClick={handleConvert} disabled={loading || !xmlContent}>
                    {loading ? 'Convirtiendo...' : 'Convertir'}
                </button>
                {error && <p className="error">{error}</p>}
            </div>
            <div className="output-container">
                <textarea value={graphmlOutput} readOnly placeholder="El resultado en GraphML aparecerá aquí..." />
                <button onClick={handleDownload} disabled={!graphmlOutput}>
                    Descargar como .graphml
                </button>
            </div>
        </div>
    );
};

export default App;
