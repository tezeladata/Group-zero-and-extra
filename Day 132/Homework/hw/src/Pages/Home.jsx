import { useContext, useState } from "react";
import { themeContext } from "../Context/themeContext";
import { UserContext } from "../Context/UserContext";
import UserInfo from "./UserInfo";
import UpdateUserForm from "./UpdateUserForm";

export default function Home() {
    const [textCol, setTextCol] = useState("black");
    const { theme, toggleTheme } = useContext(themeContext);
    const { user } = useContext(UserContext);

    const toggleCol = () => {
        setTextCol(prevColor => prevColor === "black" ? "white" : "black");
    };

    return (
        <div style={{ backgroundColor: theme }} className="h-screen flex flex-col justify-center items-center">
            <p style={{ color: textCol }} className="text-4xl p-4">Current theme: {theme}</p>
            <button
                onClick={() => {
                    toggleTheme();
                    toggleCol();
                }}
                style={{ color: textCol }}
                className="text-4xl p-4">
                Toggle Theme
            </button>
            <UserInfo />
            <UpdateUserForm />
        </div>
    );
}