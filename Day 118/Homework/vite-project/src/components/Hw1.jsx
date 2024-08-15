import React, { useState } from 'react';

const Hw1 = () => {
    const [count, setcount] = useState(0);
    const increment = () => {
        setcount(count +1);
    }
    const decrement = () => {
        setcount(count -1);
    }
    const zero = () => {
        setcount(0);
    }

    return (
        <section>
            <hr />
            <p>Count: {count}</p>
            <button onClick={increment}>+1</button>
            <button onClick={decrement}>-1</button>
            <button onClick={zero}>Back to 0</button>
            <hr />
        </section>
    );
}

export default Hw1;