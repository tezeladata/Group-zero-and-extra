import {useState} from "react";

export const Dummy = () => {
    const [error, setError] = useState(false);

    if (error) {
        throw new Error("Something went wrong");
    }

    return (
        <div>
            <h2>Hello world</h2>
            <button onClick={() => setError(true)}>Generate error</button>
        </div>
    )
}