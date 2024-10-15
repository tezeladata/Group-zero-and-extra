import { createContext, useState } from "react";

export const StudentsContext = createContext();

export const StudentsProvider = ({ children }) => {
    const [all, setAll] = useState([]);

    const addStudent = (info) => {
        setAll(prevAll => [...prevAll, info]);
    };

    return (
        <StudentsContext.Provider value={{ all, addStudent }}>
            {children}
        </StudentsContext.Provider>
    );
};