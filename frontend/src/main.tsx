// import './formalizer.css'
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter as Router } from "react-router-dom";
import { ThemeProvider } from "./styles/theme/themeContext";
import App from "./App";

createRoot(document.getElementById("root")!).render(
    <StrictMode>
        <ThemeProvider>
            <Router>
                <App />
            </Router>
        </ThemeProvider>
    </StrictMode>
);
