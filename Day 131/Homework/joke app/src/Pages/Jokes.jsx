import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function Jokes() {
  const [data, setData] = useState(null);
  const [next, setNext] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("https://v2.jokeapi.dev/joke/Programming?blacklistFlags=sexist&type=single");

        if (!response.ok) {
            alert("error")
        }

        const result = await response.json();
        setData(result);
      } catch (error) {
        alert("error")
      } 
    };

    fetchData();
  }, [next]);

  console.log(data)

  return (
    <section className="h-screen flex items-center justify-center flex-col bg-green-950 ">
      <p className="text-white font-bold text-3xl text-center max-w-lg">{data?.joke || "Loading..."}</p> 
      <br />
      <button onClick={() => setNext(prev => prev + 1)} className="text-white font-bold rounded-full bg-gray-700 p-5">Click to generate next joke</button>
      <Link to={'/'} className="p-5 text-4xl text-gray-700 font-bold">Back to home page</Link>
    </section>
  );
}