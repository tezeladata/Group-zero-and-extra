import { useContext } from "react";
import { StudentsContext } from "../Context/StudentsContext";

const Admin = () => {
    const { students, addStudent } = useContext(StudentsContext);

    const handleSubmit = (e) => {
        e.preventDefault();
        const student = {
            fullname: e.target.fullname.value,
            email: e.target.email.value,
            age: e.target.age.value,
        };
        addStudent(student);
    };

    return (
        <main>
            <section>
                <h1>Admin panel</h1>
            </section>

            <section>
                <h2>Add student</h2>
                <form onSubmit={handleSubmit}>
                    <input type="text" name="fullname" placeholder="fullname" required />
                    <input type="email" name="email" placeholder="email" required />
                    <input type="number" name="age" placeholder="age" required />
                    <button type="submit">Submit</button>
                </form>
            </section>

            <section>
                <h2>Students</h2>
                <ul>
                    {students?.map((student) => (
                        <li key={student.id}>
                            <strong>{student.fullname}</strong> {student.email} {student.age}
                        </li>
                    ))}
                </ul>
            </section>
        </main>
    );
};

export default Admin;