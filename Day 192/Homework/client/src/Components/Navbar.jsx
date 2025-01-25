import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <header>
            <hr/>
            <h1>GOA system</h1>

            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/register">Register</Link></li>
                    <li><Link to="/login">Login</Link></li>
                </ul>
            </nav>

            <hr/>
        </header>
    )
}

export default Navbar;