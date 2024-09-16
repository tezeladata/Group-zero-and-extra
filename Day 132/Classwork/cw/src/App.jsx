import {Link, Route, Routes} from "react-router-dom";

// Pages
import Home from "./Pages/Home.jsx";
import About from "./Pages/About.jsx";
import Profile from "./Pages/Profile.jsx";
import Photos from "./Pages/Photos.jsx";
import Contact from "./Pages/Contact.jsx";

export default function App(){
    return (
        <>
            <ul className="flex items-center justify-center p-2">
                <li><Link to='/' className="p-2">Home</Link></li>
                <li><Link to='/about' className="p-2">About</Link></li>
                <li><Link to='/profile' className="p-2">Profile</Link></li>
                <li><Link to='/photos' className="p-2">Photos</Link></li>
                <li><Link to='/contact' className="p-2">Contact</Link></li>
            </ul>
            <hr />

            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/profile" element={<Profile />} />
                <Route path="/photos" element={<Photos />} />
                <Route path="/contact" element={<Contact />} />
            </Routes>
        </>
    )
}