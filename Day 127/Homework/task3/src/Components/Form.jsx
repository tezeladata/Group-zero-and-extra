import React, { useState, useEffect } from "react";

export default function Form() {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    const storedUsers = JSON.parse(localStorage.getItem("users")) || [];
    setUsers(storedUsers);
  }, []);

  const handleRegister = () => {
    if (!name || !email) {
      alert("Please fill out all fields.");
      return;
    }

    const newUser = { name, email };

    // Check if user already exists
    const userExists = users.some(
      (user) => user.email.toLowerCase() === newUser.email.toLowerCase()
    );

    if (userExists) {
      alert("An account with this email already exists.");
    } else {
      const updatedUsers = [...users, newUser];
      setUsers(updatedUsers);
      localStorage.setItem("users", JSON.stringify(updatedUsers));
      alert("User registered successfully!");
      setName("");
      setEmail("");
    }
  };

  return (
    <section className="p-4">
      <h1 className="text-2xl font-bold mb-4">User Registration</h1>
      <form
        className="flex flex-col gap-4 max-w-sm"
        onSubmit={(e) => e.preventDefault()}
      >
        <input
          type="text"
          className="border border-gray-300 p-2 rounded"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="email"
          className="border border-gray-300 p-2 rounded"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button
          type="button"
          className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
          onClick={handleRegister}
        >
          Register
        </button>
      </form>
      <h2 className="text-xl font-bold mt-6">Registered Users:</h2>
      <ul className="mt-2">
        {users.map((user, index) => (
          <li key={index} className="border-b border-gray-200 py-2">
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    </section>
  );
}