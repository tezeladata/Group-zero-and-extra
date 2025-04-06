import express from "express";
import readFile from "../Utils/readFile.js";
import writeFile from "../Utils/writeFile.js";

// Route
export const todo = express.Router();

// database
const filepath = "./Database/todos.json"

// get all tasks
todo.get("/", async (req, res) => {
    const { limit, status, priority } = req.query;
    try {
        // Get data
        let data = await readFile(filepath);

        // queries
        if (limit) {
            if (limit < 0) {
                return res.status(404).send("Limit should be non-negative number")
            }
            if (limit > data.length) {
                return res.status(404).send("Limit is higher than the count of elements")
            }
            data = data.splice(0, parseInt(limit))
        }

        if (status) {
            switch (status) {
                case "completed":
                    data = data.filter(item => item.status === "completed");
                    if (data.length === 0) {
                        return res.status(404).send("No tasks are completed");
                    }
                    break;
                case "in-progress":
                    data = data.filter(item => item.status === "in-progress");
                    if (data.length === 0) {
                        return res.status(404).send("No tasks are in-progress");
                    }
                    break;
                default:
                    return res.status(404).send("Wrong value for query named status");
            }
        }

        if (priority) {
            if (priority) {
                switch (priority) {
                    case "low":
                        data = data.filter(item => item.priority === "low");
                        break;
                    case "normal":
                        data = data.filter(item => item.priority === "normal");
                        break;
                    case "high":
                        data = data.filter(item => item.priority === "high");
                        break;
                    default:
                        return res.status(404).send("Wrong value for query named priority");
                }
            }
        }
        
        // Send tasks
        res.status(200).json(data)
    } catch (e) {
        return res.status(400).send("Database could not be read")
    }
})

// Get single task
todo.get("/:id", async (req, res) => {
    const id = req.params.id;

    try {
        const data = await readFile(filepath);
        
        // Find task
        const task = data.filter(item => item.title === id);
        
        // Not found
        if (task.length === 0){
            return res.status(404).send("Task not found")
        } 

        res.status(200).json(task);
    } catch (e) {
        return res.status(404).send(e)
    }
})

// Post task
todo.post("/", async (req, res) => {
    const {title, description, priority} = req.body;

    try {
        const data = await readFile(filepath);

        // Insufficient information
        if (title === undefined || description === undefined || priority === undefined){
            return res.status(404).send("Not enough information - properties missing")
        }

        // Task already exists with same title
        const alreadyExists = data.filter(item => item.title === title);
        if (alreadyExists.length > 0) {
            return res.status(404).send("Task already exists with same title")
        }

        // Create new task
        const newTask = {"id": data.length, title, description, "status": "in-progress", priority};
        
        // Add task to array
        data.push(newTask);
        
        // Save changes
        await writeFile(filepath, data);

        return res.status(200).send("Task added successfully");
    } catch (e) {
        return res.status(404).send(e)
    }
})

// Put task
todo.put("/", async (req, res) => {
    const {title, status, priority} = req.body;

    try {
        const data = await readFile(filepath);

        // Insufficient information
        if (title === undefined || status === undefined || priority === undefined) {
            return res.status(404).send("Not enough information - properties missing")
        }

        // Find task
        let task = data.filter(item => item.title === title);
        
        // Task not found
        if (task.length === 0){
            return res.status(404).send("Task not found - wrong title")
        }        

        task = task[0]

        // No changes made to task
        if (task.status === status && task.priority === priority){
            return res.status(400).send("No changes made to task")
        }

        // save changes
        task.status = status;
        task.priority = priority;
        await writeFile(filepath, data)

        return res.status(200).send("Task edited successfully")
    } catch(e) {
        return res.status(404).send(e)
    }
})

// Delete task
todo.delete("/:id", async (req, res) => {
    const id = parseInt(req.params.id);

    try {
        let data = await readFile(filepath);
        const startLen = data.length;

        // Filter data
        data = data.filter(item => item.id !== id);
        const endLen = data.length;

        // No changes made to array
        if (startLen === endLen) {
            return res.status(404).send("No changes made to database")
        }

        // Save changes
        await writeFile(filepath, data);

        return res.status(200).send("Task deleted successfully")
    } catch(e) {
        return res.status(404).send(e)
    }
})