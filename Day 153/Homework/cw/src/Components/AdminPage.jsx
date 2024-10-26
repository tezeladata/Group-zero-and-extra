import useForm from "../Hooks/useForm.jsx";
import { useState, useEffect } from "react";
import {Navigate} from "react-router-dom";

const AdminPage = () => {
    const { info, handleChange } = useForm();
    // For all students
    const [studentArr, setStudentArr] = useState([]);
    // For student editing
    const [isEditing, setIsEditing] = useState(false);
    const [currentEditIndex, setCurrentEditIndex] = useState(null);
    const [editInfo, setEditInfo] = useState({});
    // Navigate back
    const [back, setBack] = useState(false);

    // Check when student is added
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("Form submitted with: ", info);

        if (isEditing) {
            updateStudent();
        } else {
            addToArray();
        }
    };

    // working with localStorage
    useEffect(() => {
        const storedData = JSON.parse(localStorage.getItem("all students"));
        if (storedData) setStudentArr(storedData);
    }, []);

    // Add to localStorage when studentArr changes
    useEffect(() => {
        localStorage.setItem("all students", JSON.stringify(studentArr));
    }, [studentArr]);

    // Add student to array
    const addToArray = () => {
        setStudentArr((prevArray) => [...prevArray, info]);

        // Reset the input fields
        handleChange({ target: { name: "name", value: "" } });
        handleChange({ target: { name: "age", value: "" } });
        handleChange({ target: { name: "email", value: "" } });
        handleChange({ target: { name: "password", value: "" } });
    };

    // Remove student
    const removeFromArray = (ind) => {
        setStudentArr((prev) => prev.filter((_, index) => index !== ind));
    };

    // Edit student
    const editStudent = (ind) => {
        setCurrentEditIndex(ind);
        setEditInfo(studentArr[ind]);
        setIsEditing(true);
    };

    // Update existing student
    const updateStudent = () => {
        setStudentArr((prevArray) =>
            prevArray.map((student, index) =>
                index === currentEditIndex ? editInfo : student
            )
        );
        setIsEditing(false);
        setCurrentEditIndex(null);
        setEditInfo({});

        // Reset the input fields after updating
        handleChange({ target: { name: "name", value: "" } });
        handleChange({ target: { name: "age", value: "" } });
        handleChange({ target: { name: "email", value: "" } });
        handleChange({ target: { name: "password", value: "" } });
    };

    // Handle change from form edit fields
    const handleEditChange = (e) => {
        const { name, value } = e.target;
        setEditInfo((prev) => ({ ...prev, [name]: value }));
    };

    // Navigate back
    const returnBack = () => {
        setBack(true);
    }
    if (back) {
        return <Navigate to="/" />
    }

    return (
        <section>
            {/* Back to the landing page */}
            <button onClick={() => returnBack()}>Back to home</button>


            {/*  Add or edit student  */}
            <section>
                <h2>{isEditing ? "Edit student" : "Add student"}</h2>

                <form onSubmit={handleSubmit}>
                    <label>{isEditing ? "Edit student" : "Add student"}</label><br /><br />
                    <input
                        type="text"
                        required
                        placeholder="Enter student fullname"
                        onChange={isEditing ? handleEditChange : handleChange}
                        value={isEditing ? editInfo.name || "" : info.name || ""}
                        name="name"
                    /><br /><br />
                    <input
                        type="number"
                        required
                        placeholder="Enter student age"
                        onChange={isEditing ? handleEditChange : handleChange}
                        value={isEditing ? editInfo.age || "" : info.age || ""}
                        name="age"
                    /><br /><br />
                    <input
                        type="email"
                        required
                        placeholder="Enter student email"
                        onChange={isEditing ? handleEditChange : handleChange}
                        value={isEditing ? editInfo.email || "" : info.email || ""}
                        name="email"
                    /><br /><br />
                    <input
                        type="password"
                        required
                        placeholder="Enter student password"
                        onChange={isEditing ? handleEditChange : handleChange}
                        value={isEditing ? editInfo.password || "" : info.password || ""}
                        name="password"
                    /><br /><br />

                    <br /><br />
                    <button type="submit">{isEditing ? "Update Student" : "Submit Form"}</button>
                </form>
            </section>

            {/*  View all students  */}
            <section>
                <h2>All students</h2>
                <ul>
                    {studentArr.map((student, index) => (
                        <li key={index}>
                            <p><strong>Name: </strong> {student.name}</p>
                            <p><strong>Age: </strong> {student.age}</p>
                            <p><strong>Email: </strong> {student.email}</p>
                            <button onClick={() => removeFromArray(index)}>Delete this student</button>
                            <button onClick={() => editStudent(index)}>Edit student</button>
                        </li>
                    ))}
                </ul>
            </section>
        </section>
    );
};

export default AdminPage;