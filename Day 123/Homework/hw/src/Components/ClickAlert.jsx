import { useEffect, useState } from "react";

export default function ClickAlert(){
    const [count, setCount] = useState(0);

    useEffect(() => {
        if (count < 5){
            console.log(count)
        } else{
            alert(count)
        }
    })

    return (
        <div>
            <p>{count}</p>
            <button onClick={() => setCount(prev => prev + 1)}>Click me</button>

            <hr />
        </div>
    )
}