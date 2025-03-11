import { useEffect, useState } from "react";

const App = () => {
  const [tasks, setTasks] = useState([]);
  const [editing, setEditing] = useState(false);
  const [currentTask, setCurrentTask] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    const newTask = {
      name: e.target.name.value,
      description: e.target.description.value,
      time: `${new Date().getHours()}:${new Date().getMinutes()}, ${new Date().getMonth() + 1}/${new Date().getDate()}/${new Date().getFullYear()}`,
      id: editing ? currentTask.id : tasks.length + 1,
    };

    if (editing) {
      setTasks((prevTasks) => prevTasks.map((task) => (task.id === currentTask.id ? newTask : task)));
      setEditing(false);
      setCurrentTask(null);
    } else {
      setTasks((prevTasks) => [...prevTasks, newTask]);
    }

    e.target.name.value = "";
    e.target.description.value = "";
  };

  const handleEdit = (task) => {
    setEditing(true);
    setCurrentTask(task);
  };

  const handleDelete = (taskId) => {
    setTasks((prevTasks) => prevTasks.filter((task) => task.id !== taskId));
  };

  return (
    <main className="min-h-[100vh] bg-gray-900 flex flex-col">
      {/* form section */}
      <section className="w-full">
        <div className="mx-10 my-5 bg-gray-700 p-5 rounded-lg">
          <h1 className="text-3xl pb-4 text-white drop-shadow-[0px_0px_27px_rgba(1,98,46,1)]">
            {editing ? "Edit" : "Create"} a task
          </h1>
          <form className="pt-4 w-full flex gap-x-20" onSubmit={handleSubmit}>
            <input type="text" name="name" placeholder="Enter task name:" defaultValue={editing ? currentTask.name : ""} className="text-xl py-2 pl-2 bg-black text-white rounded-lg font-bold" required/>
            <input type="text" name="description" placeholder="Enter task description: " defaultValue={editing ? currentTask.description : ""} className="text-xl py-2 pl-2 bg-black text-white rounded-lg font-bold" required
/>
            <button className="bg-black text-white border border-gray-900 text-lg border-b-6 font-medium overflow-hidden relative px-4 py-2 rounded-md hover:brightness-150 hover:border-t-6 hover:border-b active:opacity-75 outline-none duration-300 group cursor-pointer">
              <span className="bg-white shadow-white absolute -top-[150%] left-0 inline-flex w-80 h-[5px] rounded-md opacity-50 group-hover:top-[150%] duration-500 shadow-[0_0_10px_10px_rgba(0,0,0,0.3)]"></span>
              {editing ? "Save" : "Create"} Task
            </button>
          </form>
        </div>
      </section>

      {/* tasks div */}
      <section className="w-full">
        <div className="mx-10 my-5 bg-gray-700 p-5 rounded-lg grid grid-cols-3 gap-x-5 gap-y-5">
          {tasks.map((item) => (
            <div key={item.id} className="bg-white p-4 flex flex-col relative rounded-lg">
              <h2 className="text-2xl font-bold pb-2 max-w-[80%]">{item.name}</h2>
              <p>{item.description}</p>
              <b className="pb-5">Task created at: {item.time}</b>
              <i className="absolute right-2 bottom-2 cursor-pointer" onClick={() => handleDelete(item.id)}>❌</i>
              <i className="absolute right-2 top-2 cursor-pointer" onClick={() => handleEdit(item)}>✏️</i>
              <p>{item.id}</p>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
};

export default App;