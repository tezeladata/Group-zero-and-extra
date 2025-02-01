import { useContext } from "react";
import { AuthContext } from "../Context/AuthContext.jsx";

const Register = () => {
    const { register } = useContext(AuthContext);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const account = {
            email: e.target.email.value,
            pass: e.target.password.value,
        };

        try {
            await register(account);
            alert("Registration successful!");
        } catch (error) {
            console.error(error);
            alert("Registration failed. Please try again.");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="email" name="email" placeholder="Email" required />
            <input type="password" name="password" placeholder="Password" required />
            <button>Register</button>
        </form>
    );
};

export default Register;