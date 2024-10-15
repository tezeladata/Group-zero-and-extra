import React, { useContext } from "react";
import { StudentsContext } from "../Context/studentsContext";

const StudentList = () => {
    const { all } = useContext(StudentsContext);

    return (
        <section className="student-list">
            <h2 className="text-2xl font-bold">Registered Students</h2>
            {all.length > 0 ? (
                <ul>
                    {all.map((student, index) => (
                        <li key={index} className="p-2 text-lg">
                            <strong>{student.username}</strong> - {student.email} <br /> <strong>Facebook link:</strong> - {student.link} <br /> <strong>Password:</strong> - {student.password}
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No students registered yet.</p>
            )}
        </section>
    );
};

export default StudentList;