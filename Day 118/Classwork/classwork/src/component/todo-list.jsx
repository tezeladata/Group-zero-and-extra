import React, { useState } from "react";

export default function Todo() {
  const [tasks, setTasks] = useState([]);
  const [task, setTask] = useState("");
  const [time, setTime] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    setTasks([...tasks, <p>{task} {time}</p>]);
    setTask("");
    setTime("");
  };

  return (
    <div>
      <form id="main-form" onSubmit={handleSubmit}>
        <input type="text" placeholder="Enter task: " name="task" value={task} onChange={(e) => setTask(e.target.value)} />
        <input type="number" placeholder="Enter time: " name="time" value={time} onChange={(e) => setTime(e.target.value)} />
        <button type="submit">Submit Task</button>
      </form>

      <div>
        {tasks}
      </div>
    </div>
  );
}