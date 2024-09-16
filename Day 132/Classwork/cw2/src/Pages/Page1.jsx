import { useContext } from "react";
import { dataContext } from "../Context/dataContext.jsx";

const Page1 = () => {
    const { lang_obj } = useContext(dataContext);

    return (
        <section>
            <hr /> <br />
            <h2>Current language is: {lang_obj.lang}</h2>
            <p>{lang_obj.lang === "Geo" ? "გამარჯობა" : "Hello"}</p>
        </section>
    );
};

export default Page1;