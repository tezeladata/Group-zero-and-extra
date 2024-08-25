import { useEffect, useState } from "react";

export default function Api() {
    const [text, setText] = useState("");

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
                const data = await response.json();
                setText(JSON.stringify(data));
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    console.log(text);

    return (
        <div>
            <p>{text}</p> {/* Display the fetched data */}
            <hr />
        </div>
    );
}