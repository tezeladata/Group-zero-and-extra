import { useContext } from "react";
import { AuthContext } from "../Context/Auth.jsx";
import { useLocation } from "react-router-dom";

const Login = () => {
    const { login } = useContext(AuthContext);
    const location = useLocation();

    const handleSubmit = (e) => {
        e.preventDefault();

        const account = {
            email: e.target.email.value,
            password: e.target.password.value,
        }

        login(account);
    }

    return (
        <section>
            <h2>{location.pathname === "/admin/login" ? "Admin Login" : "User Login"}</h2>
            <form onSubmit={handleSubmit}>
                <input type="email" name="email" placeholder="Email" required />
                <input type="password" name="password" placeholder="Password" required />
                <button>Login</button>
            </form>
        </section>
    )
}

export default Login;