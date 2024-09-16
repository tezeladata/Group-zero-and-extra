import {createContext} from "react";

const dataContext = createContext();

const DataProvider = ({ children }) => {
    const acc = {
        firstname: "John",
        lastname: "Doe",
        email: "john@doe.com"
    }

    return (
        <dataContext.Provider value={{acc}}>
            {children}
        </dataContext.Provider>
    )
}

export { dataContext, DataProvider }