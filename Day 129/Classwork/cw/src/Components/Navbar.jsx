import { Link } from "react-router-dom";

const Navbar = () => {
    const navLinks = ["home", "about", "contact", "team"];

    return (
        <header>
            <h1>My Website</h1>
            <nav>
                <ul>
                    {navLinks.map((path, index) => (
                        <li key={index}>
                            <Link to={`/${path}`}>{path}</Link>
                        </li>
                    ))}
                </ul>
            </nav>
        </header>
    );
};

export default Navbar;