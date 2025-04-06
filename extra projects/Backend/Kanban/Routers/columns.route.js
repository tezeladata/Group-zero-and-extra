// Modules
import express from "express";

// Utils
import readFile from "../Utils/readFile.js";
import writeFile from "../Utils/writeFile.js";

// db
import { TASKS_FILE } from "../app.js";

// Router
export const columnsRouter = express.Router();

// Routes

// Get all column names
columnsRouter.get("/", async (req, res) => {
    try {
        const data = await readFile(TASKS_FILE);

        // Get columns
        const columns = [];
        data.map(item => {if (!columns.includes(item.column)) {columns.push(item.column)}});
        console.log(columns);

        // If columns do not exist
        if (columns.length === 0){
            return res.status(400).send("Database does not have any column")
        }

        return res.status(200).json(columns);
    } catch(e) {
        return res.status(400).send("Failed to read database")
    }
})

// Get specific column by ID
columnsRouter.get("/:id", async (req, res) => {
    const column = req.params.id;
    
    try {
        const data = await readFile(TASKS_FILE);
        
        // Find tasks, which belong to stated column
        const result = data.filter(item => item["column"] === column);

        // If stated column does not have any tasks;
        if (result.length === 0){
            return res.status(404).send("Column does not have any tasks")
        }

        res.status(200).json(result)
    } catch(e) {
        return res.status(400).send("Failed to read database")
    }
})

// Delete column by ID
// Tasks, which are in that column, will be deleted
columnsRouter.delete("/:id", async (req, res) => {
    const column = req.params.id;
    
    try {
        let data = await readFile(TASKS_FILE);
        const startLen = data.length;
        
        // Filter data
        data = data.filter(item => item["column"] !== column);
        const afterLen = data.length;
        
        // If database's length does not change - that column does not exist
        if (startLen === afterLen){
            return res.status(400).send("That column does not exist")
        }

        // Save changes to database
        await writeFile(TASKS_FILE, data);
        
        res.status(200).send("Column deleted with it's tasks successfully")
    } catch(e) {
        return res.status(400).send("Failed to read database")
    }
})