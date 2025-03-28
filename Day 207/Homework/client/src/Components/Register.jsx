const Register = () => {
    const handleSubmit = async (e) => {
        e.preventDefault();
    
        const newUser = {
            "name": e.target.name.value,
            "email": e.target.email.value,
            "password": e.target.password.value
        };
    
        e.target.name.value = "";
        e.target.email.value = "";
        e.target.password.value = "";
    
        try {
            const response = await fetch("http://localhost:3000/user/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(newUser),
            });
    
            if (response.ok) {
                window.location.href = "/login"; 
            } else {
                console.error("Registration failed!");
            }
        } catch (error) {
            console.error("Error occurred:", error);
        }
    };

    return (
        <section className="p-5">
            <hr />
            <h1 className="text-4xl font-bold text-center pb-5">Register</h1>

            <form className="text-center" onSubmit={handleSubmit}>
                <input type="text" placeholder="Enter name" required name="name" className="text-center w-[20%] bg-black text-white rounded-lg" /> <br /> <br />
                <input type="email" placeholder="Enter email" required name="email" className="text-center w-[20%] bg-black text-white rounded-lg" /> <br /> <br />
                <input type="password" placeholder="Enter password" required name="password" className="text-center w-[20%] bg-black text-white rounded-lg" /> <br /> <br />
                <button type="submit" className="mb-5 bg-black px-5 py-2 text-white rounded-lg cursor-pointer">Submit form</button>
            </form>

            <hr />
        </section>
    )
};

export default Register;