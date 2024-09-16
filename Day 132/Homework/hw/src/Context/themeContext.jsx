import {createContext, useState} from "react";

const themeContext = createContext();

const ThemeProvider = ({ children }) => {
    const [theme, setTheme] = useState("white");

    const toggleTheme = () => {
        setTheme(prev => prev === "white" ? "black" : "white");
    }

    return (
        <themeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </themeContext.Provider>
    )
}

export {themeContext, ThemeProvider};