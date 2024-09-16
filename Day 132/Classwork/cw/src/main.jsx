import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import {BrowserRouter} from "react-router-dom";
import {DataProvider} from "./context/dataContext.jsx";

createRoot(document.getElementById('root')).render(
    <DataProvider>
        <BrowserRouter>
            <App />
        </BrowserRouter>
    </DataProvider>
)
