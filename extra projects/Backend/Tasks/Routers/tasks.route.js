// Modules
import express from 'express';

// Utils
import readFile from "../Utils/readFile.js";
import writeFile from "../Utils/writeFile.js";

// db
import {TASKS_FILE} from "../app.js";

// Router
export const tasksRouter = express.Router();

// Get all tasks
tasksRouter.get("/", async (req, res) => {
    try {
        // Get tasks
        const data = await readFile(TASKS_FILE);

        // If empty
        if (data.length === 0){
            return res.status(400).send("Database is empty")
        }

        return res.status(200).json(data);
    } catch (e) {
        res.status(400).send("Failed to read data")
    }
})

// Get single task
tasksRouter.get("/:id", async (req, res) => {
    try {
        // Id of task
        const id = parseInt(req.params.id);

        // Get all tasks
        const data = await readFile(TASKS_FILE);

        // Find task
        const task = data.filter(t => t.id === id);

        // If task not found
        if (task.length === 0){
            return res.status(404).send({ "error": "Task not found" })
        }

        // Return task
        return res.status(200).json(task)
    } catch (e) {
        return res.status(400).send("Failed to read data")
    }
})

// Add new task
tasksRouter.post("/", async (req, res) => {
    try {
        // New task
        const task = req.body;

        // Get data
        const data = await readFile(TASKS_FILE);
        const len = data.length;

        // Task already exists
        const matching = data.filter(t => t.title === task.title);
        if (matching.length > 0){
            return res.status(400).send("Task already exists")
        }

        // Update task and save it to tasks
        task.id = len
        data.push(task);

        // Save tasks to JSON file
        await writeFile(TASKS_FILE, data)

        return res.status(200).json(task);
    } catch (e) {
        return res.status(400).send("Failed to create data");
    }
})

// Update existing task
tasksRouter.put("/:id", async (req, res) => {
    try {
        // Id of task
        const id = parseInt(req.params.id);

        // task and it's eligibility
        const task = req.body;
        if ((!Object.keys(task).includes("title") || !Object.keys(task).includes("completed")) && task.length !== 2){
            return res.status(400).send("Wrong body for task")
        }

        // Get data
        const data = await readFile(TASKS_FILE);

        // Find task by id
        const foundTask = data.filter(t => t.id === id);

        // Task not found
        if (foundTask.length === 0){
            return res.status(404).send(`No task found with id ${id}`)
        }

        // Update task
        foundTask[0].title = task.title;
        foundTask[0].completed = task.completed;

        // Save changes to db
        await writeFile(TASKS_FILE, data);

        return res.status(200).json(foundTask);
    } catch (e) {
        return res.status(400).send("Failed to update data")
    }
})

// Delete task
tasksRouter.delete("/:id", async (req, res) => {
    try {
        // Id of task
        const id = parseInt(req.params.id);

        // Get data
        let data = await readFile(TASKS_FILE);

        // Check if task exists with given id
        const taskExists = data.filter(t => t.id === id).length > 0;
        if (!taskExists){
            return res.status(404).send(`No task found with id ${id}`)
        }

        // update tasks
        data = data.filter(t => t.id !== id);

        // Save changes
        await writeFile(TASKS_FILE, data);

        return res.status(200).json({ "message": "Task deleted" });
    } catch (e) {
        return res.status(400).send("Failed to delete task")
    }
})