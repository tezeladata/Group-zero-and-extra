import Info from "./Info.jsx";
import {ThemeProvider} from "../Context/ThemeContext.jsx";

export const Home = () => {

    return (
            <main>
                <ThemeProvider initialTheme="blue">
                    <Info />
                </ThemeProvider>

                <ThemeProvider initialTheme="green">
                    <Info />
                </ThemeProvider>
            </main>
    );
};