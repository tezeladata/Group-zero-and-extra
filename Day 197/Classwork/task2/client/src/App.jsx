const App = () => {
    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const newAcc = {
                name: e.target.name.value,
                email: e.target.email.value,
                password: e.target.password.value
            }

            const res = await fetch("http://localhost:3000/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(newAcc)
            })

            if (res.ok){
                const data = await res.json()
                console.log(data)
            } else {
                return await res.json()
            }
        } catch (error) {
            console.log(error.message)
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Enter fullname" name="name" required/>
            <input type="email" placeholder="Enter email" name="email" required/>
            <input type="password" placeholder="Enter password" name="password" min="6" required/>
            <button>Submit</button>
        </form>
    )
}

export default App;