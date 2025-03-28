import { Route, Routes } from "react-router";
import Register from "./Components/Register";
import Login from "./Components/Login";

const App = () => {
  return (
    <main className="bg-gray-800 min-h-[100vh]">
      <Routes>
        <Route path="/" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </main>
  )
}

export default App;