import {useContext} from "react";
import {dataContext} from "../context/dataContext.jsx";

const Photos = () => {
    const {acc} = useContext(dataContext);

    console.log(acc);

    return (
        <section>
            <h1>Photos component</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur, quas!</p>

            <br />
            <b>Name: {acc.firstname}, <br />Surname: {acc.lastname}, <br/>Email: {acc.email}</b>
        </section>
    )
}

export default Photos;