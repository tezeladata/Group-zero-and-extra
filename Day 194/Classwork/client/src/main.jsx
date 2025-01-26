import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import AuthProvider from "./Context/AuthContext.jsx";
import {BrowserRouter} from "react-router";
import StudentsProvider from "./Context/StudentsContext.jsx";

createRoot(document.getElementById('root')).render(
    <BrowserRouter>
        <AuthProvider>
            <StudentsProvider>
                    <App />
            </StudentsProvider>
        </AuthProvider>
    </BrowserRouter>
)
