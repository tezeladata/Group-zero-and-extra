// Modules
import express from "express";

// Utils
import readFile from "../Utils/readFile.js";
import writeFile from "../Utils/writeFile.js";

// db
import { TASKS_FILE } from "../app.js";

// Router
export const subtasksRouter = express.Router();

// Routes

// Get subtask by parents heading followed by it's name
// Parents heading is necessary, because there could be subtasks with same names in different tasks
subtasksRouter.get("/:taskID/:subtaskID", async (req, res) => {
    const { taskID, subtaskID } = req.params;

    try {
        const data = await readFile(TASKS_FILE);

        // find given task
        const task = data.filter(item => item.heading == taskID);
        
        // If task is not found
        if (task.length === 0) {
            return res.status(404).send("Given task was not found in database")
        };

        const subtask = task[0].subtasks.filter(item => item.name === subtaskID);
        
        // If subtask is not found
        if (subtask.length === 0) {
            return res.status(404).send("Given task does not have that subtask");
        };

        // Return subtask
        return res.status(200).json(subtask[0])
    } catch(e) {
        return res.status(400).send("Error on request:", e)
    }
})

// Post request is not necessary, because it automatically happens when task is created (POST) or edited (PUT)

// Get subtask by parents heading followed by it's name
// Parents heading is necessary, because there could be subtasks with same names in different tasks
// Change subtasks status by post method
subtasksRouter.put("/:taskID/:subtaskID", async (req, res) => {
    const { taskID, subtaskID } = req.params;
    let { status } = req.body;

    // Make sure case problem does not exist
    if (status === "completed"){
        status = "Completed"
    } else if (status === "not completed"){
        status = "Not completed"
    }

    try {
        const data = await readFile(TASKS_FILE);
        
        // Find given task and it's index in database
        const task = data.filter(item => item.heading === taskID);
        const ind = data.findIndex(item => item.heading === task[0].heading);
        
        // If task is not found
        if (task.length === 0){
            return res.status(404).send("Given task does not exist");
        }

        // Find given task
        const subtask = task[0].subtasks.filter(item => item.name == subtaskID);
        
        // If subtask is not found
        if (subtask.length === 0){
            return res.status(404).send("Given task does not have that subtask")
        }

        // Change subtask
        subtask[0]["status"] = status

        // find number of completed subtasks
        const numOfComp = task[0].subtasks.filter(item => item.status === "Completed").length;

        // Save number of completed subtasks to database
        data[ind]["number of completed subtasks"] = numOfComp;

        // Save changes to database
        await writeFile(TASKS_FILE, data);

        return res.status(200).send("Subtask changed successfully");
    } catch(e) {
        return res.status(400).send("Error on request:", e)
    }
})

// Delete request is not necessary, because it automatically happens when task is edited (PUT)