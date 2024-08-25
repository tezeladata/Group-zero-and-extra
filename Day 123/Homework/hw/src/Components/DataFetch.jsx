import { useEffect, useState } from "react";

export default function DataFetch() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        let isMounted = true;

        const fetchData = async () => {
            try {
                const response = await fetch('https://jsonplaceholder.typicode.com/todos');
                const result = await response.json();
                if (isMounted) {
                    setData(result);
                    setLoading(false);
                }
            } catch (err) {
                if (isMounted) {
                    setError(err);
                    setLoading(false);
                }
            }
        };

        fetchData();

        return () => {
            isMounted = false;
        };
    }, []);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error.message}</p>;

    return (
        <div>
            <ul>
                {data.map(item => (
                    <li key={item.id}>{item.title}</li>
                ))}
            </ul>

            <hr />
        </div>
    );
}