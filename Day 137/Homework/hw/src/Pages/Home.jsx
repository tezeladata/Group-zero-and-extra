import ThemeProvider from "../Context/ThemeContext.jsx";
import Dummy from "./Dummy.jsx";
import UserProvider from "../Context/UserContext.jsx";
import LanguageProvider from "../Context/LanguageContext.jsx";

export const Home = () => {
    return (
        <main>
            <ThemeProvider initialTheme="dark">
                <UserProvider>
                    <LanguageProvider>
                        <Dummy />
                    </LanguageProvider>
                </UserProvider>
            </ThemeProvider>

            <ThemeProvider initialTheme="dark">
                <UserProvider>
                    <LanguageProvider>
                        <Dummy />
                    </LanguageProvider>
                </UserProvider>
            </ThemeProvider>
        </main>
    )
}