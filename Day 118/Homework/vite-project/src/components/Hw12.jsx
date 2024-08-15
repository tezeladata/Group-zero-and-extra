import React, { useState } from "react";
import "./hw12.css";

const Hw12 = () => {
    const [time, setTime] = useState(0); 

    const main = (e) => {
        e.preventDefault();
        let total = document.getElementById("form1").minutes.value * 60 + 
                    parseInt(document.getElementById("form1").seconds.value, 10);

        const intervalId = setInterval(() => {
            setTime(total);
            total -= 1;
            if (total < 0) {
                clearInterval(intervalId); 
            }
        }, 1000);
    }

    const formatTime = (seconds) => {
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
    }

    return (
        <div>
            <hr />
            <form id="form1" onSubmit={main}>
                <input type="number" name="minutes" placeholder="Enter minutes" required min="0" />
                <input type="number" name="seconds" placeholder="Enter seconds" required min="0" max="59" />
                <button type="submit">Start Timer</button>
            </form>
            <p id="display-p">{time > 0 ? formatTime(time) : "Time's up!"}</p>
            <hr />
        </div>
    );
};

export default Hw12;