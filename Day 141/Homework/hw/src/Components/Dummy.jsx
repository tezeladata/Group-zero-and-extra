import {useState} from "react";

export const Dummy = () => {
    const [error, setError] = useState(false);

    if (error){
        throw new Error("Error occurred!")
    }
    return (
        <div>
            <h2>Hello World!</h2>
            <button onClick={() => setError(true)}>Generate error!</button>
        </div>
    )
}