import React, { useEffect, useState } from "react";

export default function Weather() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWeather = async () => {
      try {
        const response = await fetch(
          "http://api.weatherapi.com/v1/current.json?key=14cecb40ea2a4fb5a0d124826243008&q=Tbilisi"
        );
        const json = await response.json();
        setData(json);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchWeather();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <section>
      <h1>Weather Info</h1>
      {data && (
        <div>
          <p>Location: {data.location.name}, {data.location.region}</p>
          <p>Temperature: {data.current.temp_c} °C</p>
          <p>Condition: {data.current.condition.text}</p>
        </div>
      )}
    </section>
  );
}