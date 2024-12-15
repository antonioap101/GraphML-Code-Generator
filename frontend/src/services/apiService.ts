// src/services/apiService.ts

export interface ConvertResponse {
    graphml: string;
}

export interface ConvertError {
    detail: string;
}

export const convertXmlToGraphml = async (xmlContent: string): Promise<ConvertResponse> => {
    const response = await fetch('/convert/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ xml_content: xmlContent }),
    });

    if (!response.ok) {
        const error: ConvertError = await response.json();
        throw new Error(error.detail || 'Error al convertir el archivo.');
    }

    return response.json();
};
