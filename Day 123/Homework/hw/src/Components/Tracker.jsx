import { useEffect, useState } from "react";

export default function Tracker(){
    const [text, setText] = useState("");

    useEffect(() => {
        alert(text)
    }, [text])

    const handleChange = (e) => {
        setText(e.target.value)
    }

    return (
        <div>
            <input type="text" placeholder="Enter title:" onChange={handleChange}/>
            <hr />
        </div>
    )
}