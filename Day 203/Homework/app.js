import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import dotenv from "dotenv";

// utils
import readFile from "./utils/readFile.js";
import writeFile from "./utils/writeFile.js"

// Server
const app = express();

// Port
dotenv.config();
const PORT = process.env.PORT;

// Dbs
const DATA_FILE = process.env.DATA_FILE;
const LOGS_FILE = process.env.LOGS_FILE;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(async (req, res, next) => {
    console.log("\nLogger middleware\n")
    console.log(`Method: ${req.method}\nPath: ${req.path}\nURL: ${req.url}`);
    for (let key in req.query){
        console.log(`Query key: ${key}, Query value: ${req.query[key]}`)
    };
    console.log("\nInformation of request logged in console!\n");

    // Add log to logs file
    const data = [["Method", req.method], ["Path", req.path], ["Url", req.url], ["Query", req.query], ["Params", req.params]];
    const prev = await readFile(LOGS_FILE);
    prev.push(data)
    await writeFile(LOGS_FILE, JSON.stringify(prev));

    // To next middleware
    next();
})


// Routes

// Get all tasks
app.get("/tasks", async (req, res) => {
    const {completed} = req.query;
    try {
        let data = await readFile(DATA_FILE);

        if (completed === "true"){
            data = data.filter(item => item.completed === "true")
        } else if (completed === "false"){
            data = data.filter(item => item.completed === "false")
        }

        res.status(200).json(data)
    } catch(e) {
        return res.status(404).send(e)
    }
})

// Get task by ID
app.get("/tasks/:id", async (req, res) => {
    const id = parseInt(req.params.id);
    try {
        const data = await readFile(DATA_FILE);

        const item = data.filter(item => item.id === id);

        if (item.length === 0){
            return res.status(404).send(`Item not found by ID number ${id}`)
        }

        res.status(200).json(item);
    } catch(e) {
        return res.status(400).send(e)
    }
})

// Add new task
app.post("/tasks", async (req, res) => {
    const {task, duration, completed} = req.body;

    try {
        const data = await readFile(DATA_FILE);

        if (!task || !duration || !completed){
            return res.status(400).send("Not enough information")
        }

        data.push({"id": data.length + 1, task, duration, completed});
        await writeFile(DATA_FILE, JSON.stringify(data));

        return res.status(200).json(data);
    } catch(e) {
        return res.status(400).send(e)
    }
})

// Edit task by ID
app.put("/tasks/:id", async (req, res) => {
    const id = parseInt(req.params.id);
    const {task, duration, completed} = req.body;

    try {
        const data = await readFile(DATA_FILE);

        if (!task || !duration || !completed) {
            return res.status(400).send("Not enough information")
        }
        
        const ind = data.findIndex(item => item.id === id);

        if (ind === -1) {
            return res.status(404).send(`Item not found by ID number ${id}`)
        }

        data[ind] = {id, task, duration, completed};
        await writeFile(DATA_FILE, JSON.stringify(data));

        return res.status(200).json(data)
    } catch(e) {
        res.status(400).send(e)
    }
})

// Delete task by ID
app.delete("/tasks/:id", async (req, res) => {
    const id = parseInt(req.params.id);

    try {
        let data = await readFile(DATA_FILE);
        
        const ind = data.findIndex(item => item.id == id);

        if (ind === -1) {
            return res.status(404).send(`Item not found by ID number ${id}`)
        }

        data = data.filter(item => item.id !== id);
        await writeFile(DATA_FILE, JSON.stringify(data));

        return res.status(200).json(data);
    } catch(e) {
        return res.status(400).send(e);
    }
})

// Start server
app.listen(PORT, () => console.log(`Server started on port ${PORT}`))