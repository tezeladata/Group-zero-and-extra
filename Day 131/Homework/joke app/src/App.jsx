import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./Pages/Home.jsx";
import Jokes from "./Pages/Jokes.jsx";
import './index.css';

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/jokes" element={<Jokes />} />
    </Routes>
  );
}