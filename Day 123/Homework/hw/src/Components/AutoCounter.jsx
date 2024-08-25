import { useEffect, useState } from "react";

export default function AutoCounter(){
    const [num, setNum] = useState(0);

    useEffect(() => {
        const intervalId = setInterval(() => {
            setNum(prev => prev + 1)
        }, 1000);

        return () => clearInterval(intervalId)
    }, [])

    return (
        <div>
            <p>Number: {num}</p>

            <hr />
        </div>
    )
}