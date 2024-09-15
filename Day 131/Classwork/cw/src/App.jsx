import {Link, Route, Routes} from "react-router-dom";
import Home from "./Pages/Home.jsx";
import About from "./Pages/About.jsx";
import Contact from "./Pages/Contact.jsx";
import Products from "./Pages/Products.jsx";
import Info from "./Pages/Info.jsx";

export default function App() {
    return (
        <>
            <nav>
                <ul>
                    <li>
                        <Link to={'about'}>About</Link>
                    </li>

                    <li>
                        <Link to={'/'}>Home</Link>
                    </li>

                    <li>
                        <Link to={'/contact'}>Contact</Link>
                    </li>

                    <li>
                        <Link to={'/products'}>Products</Link>
                    </li>

                    <li>
                        <Link to={'/info'}>Info</Link>
                    </li>
                </ul>
            </nav>

            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/contact" element={<Contact />} />
                <Route path="/products" element={<Products />} />
                <Route path="/info" element={<Info />} />
            </Routes>
        </>
    )
}