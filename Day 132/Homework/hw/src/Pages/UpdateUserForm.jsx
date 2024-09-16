import { useContext, useState } from "react";
import { UserContext } from "../Context/UserContext";

const UpdateUserForm = () => {
    const { user, updateUser } = useContext(UserContext);
    const [name, setName] = useState(user.name);
    const [email, setEmail] = useState(user.email);

    const handleSubmit = (e) => {
        e.preventDefault();
        updateUser({ name, email });
    };

    return (
        <form onSubmit={handleSubmit} className="p-4">
            <div>
                <label>Name:</label>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="border p-2"
                />
            </div>
            <div>
                <label>Email:</label>
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="border p-2"
                />
            </div>
            <button type="submit" className="mt-2 p-2 bg-blue-500 text-white">
                Update
            </button>
        </form>
    );
};

export default UpdateUserForm;