import React, { useState } from 'react';

function Colorize() {
    const [color, setColor] = useState('');

    const handleClick = () => {
        const newColor = document.getElementById("color-input").value;
        setColor(newColor);
    };

    return (
        <div style={{ backgroundColor: color, height: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
            <p>Current color is {color}</p>
            <br />
            <input type="color" id="color-input" placeholder='Enter Color' />
            <button id='main-button' onClick={handleClick}>Change Color</button>
        </div>
    );
}

export default Colorize;