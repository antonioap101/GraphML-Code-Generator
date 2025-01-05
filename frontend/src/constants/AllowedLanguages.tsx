import {DropDownOption} from "../components/dropDown/DropDownComponent.tsx";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCode} from "@fortawesome/free-solid-svg-icons";

export enum AllowedLanguages {
    TypeScript = "Typescript",
    Java = "Java",
    CSharp = "C#"
}


export const languageOptions: DropDownOption[] = Object.values(AllowedLanguages).map((language) => ({
    value: language,
    label: language.toLowerCase(),
    icon: <FontAwesomeIcon icon={faCode} />,
}));

export const languageExamples: Record<AllowedLanguages, string> = {
    [AllowedLanguages.TypeScript]: `// TypeScript Example
console.log("Hello, World!");`,
    [AllowedLanguages.Java]: `// Java Example
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}`,
    [AllowedLanguages.CSharp]: `// C# Example
using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}`,
};

