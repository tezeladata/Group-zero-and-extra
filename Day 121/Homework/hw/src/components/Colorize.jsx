import { useState } from "react";

export default function Colorize(){
    const [color, setColor] = useState("#FFF")

    const handleChange = (e) => {
        setColor(e.target.value)
    }

    return (
        <div>
            <input type="color" name="input1" onChange={handleChange} />
            <div style={{width: '200px', height: '200px', backgroundColor: color, display: 'flex', justifyContent: "center", alignItems: 'center'}}>
                <p>Preview box</p>
            </div>  
        </div>
    )
}