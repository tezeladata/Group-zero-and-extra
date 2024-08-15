import React, { useState } from 'react';

const Hw4 = () => {
    const [background, setBackground] = useState();

    const backgroundChanger = () => {
        const colors = ["#111", "#222", "#333", "#444", "#555", "#666", "#777", "#888", "#999"];
        const randomIndex = Math.floor(Math.random() * colors.length);
        setBackground(colors[randomIndex]);
    }

    return (
        <section style={{width: '400px', backgroundColor: background}}>
            <hr />
            <button onClick={backgroundChanger}>Click to change background</button>
            <hr />
        </section>
    );
}

export default Hw4;