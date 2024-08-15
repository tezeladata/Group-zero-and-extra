import React, { useState } from 'react';

const Hw3 = () => {
    const [visibility, setVisibility] = useState("Block");

    const changeVisibility = () => {
        if (visibility === "Block"){
            setVisibility("None")
        } else{
            setVisibility("Block")
        }
    };

    return (
        <section>
            <hr />
            <button onClick={changeVisibility}>Click to see Text</button>
            <p id='p1' style={{display: visibility}}>Hello there</p>
            <hr />
        </section>
    );
}

export default Hw3;