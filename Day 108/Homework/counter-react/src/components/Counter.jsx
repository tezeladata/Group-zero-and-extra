import { useState } from "react"

const Counter = () => { 
  const [count, setCount] = useState(0);

  const addOne = () => {
    setCount(count + 1);
  };
  
  const removeOne = () => {
    setCount(count - 1);
  };
  
  const reset = () => {
    setCount(0);
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={addOne}>+1</button>
      <button onClick={removeOne}>-1</button>
      <button onClick={reset}>Reset</button>
      <hr></hr>
    </div>
  )
}

export default Counter
