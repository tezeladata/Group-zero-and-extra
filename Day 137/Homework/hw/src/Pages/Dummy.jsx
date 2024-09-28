import {useContext} from "react";
import {ThemeContext} from "../Context/ThemeContext.jsx";
import {UserContext} from "../Context/UserContext.jsx";
import {LanguageContext} from "../Context/LanguageContext.jsx";

const Dummy = () => {
    const {theme, setTheme} = useContext(ThemeContext);
    const {isLoggedIn, user, setIsLoggedIn, setUser} = useContext(UserContext);
    const {language, setLanguage} = useContext(LanguageContext);


    return (
        <section>
            <h1>Hello, there</h1>
            <p>Theme is {theme}</p>

            <br/>
            <button onClick={() => setTheme(theme === "dark" ? "light" : "dark")}>Click here to change Theme</button>
            <br/>

            <form>
                <input value={user} onChange={(e) => setUser(e.target.value)} placeholder="Enter name"/>
            </form>

            <button onClick={() => setIsLoggedIn(isLoggedIn === "yes" ? "no" : "yes")}>Click to log in / log out</button>

            <br/>
            <p>Is logged in: {isLoggedIn} <br/> User: {user}</p>
            <br />

            <p>Current language is: {language}</p>
            <button onClick={() => setLanguage(language === "english" ? "spanish" : "english")}>Click here to change language</button>
            <p>{language === "english" ? "hello there" : "Hola, qué tal"}</p>
            <hr/>
        </section>
    )
}

export default Dummy;