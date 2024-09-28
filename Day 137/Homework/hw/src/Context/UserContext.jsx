import {createContext, useState} from "react";

export const UserContext = createContext();

const UserProvider = ({children}) => {
    const [isLoggedIn, setIsLoggedIn] = useState("yes");
    const [user, setUser] = useState("");

    return (
        <UserContext.Provider value={{isLoggedIn, user, setIsLoggedIn, setUser}}>
            {children}
        </UserContext.Provider>
    )
}

export default UserProvider;