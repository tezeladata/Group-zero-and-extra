// Modules
import express from "express";

// Utils
import readFile from "../Utils/readFile.js";
import writeFile from "../Utils/writeFile.js";

// db
import { TASKS_FILE } from "../app.js";

// Router
export const boardsRouter = express.Router();

// Routes

// Get board names
boardsRouter.get("/", async (req, res) => {
    try {
        const data = await readFile(TASKS_FILE);
        
        // Find all board names
        const boards = [];
        data.map(item => {if (!boards.includes(item.board)) {boards.push(item.board)}});
        
        // If database does not have any boards
        if (boards.length === 0){
            return res.status(400).send("Database does not have any boards")
        }

        return res.status(200).json(boards);
    } catch(e) {
        return res.status(400).send("Failed to read database")
    }
})

// Get single board with it's columns and their tasks by ID
boardsRouter.get("/:id", async (req, res) => {
    const board = req.params.id;
    
    try {
        const data = await readFile(TASKS_FILE);
        
        // Find board and it's tasks
        const result = data.filter(item => item["board"] === board);
        
        // If board does not exist
        if (result.length === 0){
            return res.status(400).send("Given board does not exist")
        }

        return res.status(200).json(result)
    } catch(e) {
        return res.status(400).send("Failed to read database")
    }
})

// Delete board with it's ID
boardsRouter.delete("/:id", async (req, res) => {
    const board = req.params.id;

    try {
        let data = await readFile(TASKS_FILE);
        const startLen = data.length;
        
        // Filter tasks - no task should have board property set to given ID
        data = data.filter(item => item["board"] !== board);
        const endLen = data.length;

        // Board does not exist
        if (startLen === endLen) {
            return res.status(400).send("Given board does not exist")
        }

        // Save changes to database
        await writeFile(TASKS_FILE, data);

        return res.status(200).send("Board deleted with it's tasks successfully")
    } catch(e) {
        return res.status(400).send("Failed to read database")
    }
})