import { useState } from "react";

const Tester = () => {
  const [error, setError] = useState(false);

  const fetcher = async () => {
    setError(false);

    try {
      const response = await fetch('https://jsonplaceholder.typicdos/1');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const jsonData = await response.json();
      console.log(jsonData);
    } catch (err) {
      setError(true);
    }
  };

  if (error){
      throw new Error('Network response was not ok');
  }

  return (
    <section>
      <button onClick={fetcher}>Click to fetch Data</button>
    </section>
  );
};

export default Tester;