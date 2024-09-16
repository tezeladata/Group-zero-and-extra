import {useContext} from "react";
import {dataContext} from "../context/dataContext.jsx";

const About = () => {
    const {acc} = useContext(dataContext);

    return (
        <section>
            <h1>About component</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur, quas!</p>

            <br/>
            <b>Name: {acc.firstname}, <br/>Surname: {acc.lastname}, <br/>Email: {acc.email}</b>
        </section>
    )
}

export default About;