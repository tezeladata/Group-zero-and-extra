import React, { useState } from "react";
import "../section1.css";

function Section1() {
    const [appear, setAppear] = useState(true);

    const handleClick = () => {
        setAppear(prevAppear => !prevAppear);
    };

    return (
        <div>
            <button onClick={handleClick}>Click here to {appear ? "hide" : "show"} paragraph</button>
            {appear && <p id="main-par">This was supposed to be a hidden paragraph</p>}
        </div>
    );
}

export default Section1;