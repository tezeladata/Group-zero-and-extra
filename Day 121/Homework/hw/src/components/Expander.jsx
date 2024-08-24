import { useState } from "react";

export default function Expander(){
    const [display, setDisplay] = useState("None");
    const [text, setText] = useState("See more");

    const handleClick = () => {
        if (display == "None"){
            setDisplay("Block")
            setText("See less")
        } else{
            setDisplay("None")
            setText("See more")
        }
    }

    return (
        <div>
            <p>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Natus ducimus minus facere dolores molestias. 
                <span id="span1" style={{display: display}}>numquam nihil assumenda repellendus voluptates dicta ullam error consequuntur quidem voluptatibus. Autem quidem incidunt dicta eaque?</span>
            </p>
            <button onClick={handleClick}>{text}</button>
        </div>
    )
}