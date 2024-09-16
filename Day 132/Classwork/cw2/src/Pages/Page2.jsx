import { useContext } from "react";
import { dataContext } from "../Context/dataContext.jsx";

const Page2 = () => {
    const { lang_obj, toggleLanguage } = useContext(dataContext);

    return (
        <section>
            <hr /> <br />
            <h2>Current language is: {lang_obj.lang}</h2>
            <p>{lang_obj.lang === "Geo" ? "გამარჯობა" : "Hello"}</p>
            <button onClick={toggleLanguage}>Click here to change language</button>
        </section>
    );
};

export default Page2;