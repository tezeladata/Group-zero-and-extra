import React, { useEffect, useState } from "react";

export default function Classwork() {
    const [city, setCity] = useState("");
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {
        setCity(e.target.value);
    };

    useEffect(() => {
        if (!city) return;

        const fetchWeather = async () => {
            setLoading(true);
            try {
                const response = await fetch(
                    `http://api.weatherapi.com/v1/current.json?key=14cecb40ea2a4fb5a0d124826243008&q=${city}`
                );
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const json = await response.json();
                console.log(json);
                setData(json);
                setError(null);
            } catch (err) {
                console.error(err);
                setError(err.message);
                setData(null);
            } finally {
                setLoading(false);
            }
        };

        fetchWeather();
    }, [city]);

    return (
        <section className="w-full h-screen flex justify-center items-center flex-col">
            <form>
                <input type="text" onChange={handleChange} placeholder="Enter city name:" value={city} className="text-center text-white font-bold text-2xl p-5 bg-green-500 rounded-lg shadow-2xl border-2 border-black" />
                <br />
            </form>

            <h1 className="font-bold text-4xl p-10 text-white">Weather Info</h1>
            {loading && <p>Loading...</p>}
            {error && <p className="text-white">Error: {error}</p>}
            {data && (
                <div className="p-5 bg-green-500 rounded-2xl text-white">
                    <p className="font-bold text-center p-2">Location: {data.location.name}, {data.location.region}</p>
                    <p className="font-bold text-center p-2">Temperature: {data.current.temp_c} °C</p>
                    <p className="font-bold text-center p-2">Condition: {data.current.condition.text}</p>
                </div>
            )}
        </section>
    );
}