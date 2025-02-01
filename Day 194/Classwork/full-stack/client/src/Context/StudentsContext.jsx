import { createContext, useEffect, useState } from "react";

export const StudentsContext = createContext();

const StudentsProvider = ({ children }) => {
    const [students, setStudents] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await fetch("http://localhost:3000/students/");
                const json = await res.json();
                setStudents(json);
            } catch (err) {
                console.error("Failed to fetch students:", err);
            }
        };

        fetchData();
    }, []);

    const addStudent = async (student) => {
        try {
            const res = await fetch("http://localhost:3000/students/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(student),
            });

            if (!res.ok) {
                throw new Error(`Failed to register: ${res.status} ${res.statusText}`);
            }

            const data = await res.json();
            setStudents((prevStudents) => [...prevStudents, data.student]);
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <StudentsContext.Provider value={{ students, addStudent }}>
            {children}
        </StudentsContext.Provider>
    );
};

export default StudentsProvider;