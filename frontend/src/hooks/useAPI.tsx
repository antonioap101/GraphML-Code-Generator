import React, {createContext, ReactNode, useContext,  useState} from "react";
import ApiService from "../services/apiService";
import {CRUDCodeGeneratorInput} from "../constants/CRUDCodeGeneratorInput.ts";

// Define el tipo para el contexto de la API
interface ApiContextType {
    convertXmlToGraphml: (xmlContent: string) => Promise<void>;
    generateCrud: (crudInput: CRUDCodeGeneratorInput) => Promise<void>;
    graphmlOutput: string;
    crudOutput: string;
    loading: boolean;
    error: string | null;
}

// Crear el contexto
const ApiContext = createContext<ApiContextType | null>(null);

// Proveedor del contexto
export const ApiProvider: React.FC<{ children: ReactNode }> = ({children}) => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [graphmlOutput, setGraphmlOutput] = useState<string>("");
    const [crudOutput, setCrudOutput] = useState<string>("");



    const convertXmlToGraphml = async (xmlContent: string) => {
        setLoading(true);
        setError(null);
        try {
            const result = await ApiService.convertXmlToGraphml(xmlContent);
            setGraphmlOutput(result.graphml);
        } catch (err) {
            setError((err as Error).message || "Unknown error occurred.");
        } finally {
            setLoading(false);
        }
    };

    const generateCrud = async (crudInput: CRUDCodeGeneratorInput) => {
        setLoading(true);
        setError(null);
        try {
            const result = await ApiService.generateCrud(crudInput);
            setCrudOutput(result.code); // Ajusta según la respuesta del backend
        } catch (err) {
            setError((err as Error).message || "Unknown error occurred.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <ApiContext.Provider
            value={{
                convertXmlToGraphml, generateCrud, graphmlOutput, crudOutput, loading, error,
            }}
        >
            {children}
        </ApiContext.Provider>
    );
};

// Hook para consumir el contexto
export const useApi = (): ApiContextType => {
    const context = useContext(ApiContext);
    if (!context) {
        throw new Error("useApi must be used within an ApiProvider");
    }
    return context;
};
