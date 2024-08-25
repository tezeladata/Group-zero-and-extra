import { useState } from "react";

export default function Title(){
    const [text, setText] = useState("");

    const handleChange = (e) => {
        setText(e.target.value)
        document.title = text
    }

    return (
        <div>
            <input type="text" placeholder="Enter title:" onChange={handleChange}/>
            <hr />
        </div>
    )
}