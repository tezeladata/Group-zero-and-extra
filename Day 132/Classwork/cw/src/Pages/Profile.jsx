import {dataContext} from "../context/dataContext.jsx";
import {useContext} from "react";

const Profile = () => {
    const {acc} = useContext(dataContext);

    return (
        <section>
            <h1>Profile component</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur, quas!</p>

            <br/>
            <b>Name: {acc.firstname}, <br/>Surname: {acc.lastname}, <br/>Email: {acc.email}</b>
        </section>
    )
}

export default Profile;