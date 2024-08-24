import React, { useState } from 'react';

export default function Theme(){
    const [background, setBackground] = useState("#FFF");

    const handleClick = () => {
        if (background === "#FFF"){
            setBackground("#000");
        } else{
            setBackground("#FFF");
        }
    }

    return (
        <div style={{ backgroundColor: background, height: '500px' }}>
            <button onClick={handleClick}>Click here to change background color of current div</button>
        </div>
    );
}