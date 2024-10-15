import { useContext, useState } from "react";
import { StudentsContext } from "../Context/studentsContext.jsx";

const StudentItem = () => {
    const [student, setStudent] = useState("");
    const [found, setFound] = useState([]);
    const { all } = useContext(StudentsContext);

    const handleInputChange = (e) => {
        setStudent(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const foundStudents = all.filter(item => item.username === student);
        setFound(foundStudents.length > 0 ? foundStudents : []);
    };

    return (
        <section>
            <hr />
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Search student by name"
                    name="student-input"
                    value={student}
                    onChange={handleInputChange}
                />
                <button type="submit">Submit</button>
            </form>
            {found.length > 0 ? (
                <>
                    <p>{found[0].username}</p>
                    <p>{found[0].email}</p>
                    <p>{found[0].password}</p>
                    <p>{found[0].link}</p>
                </>
            ) : (
                <p>No student found</p>
            )}
        </section>
    );
};

export default StudentItem;