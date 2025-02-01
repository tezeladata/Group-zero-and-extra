import React, { createContext, useState } from "react";

export const AuthContext = createContext({ register: () => {}, login: () => {} });

const AuthProvider = ({ children }) => {
    const [admin, setAdmin] = useState(null);

    const register = async (acc) => {
        try {
            const res = await fetch(`http://localhost:3000/admin/register`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(acc),
            });

            if (!res.ok) {
                throw new Error(`Failed to register: ${res.status} ${res.statusText}`);
            }

            const msg = await res.json();
            console.log("Registration successful:", msg);
        } catch (error) {
            console.error("Registration error:", error);
        }
    };

    const login = async (acc) => {
        try {
            const res = await fetch(`http://localhost:3000/admin/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(acc),
            });

            if (!res.ok) {
                throw new Error(`Failed to login: ${res.status} ${res.statusText}`);
            }

            const data = await res.json();
            setAdmin(data);
            console.log("Login successful:", data);
        } catch (error) {
            console.error("Login error:", error);
        }
    };

    const logout = () => {
        setAdmin(null);
    }

    return (
        <AuthContext.Provider value={{ register, login, admin, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthProvider;