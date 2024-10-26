import useForm from "../Hooks/useForm.jsx";
import {useState} from "react";
import {Navigate} from "react-router-dom";

const Register = () => {
    const {info, handleChange} = useForm();
    // For navigation
    const [toLogin, setToLogin] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("Form submitted with: ", info)

        const account = {email: info.email, password: info.password};
        localStorage.setItem("account", JSON.stringify(account));

        handleClear();

        setToLogin(true);
    }

    const handleClear = () => {
        handleChange({target: {name: "email", value: ""}});
        handleChange({target: {name: "password", value: ""}});
    }

    const handleDelete = () => {
        localStorage.removeItem("account");
    }

    // For navigation
    if (toLogin) {
        return <Navigate to="login" />
    }


    return (
        <section>
            <form onSubmit={handleSubmit}>
                <input type="email" required placeholder="Enter email" onChange={handleChange} name="email" />
                <input type="password" required placeholder="Enter password" onChange={handleChange} name="password" />

                <button type="submit">Submit form</button>
            </form>

            <hr/>
            <button onClick={() => handleDelete()}>Remove account from local storage</button>
        </section>
    )
}

export default Register;