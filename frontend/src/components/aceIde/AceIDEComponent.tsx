import React from 'react';
import AceEditor from 'react-ace'

// import mode-<language> , this imports the style and colors for the selected language.
import 'ace-builds/src-noconflict/mode-java'
import 'ace-builds/src-noconflict/mode-python'
import 'ace-builds/src-noconflict/mode-csharp'
import 'ace-builds/src-noconflict/mode-typescript'


// there are many themes to import, I liked monokai.
import 'ace-builds/src-noconflict/theme-monokai'
import 'ace-builds/src-noconflict/theme-clouds'

// this is an optional import just improved the interaction.
import 'ace-builds/src-noconflict/ext-language_tools'
import 'ace-builds/src-noconflict/ext-beautify'

// Configurar el path base de Ace
import ace from "ace-builds/src-noconflict/ace";
import {useTheme} from "../../styles/theme/themeContext.tsx";

ace.config.set("basePath", "/ace-builds");

// Inject code and setCode as props
interface AceIDEComponent {
    code: string;
    setCode: (code: string) => void;
    language: string;
}


const AceIDEComponent: React.FC<AceIDEComponent> = ({code, setCode, language}) => {

    const { theme } = useTheme();

    console.log("AceIDEComponent -> language", language)

    return (
            <AceEditor
                style={{
                    height: '50vh',
                    width: '100%',
                }}
                readOnly={false}
                placeholder='Start Coding'
                mode={language}
                theme={theme === 'light' ? 'clouds' : 'monokai'}
                name='basic-code-editor'
                onChange={currentCode => setCode(currentCode)}
                fontSize={18}
                showPrintMargin={true}
                showGutter={true}
                highlightActiveLine={true}
                value={code}
                setOptions={{
                    enableBasicAutocompletion: true,
                    enableLiveAutocompletion: true,
                    enableSnippets: true,
                    showLineNumbers: true,
                    tabSize: 4,
                }}
            />

    );
};

export default AceIDEComponent;

