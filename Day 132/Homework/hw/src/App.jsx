import Home from "./Pages/Home";
import { ThemeProvider } from "./Context/themeContext";
import { UserProvider } from "./Context/UserContext";
import { LanguageProvider } from "./Context/LanguageContext";

export default function App() {
    return (
        <ThemeProvider>
            <UserProvider>
                <LanguageProvider>
                    <Home />
                </LanguageProvider>
            </UserProvider>
        </ThemeProvider>
    );
}