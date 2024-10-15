import StudentForm from "./Components/StudentForm.jsx";
import {StudentsProvider} from "./Context/studentsContext.jsx";
import StudentList from "./Components/StudentList.jsx";
import StudentItem from "./Components/StudentItem.jsx";

const App = () => {
    return (
        <>
            <StudentsProvider>
                <StudentForm />
                <StudentList />
                <StudentItem />
            </StudentsProvider>
        </>

    //stopped at task 6
    )
}

export default App;