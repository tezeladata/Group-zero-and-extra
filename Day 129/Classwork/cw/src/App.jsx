// import Classwork from "./Components/Classwork.jsx";
import Home from "./Components/Home.jsx";
import About from "./Components/About.jsx";
import Navbar from "./Components/Navbar.jsx";
import {Route, Routes} from "react-router-dom";

const App = () => {
    return (
        <>
            <Navbar />

            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
            </Routes>
        </>
    )
}

export default App
