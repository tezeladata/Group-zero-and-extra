export default function Weather({ city, temp, longitude, latitude, timeZone, description }) {
  return (
      <section className="text-center">
          <hr className="mb-3"/>
          <h1 className="text-2xl">Weather for <span className="font-bold">{city}</span></h1>
          <h2>Weather: {description}</h2>
          <p>Temperature: {temp} °C</p>
          <b>Latitude: {latitude}, Longitude: {longitude}</b> <br/>
          <i>Timezone: {timeZone}</i>
          <hr className="mt-3"/>
      </section>
  );
}