import { useState } from 'react';
import Weather from './Weather';

export default function Home() {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setCity('');

    if (city.trim()) {
      try {
        const apiKey = '238daee9e898e1e4618031c00ce980e4';
        const response = await fetch(
          `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`
        );
        const weatherData = await response.json();
        console.log(weatherData);

        const newInfo = {
          city: weatherData.name,
          temp: weatherData.main.temp,
          longitude: weatherData.coord.lon,
          latitude: weatherData.coord.lat,
          timeZone: weatherData.timezone,
          description: weatherData.weather[0].description
        };
        setWeather(newInfo);

      } catch (error) {
        alert('Error fetching weather data:', error);
      }
    }
  };

  return (
    <section className="w-full h-screen flex items-center justify-center flex-col bg-yellow-600">
      <h1 className="text-4xl p-5">Hello, this is simple weather site</h1>

        <form onSubmit={handleSubmit} className="w-1/4 flex flex-col items-center justify-center mb-5">
            <input type="text" placeholder="Enter city name" value={city} onChange={(e) => setCity(e.target.value)} className="w-2/4 text-center font-bold text-2xl p-3 rounded-2xl"/>
            <br />

            <button type="submit" className="bg-gray-600 p-5 text-white cursor-pointer rounded-2xl m-4">Get Weather</button>
        </form>

        {weather && (
        <Weather
          city={weather.city}
          temp={weather.temp}
          longitude={weather.longitude}
          latitude={weather.latitude}
          timeZone={weather.timeZone}
          description={weather.description}
        />
      )}
    </section>
  );
}
