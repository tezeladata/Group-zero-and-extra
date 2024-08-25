import { useState } from "react"

export default function Visibility(){
    const [display, setDisplay] = useState("Block");

    const handleClick  = () => {
        if (display === "Block"){
            setDisplay("None")
        } else{
            setDisplay("Block")
        }
    }

    return (
        <div>
            <p style={{display: display}}>Hello there!</p>
            <button onClick={() => handleClick()}>Click here to change Visibility</button>

            <hr />
        </div>
    )
}