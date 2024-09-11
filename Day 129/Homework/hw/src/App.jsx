import Form from "./Components/Form.jsx";
import Navbar from "./Components/Navbar.jsx";
import {Route, Routes} from "react-router-dom";
import About from "./Components/About.jsx";
import Home from "./Components/Home.jsx";

export default function App() {
    return (
        <>

            <Navbar />

            <Routes>
                <Route path="/Home" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/Form" element={<Form />} />
            </Routes>

        </>
    )
}