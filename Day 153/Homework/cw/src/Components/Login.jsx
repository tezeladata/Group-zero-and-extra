import useForm from "../Hooks/useForm.jsx";
import {Navigate} from "react-router-dom";
import {useState} from "react";

const Login = () => {
    const {info, handleChange} = useForm();
    // for validation
    const [valid, setValid] = useState(false);
    // for navigation to home
    const [navigateBack, setNavigateBack] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("Form submitted with: ", info)
    }

    const checkInfo = () => {
        let registrationAccount = JSON.parse(localStorage.getItem("account"));
        console.log(registrationAccount);

        if (info.email === registrationAccount.email && info.password === registrationAccount.password){
            setValid(true);
        }
    }

    const back = () => {
        setNavigateBack(true);
    }

    if (valid) {
        return <Navigate to="/admin" />
    }

    if (navigateBack) {
        return <Navigate to="/" />
    }


    return (
        <section>
            <form onSubmit={handleSubmit}>
                <label>Check for info, log in</label>
                <br/><br/>
                <input type="email" required placeholder="Enter email again" onChange={handleChange} name="email"/>
                <br/><br/>
                <input type="password" required placeholder="Enter password again" onChange={handleChange}
                       name="password"/>

                <br/><br/>
                <button type="submit" onClick={() => checkInfo()}>Submit form</button>
            </form>

            <hr/>
            <button onClick={() => back()}>Back to registration</button>
        </section>
    )
}

export default Login;