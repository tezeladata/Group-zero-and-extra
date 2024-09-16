import { useContext } from "react";
import { UserContext } from "../Context/UserContext";

const UserInfo = () => {
    const { user } = useContext(UserContext);

    return (
        <div className="p-4">
            <h2 className="text-2xl">User Information</h2>
            <p><strong>Name:</strong> {user.name}</p>
            <p><strong>Email:</strong> {user.email}</p>
        </div>
    );
};

export default UserInfo;