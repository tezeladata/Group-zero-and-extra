import React, { useState } from 'react';

const Todo = () => {
    const [task, setTask] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        setTask([...task, e.target.input1.value]);
        e.target.input1.value = ''; // Clear
    }

    const handleDelete = (index) => {
        setTask(task.filter((_, i) => i !== index));
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder='Enter task: ' name='input1'/>
                <button>Submit</button>
            </form>
            <br />

            <ul>
                {
                    task.map((name, index) => (
                        <li key={index} onClick={() => handleDelete(index)}>{name}</li>
                    ))
                }
            </ul>

            <hr />
        </div>
    );
};

export default Todo;