import Clicker from "./Components/Clicker.jsx";
import {useState} from "react";

const App = () => {
    const [number, setNumber] = useState(0);

    return (
        <>
            <Clicker />

            <section>
                <hr/>
                <hr/>
                <hr/>
                <p>Number: {number}</p>
                <button onClick={() => setNumber(number + 1)}>Click to increase</button>
            </section>
        </>
    )
}

export default App;