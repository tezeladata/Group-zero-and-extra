import { useState } from "react";

const Counter = () => {
    const [count, setCount] = useState(0);

    // Plus
    const addOne = () => setCount(prevCount => prevCount + 1);
    const addFive = () => setCount(prevCount => prevCount + 5);
    const addTen = () => setCount(prevCount => prevCount + 10);

    // Reset
    const reset = () => setCount(0);

    // Minus
    const removeOne = () => setCount(prevCount => prevCount - 1);
    const removeFive = () => setCount(prevCount => prevCount - 5);
    const removeTen = () => setCount(prevCount => prevCount - 10);

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={addOne}>+1</button>
            <button onClick={addFive}>+5</button>
            <button onClick={addTen}>+10</button>
            <button onClick={reset}>Reset</button>
            <button onClick={removeOne}>-1</button>
            <button onClick={removeFive}>-5</button>
            <button onClick={removeTen}>-10</button>
            <hr />
        </div>
    );
};

export default Counter;