import React, { useState } from 'react';

const Hw8 = () => {
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
            <button onClick={changeVisibility}>Click to see Password</button>
            <p id='p1' style={{display: visibility}}>12345678</p>
            <hr />
        </section>
    );
}

export default Hw8;