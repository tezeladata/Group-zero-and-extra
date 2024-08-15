import React, { useState } from 'react';

const Hw2 = () => {
    const [text, setText] = useState("Hello");

    const texter = () => {
        if (text === "Hello"){
            setText("Goodbye");
        } else{
            setText("Hello");
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

export default Hw2;