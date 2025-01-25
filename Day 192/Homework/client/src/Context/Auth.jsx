import {createContext, useState} from "react";
import {useNavigate} from "react-router";


export const AuthContext = createContext();

const AuthProvider = ({ children }) => {
    const [admin, setAdmin] = useState({})
    const navigate = useNavigate();

    const register = async (data) => {
        try {
            const res = await fetch("http://localhost:3000/admin/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })

            if (res.ok) {
                navigate("/login")
            }
        } catch (e) {
            console.error(e);
        }
    }

    const login = async (data) => {
        try {
            const res = await fetch("http://localhost:3000/admin/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })

            const account = await res.json();
            setAdmin(account);
        } catch (e) {
            console.error(e);
        }
    }

    return  (
        <AuthContext.Provider value={{ register, login }}>
            {children}
        </AuthContext.Provider>
    )
};

export default AuthProvider;