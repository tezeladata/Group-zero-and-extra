import { useState } from "react"

const Counter = () => {
    // We need hook, because count has to be rendered again
    const [count, setCount] = useState(0);
    const increment = () => {
        setCount(count + 1);
        // This is used for rendering
    }
    const decrement = () => {
        setCount(count - 1);
    }
    const reset = () => {
        setCount(0)
    }

    return (
        // jsx is written here
        <div>
          <p>Count: {count}</p>
          <button onClick={increment}>+1</button>
          <button onClick={decrement}>-1</button>
          <button onClick={reset}>Reset</button>
          <hr></hr>
        </div>
    )
}

export default Counter


// vanilla js is imperative way to write code. We tell browser what to do and how to do
// But in react, we use declarative way to write code. It's much easier