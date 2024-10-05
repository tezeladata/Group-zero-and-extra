import {Dummy} from "./Dummy.jsx";
import Fallback from "../Error handling/Fallback.jsx";

const Home = () => {
    return (
        <main>
            <Fallback>
                <Dummy />
                <Dummy />
            </Fallback>

            <Fallback>
                <Dummy />
                <Dummy />
            </Fallback>
        </main>
    )
};

export default Home;