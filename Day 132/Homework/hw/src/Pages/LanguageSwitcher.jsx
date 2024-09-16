import { useContext } from "react";
import { LanguageContext } from "../Context/LanguageContext";

const LanguageSwitcher = () => {
    const { language, toggleLanguage } = useContext(LanguageContext);

    return (
        <div className="p-4">
            <p>Current Language: {language}</p>
            <button onClick={toggleLanguage} className="p-2 bg-green-500 text-white">
                Toggle Language
            </button>
        </div>
    );
};

export default LanguageSwitcher;