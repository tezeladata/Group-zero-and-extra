import { createContext, useState } from "react";

// Create the context
export const dataContext = createContext();

const DataContextProvider = ({ children }) => {
    const [lang_obj, setLangObj] = useState({ lang: "Eng" });
    const toggleLanguage = () => {
        setLangObj((prev) => ({
            lang: prev.lang === "Geo" ? "Eng" : "Geo"
        }));
    };

    return (
        <dataContext.Provider value={{ lang_obj, toggleLanguage }}>
            {children}
        </dataContext.Provider>
    );
};

export default DataContextProvider;