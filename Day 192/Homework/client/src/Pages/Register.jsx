import {useContext} from "react";
import {AuthContext} from "../Context/Auth.jsx";

const Register = () => {
    const { register } = useContext(AuthContext);

    const handleSubmit = (e) => {
        e.preventDefault();

        const acc = {
            fullName: e.target.fullname.value,
            email: e.target.email.value,
            password: e.target.password.value,
        }

        register(acc);
    }

    return (
        <section>
            <form onSubmit={handleSubmit}>
                <input type="text" name="fullname" placeholder="fullname" required/>
                <input type="email" name="email" placeholder="email" required/>
                <input type="password" name="password" placeholder="password" required/>
                <button>Register</button>
            </form>
        </section>
    )
}

export default Register;