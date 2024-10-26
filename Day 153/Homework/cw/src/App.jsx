import Register from "./Components/Register.jsx";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./Components/Login.jsx";
import AdminPage from "./Components/AdminPage.jsx";
import Home from "./Components/Home.jsx";

const App = () => {
    return (
        <>
            <Router>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/admin" element={<AdminPage />} />
                </Routes>
            </Router>
        </>
    )
}

export default App;