// src/App.tsx
import React from 'react';
import '@/App.css';
import AuthorLink from "./components/authorLink/AuthorLink.tsx";
import ThemeToggleButton from "./components/buttons/themeToggleButton/ThemeToggleButton.tsx";
import HelpButton from "./components/buttons/helpButton/helpButtonAndPopUp.tsx";
import {Route, Routes} from 'react-router-dom';
import GraphMLCodeGenerator from "./pages/graphml/GraphMLCodeGenerator.tsx";
import HomePage from "./pages/homePage/HomePage.tsx";
import NotFoundPage from "./pages/notFound/NotFoundPage.tsx";
import HomeButton from "./components/buttons/homeButton/HomeButton.tsx";
import CRUDCodeGenerator from "./pages/crud/CRUDCodeGenerator.tsx";

const App: React.FC = () => {
    return (
        <div className="app-container">
            <div style={{zIndex: 1000, backgroundColor: 'transparent'}}>
                <AuthorLink/>
                <HomeButton/>
            </div>
            <div style={{
                zIndex: 1000, position: 'fixed', top: 20, right: 20, display: 'flex', gap: '10px'
            }}>
                <ThemeToggleButton/>
                <HelpButton/>
            </div>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/graphml-code-generator" element={<GraphMLCodeGenerator/>}/>
                <Route path="/crud-code-generator" element={<CRUDCodeGenerator/>}/>
                <Route path="*" element={<NotFoundPage/>}/>
            </Routes>

        </div>
    );
};

export default App;
