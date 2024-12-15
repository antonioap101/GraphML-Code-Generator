import {useState} from 'react';
import {convertXmlToGraphml} from "../services/apiService.ts";



export const useConvert = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [graphmlOutput, setGraphmlOutput] = useState('');

    const convert = async (xmlContent: string) => {
        setLoading(true);
        setError('');
        try {
            const result = await convertXmlToGraphml(xmlContent);
            setGraphmlOutput(result.graphml);
        } catch (err) {
            setError((err as Error).message || 'Error desconocido.');
        } finally {
            setLoading(false);
        }
    };

    return {loading, error, graphmlOutput, convert};
};
