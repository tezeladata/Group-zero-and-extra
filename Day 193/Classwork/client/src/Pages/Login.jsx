import { useContext } from "react";
import { AuthContext } from "../Context/AuthContext.jsx";

const Login = () => {
    const { login } = useContext(AuthContext);

    const handleSubmit = (e) => {
        e.preventDefault();

        const account = {
            email: e.target.email.value,
            pass: e.target.password.value,
        };

        login(account);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="email" name="email" placeholder="Email" required />
            <input type="password" name="password" placeholder="Password" required />
            <button>Login</button>
        </form>
    );
};

export default Login;