// src/App.tsx
import React from 'react';
import '@/App.css';
import AuthorLink from "./components/authorLink/AuthorLink.tsx";
import ThemeToggleButton from "./components/buttons/themeToggleButton/ThemeToggleButton.tsx";
import HelpButton from "./components/buttons/helpButton/helpButtonAndPopUp.tsx";
import {Route, Routes, useLocation} from 'react-router-dom';
import GraphMLCodeGenerator from "./pages/graphml/GraphMLCodeGenerator.tsx";
import HomePage from "./pages/homePage/HomePage.tsx";
import NotFoundPage from "./pages/notFound/NotFoundPage.tsx";
import HomeButton from "./components/buttons/homeButton/HomeButton.tsx";
import CRUDCodeGenerator from "./pages/crud/CRUDCodeGenerator.tsx";


const App: React.FC = () => {

    const location = useLocation();

    // Dynamic titles based on the current route
    const getPageTitle = () => {
        switch (location.pathname) {
            case "/graphml-code-generator":
                return "GraphML Code Generator";
            case "/crud-code-generator":
                return "CRUD Code Generator";
            case "/":
                return "Code Generators";
            default:
                return "Page Not Found";
        }
    };
    return (
        <div className="app-container">
            {/* AuthorLink stays at the bottom */}
            <div style={{zIndex: 1000, backgroundColor: 'transparent'}}>
                <AuthorLink/>
            </div>

            {/* Fixed header */}
            <header className="app-header">
                <div className="header-buttons">
                    <HomeButton/>
                </div>
                <h1 className="page-title">{getPageTitle()}</h1>
                <div className="header-buttons">
                    <ThemeToggleButton/>
                    <HelpButton/>
                </div>
            </header>

            {/* Main content with routes */}
            <main className="app-content">
                <Routes>
                    <Route path="/" element={<HomePage/>}/>
                    <Route path="/graphml-code-generator" element={<GraphMLCodeGenerator/>}/>
                    <Route path="/crud-code-generator" element={<CRUDCodeGenerator/>}/>
                    <Route path="*" element={<NotFoundPage/>}/>
                </Routes>
            </main>
        </div>
    );
};
export default App;
