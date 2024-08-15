import React, { useState } from "react";
import './Hw10.css';  
import cssImage from "../assets/css.png"; 
import htmlImage from "../assets/html.png"; 
import jsImage from "../assets/js.png"; 
import pythonImage from "../assets/python.png"; 
import reactImage from "../assets/react.png"; 

const Hw10 = () => {
    const [index, setIndex] = useState(0); 

    const imageArr = [cssImage, htmlImage, jsImage, pythonImage, reactImage];

    const next = () => {
        setIndex((prevIndex) => (prevIndex + 1) % imageArr.length);
    }

    const prev = () => {
        setIndex((prevIndex) => (prevIndex - 1 + imageArr.length) % imageArr.length);
    }

    return (
        <div>
            <hr />
            <img src={imageArr[index]} alt="Technology" id="main-img" />
            <button onClick={prev}>Previous</button>
            <button onClick={next}>Next</button>
            <hr />
        </div>
    );
}

export default Hw10;