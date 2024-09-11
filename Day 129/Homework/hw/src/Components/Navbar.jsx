import { Link } from "react-router-dom";

export default function Navbar() {
    const navLinks = ["home", "about", "Form"]

    return (
        <header>
            <h1>Welcome to the website</h1>

            <nav>
                <ul>
                    {navLinks.map((path, index) => {
                        return (
                            <li key={index}>
                                <Link to={`/${path}`}>{path}</Link>
                            </li>
                        )
                    })}
                </ul>
            </nav>
        </header>
    )
}