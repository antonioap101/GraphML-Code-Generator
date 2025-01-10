// import './formalizer.css'
import {StrictMode} from "react";
import {createRoot} from "react-dom/client";
import {BrowserRouter as Router} from "react-router-dom";
import {ThemeProvider} from "./styles/theme/themeContext";
import App from "./App";
import {ApiProvider} from "./hooks/useAPI.tsx";

createRoot(document.getElementById("root")!).render(
    <StrictMode>
        <ThemeProvider>
            <ApiProvider>
                <Router>
                    <App/>
                </Router>
            </ApiProvider>
        </ThemeProvider>
    </StrictMode>
);
