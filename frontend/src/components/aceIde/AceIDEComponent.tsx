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
    readonly?: boolean;
    enableBasicAutocompletion?: boolean;
}


const AceIDEComponent: React.FC<AceIDEComponent> = ({code, setCode, language, readonly=true, enableBasicAutocompletion: enableAutocompletion = false}) => {

    const {theme} = useTheme();

    return (
        <AceEditor
            style={{
                display: 'flex',
                width: '100%',
                flex: 1
            }}
            placeholder='Start Coding'
            mode={language}
            theme={theme === 'lightTheme' ? 'clouds' : 'monokai'}
            name='basic-code-editor'
            onChange={currentCode => setCode(currentCode)}
            fontSize={"var(--font-size-medium1)"}
            value={code}
            setOptions={{
                showPrintMargin: false,
                showGutter: true,
                highlightActiveLine: true,
                enableBasicAutocompletion: enableAutocompletion,
                enableLiveAutocompletion: enableAutocompletion,
                enableSnippets: false,
                showLineNumbers: true,
                tabSize: 4,
                showFoldWidgets: true,
                displayIndentGuides: true,
                readOnly: readonly,
            }}
        />

    );
};

export default AceIDEComponent;

