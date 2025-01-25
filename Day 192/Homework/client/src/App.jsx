import { Router, Routes, Route } from "react-router-dom";
import Register from "./Pages/Register.jsx";
import Navbar from "./Components/Navbar.jsx";
import Login from "./Pages/Login.jsx";

const App = () => {
    return (
        <div>
            <Navbar />
            <Routes>
                <Route path="/" element={<h1>Home</h1>} />
                <Route path="/register" element={<Register />} />
                <Route path="/login" element={<Login />} />
            </Routes>
        </div>
    );
}

export default App;