import React, { useState } from 'react';

const Hw7 = () => {
    const [text, setText] = useState("Hello");

    const texter = () => {
        if (text === "Like"){
            setText("Unlike");
        } else{
            setText("Like");
        }
    };

    return (
        <section>
            <hr />
            <button onClick={texter}>Click to set Text</button>
            <p id='p1'>{text}</p>
            <hr />
        </section>
    );
}

export default Hw7;