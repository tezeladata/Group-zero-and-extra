import express from "express";
import cors from "cors";
import fs from "fs";
import path from 'path';
import { fileURLToPath } from 'url';

const app = express();

// middleware
app.use(cors());
app.use(express.json());

// db
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.resolve(__dirname, './tasks.json');

// utils
const readDatabase = async () => {
    try {
        const data = await fs.promises.readFile(filePath, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        throw new Error('Failed to read or parse file');
    }
};
const writeDatabase = async (data) => {
    try {
        await fs.promises.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8');
    } catch (error) {
        console.error('Error writing to the database:', error);
        throw new Error('Unable to write to database');
    }
};

// Get all tasks
app.get("/tasks", async (req, res) => {
    const { limit } = req.query;
    try {
        let tasks = await readDatabase();

        if (limit) {
            tasks = tasks.splice(0, limit);
        }

        res.json(tasks)
    } catch(error) {
        console.log(error)
    }
})

// Get single task by ID
app.get("/tasks/:id", async (req, res) => {
    const id = parseInt(req.params.id);

    try {
        const tasks = await readDatabase();

        const result = tasks.filter(task => task.id === id);

        res.json(result)
    } catch(error) {
        console.log(error)
    }
})

// Add task
app.post("/tasks", async (req, res) => {
    try {
        let tasks = await readDatabase();

        let newTask = {"id": tasks.length + 1, ...req.body};

        tasks.push(newTask);
        writeDatabase(tasks);

        res.json(tasks);
    } catch(e) {
        console.log(e)
    }
})

// Edit task by ID
app.put("/tasks", async (req, res) => {
    try {
        let tasks = await readDatabase();

        const { id, name, duration } = req.body;

        if (!id) {return res.status(400).send("ID not given")};

        const ind = tasks.findIndex(task => task.id === id);
        if (ind === -1) {return res.status(400).send("Wrong id")};
        tasks[ind] = {...tasks[ind], name, duration};
        writeDatabase(tasks)

        res.json(tasks);
    } catch(e) {
        console.log(e)
    }
});

// Delete task by ID
app.delete("/tasks", async (req, res) => {
    const { id } = req.query;
    try {
        let tasks = await readDatabase();
        
        if (!id) {return res.status(400).send("ID not given")};

        tasks = tasks.filter(task => task.id !== parseInt(id));
        writeDatabase(tasks);

        res.json(tasks);
    } catch(e) {
        console.log(e)
    }
})

// Start server
app.listen(3000, () => console.log("Server started on port 3000"))