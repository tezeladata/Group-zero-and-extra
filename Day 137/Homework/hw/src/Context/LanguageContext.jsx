import {createContext, useState} from "react";

export const LanguageContext = createContext();

const LanguageProvider = ({children}) => {
    const [language, setLanguage] = useState("english");

    return (
        <LanguageContext.Provider value={{language, setLanguage}}>
            {children}
        </LanguageContext.Provider>
    )
}

export default LanguageProvider;