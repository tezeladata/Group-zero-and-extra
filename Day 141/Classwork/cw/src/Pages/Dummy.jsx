import {useState} from "react";

export const Dummy = () => {
    const [error, setError] = useState(false)
    if (error) {
        throw new Error("Error found!")
    }

    return (
        <div>
            <h2>Hello</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius, molestias.</p>
            <button onClick={() => setError(true)}>Click to generate error</button>
        </div>
    )
}