// src/services/apiService.ts

export interface ConvertResponse {
    graphml: string;
}

export interface ConvertError {
    detail: string;
}

export const convertXmlToGraphml = async (xmlContent: string): Promise<ConvertResponse> => {
    const response = await fetch('api/graphml/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ xml_content: xmlContent }),
    });

    if (!response) {
        throw new Error('Error converting the file (no response)');
    }

    if (!response.ok) {
        const error: ConvertError = await response.json();
        throw new Error(error.detail || 'Error converting the file');
    }

    return response.json();
};
