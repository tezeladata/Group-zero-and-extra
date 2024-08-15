import React, { useState } from "react";
import "./hw14.css"

export default function Hw14(){
    const [color, setColor] = useState("");

    const colorize = (e) => {
        e.preventDefault();
        setColor(document.getElementById("select1").value)
    }

    return (
        <div id="hw14-div" style={{backgroundColor: color}}>
            <hr />
            <form onSubmit={colorize}>
                <select id="select1">
                    <option value="red">red</option>
                    <option value="blue">blue</option>
                    <option value="green">green</option>
                    <option value="yellow">yellow</option>
                    <option value="purple">purple</option>
                </select>
                <button type="submit">Submit</button>
            </form> 

            <hr />
        </div>
    )
}