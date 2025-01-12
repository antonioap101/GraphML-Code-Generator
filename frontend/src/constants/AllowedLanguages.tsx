import {DropDownOption} from "../components/dropDown/DropDownComponent.tsx";
import JavaIcon from "../assets/icons/devicon_java.svg";
import TypeScriptIcon from "../assets/icons/devicon_typescript.svg";
import PythonIcon from "../assets/icons/logos_python.svg";


export enum AllowedLanguages {
    TypeScript = "Typescript",
    Java = "Java",
    Python = "Python",
}

// Mapeo de íconos para lenguajes
const languageIcons = {
    [AllowedLanguages.Java]: JavaIcon,
    [AllowedLanguages.TypeScript]: TypeScriptIcon,
    [AllowedLanguages.Python]: PythonIcon,
};


export const languageOptions: DropDownOption[] = Object.values(AllowedLanguages).map((language) => ({
    value: language.toLowerCase(),
    label: language,
    icon: <img src={languageIcons[language]} alt={`${language} icon`} style={{width: 24, height: 24}}/>,
}));

export const languageExamples: Record<string, string> = {
    [AllowedLanguages.TypeScript.toLowerCase()]: `// TypeScript Example
console.log("Hello, World!");`,
    [AllowedLanguages.Java.toLowerCase()]: `// Java Example
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}`,
    [AllowedLanguages.Python.toLowerCase()]: `# Python Example
print("Hello, World!")`,


};

