import {CRUDCodeGeneratorInput} from "../constants/CRUDCodeGeneratorInput.ts";

export interface ConvertResponse {
    graphml: string;
}

export interface ConvertError {
    detail: string;
}

class ApiService {
    private readonly baseUrl: string;

    constructor(baseUrl: string = "api") {
        this.baseUrl = baseUrl;
    }

    private async request<T>(endpoint: string, options: RequestInit): Promise<T> {
        const response = await fetch(`${this.baseUrl}/${endpoint}`, options);

        if (!response) {
            throw new Error("No response received from the server");
        }

        if (!response.ok) {
            const error: ConvertError = await response.json();
            throw new Error(error.detail || "An error occurred while processing the request");
        }

        return response.json();
    }

    async convertXmlToGraphml(xmlContent: string): Promise<ConvertResponse> {
        return this.request<ConvertResponse>("graphml/", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({xml_content: xmlContent}),
        });
    }

    async generateCrud(crudInput: CRUDCodeGeneratorInput): Promise<{ code: string }> {
        return this.request("crud/", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(crudInput),
        });
    }
}

export default new ApiService();
