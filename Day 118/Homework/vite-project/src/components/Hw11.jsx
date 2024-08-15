import React, { useState } from "react";

const Hw11 = () => {
    const [count, setCount] = useState(0);

    const counter = () => {
        setCount(document.getElementById("main-input").value.length)
    }

    return (
        <div>
            <hr />
            <input type="text" id="main-input" placeholder="Enter text" onChange={counter}/>
            <p>{count}</p>
            <hr />
        </div>
    );
};

export default Hw11;