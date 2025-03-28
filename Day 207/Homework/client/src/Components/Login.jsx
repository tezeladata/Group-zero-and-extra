import { useState } from "react";

const Login = () => {
    const [exists, setExists] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();

        const newUser = {
            "email": e.target.email.value,
            "password": e.target.password.value
        }

        e.target.email.value = "";
        e.target.password.value = "";

        // Send data to database
        fetch("http://localhost:3000/user/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(newUser),
        }).then(data => data.json()).then(res => {
            if (res.exists === true) {
                setExists(true)
                alert("User is logged in")
            } else {
                setExists(false);
                alert("User is not logged in")
            }
        })
    }

    return (
        <section className="p-5">
            <hr />
            <h1 className="text-4xl font-bold text-center pb-5">Login</h1>

            <form className="text-center" onSubmit={handleSubmit}>
                <input type="email" placeholder="Enter email" required name="email" className="text-center w-[20%] bg-black text-white rounded-lg" /> <br /> <br />
                <input type="password" placeholder="Enter password" required name="password" className="text-center w-[20%] bg-black text-white rounded-lg" /> <br /> <br />
                <button type="submit" className="mb-5 bg-black px-5 py-2 text-white rounded-lg cursor-pointer">Submit form</button>
            </form>

            <hr />
        </section>
    )
};

export default Login;