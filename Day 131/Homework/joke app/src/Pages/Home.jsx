import { Link } from "react-router-dom";

export default function Home() {
  return (
    <section className="bg-gray-600 flex items-center justify-center flex-col h-screen">
      <h1 className="text-4xl p-5">Jokes website</h1>
      <Link to="/jokes">
        <button className="font-bold text-3xl">Click to generate joke</button>
      </Link>
    </section>
  );
}