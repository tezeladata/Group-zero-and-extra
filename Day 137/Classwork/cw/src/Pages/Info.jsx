import {useContext} from "react";
import {ThemeContext} from "../Context/ThemeContext.jsx";

const Info = () => {
    const theme = useContext(ThemeContext);

    return (
        <section style={{backgroundColor: theme}}>
            <p>Hello world!</p>
        </section>
    )
}

export default Info;