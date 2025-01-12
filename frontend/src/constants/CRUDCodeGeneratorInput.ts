import {AllowedLanguages} from "./AllowedLanguages.tsx";
import {AllowedDBMS} from "./AllowedDBMS.tsx";
import {TypeEnum} from "./TypeEnum.ts";

export interface Validation {
    minLength?: number;
    maxLength?: number;
    pattern?: string;
    min?: number;
    max?: number;
    customCode?: string;
}


export interface FieldModel {
    name: string;
    type: TypeEnum;
    primaryKey?: boolean;
    autoIncrement?: boolean;
    nullable?: boolean;
    unique?: boolean;
    validations?: Validation;
}


export interface TableModel {
    name: string;
    fields: FieldModel[];
}

export interface ConnectionParameters {
    host: string;
    port: number;
    database_name: string;
}

export interface CRUDCodeGeneratorInput {
    table: TableModel;
    language: AllowedLanguages;
    dbms: AllowedDBMS;
    connectionParams: ConnectionParameters;
    customCode?: Record<string, string>;
}

export function createCRUDCodeGeneratorInput(
    table: TableModel,
    language: AllowedLanguages,
    dbms: AllowedDBMS,
    connectionParams: ConnectionParameters,
    customCode?: Record<string, string>
): CRUDCodeGeneratorInput {
    return {
        table,
        language,
        dbms,
        connectionParams,
        customCode,
    };
}