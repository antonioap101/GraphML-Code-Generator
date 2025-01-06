export enum TypeEnum {
    NUMBER = "number",
    TEXT = "string",
    BOOLEAN = "boolean",
    FLOAT = "float",
    DOUBLE = "double",
}

// Type enum with labels and values (labels first letter capitalized)
export const TypeEnumLabels: { [key in TypeEnum]: string } = {
    [TypeEnum.NUMBER]: "Number",
    [TypeEnum.TEXT]: "String",
    [TypeEnum.BOOLEAN]: "Boolean",
    [TypeEnum.FLOAT]: "Float",
    [TypeEnum.DOUBLE]: "Double",
};