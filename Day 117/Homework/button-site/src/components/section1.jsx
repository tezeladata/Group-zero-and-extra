import React from "react";
import "../section1.css"

function Section1(){
    let appear = true;
    const handleClick = () => {
        appear = !appear;

        if (appear){document.getElementById("main-par").style.display = "block";}
        else {document.getElementById("main-par").style.display = "none";}

        console.log(appear)
    }

    return (
        <div>
            <button onClick={handleClick}>Click here to show paragraph</button>
            <p id="main-par">This was supposed to be hidden paragraph</p>
        </div>
    )
}

export default Section1;