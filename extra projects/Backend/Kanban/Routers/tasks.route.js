// Modules
import express from "express";

// Utils
import readFile from "../Utils/readFile.js";
import writeFile from "../Utils/writeFile.js";

// db
import { TASKS_FILE } from "../app.js";

// Router
export const tasksRouter = express.Router();

// Routes
tasksRouter.get("/", async (req, res) => {
    try {
        const data = await readFile(TASKS_FILE);
        
        res.status(200).json(data)
    } catch(e) {
        return res.status(400).send("Error on request:", e)
    }
})

// id is task's heading property
tasksRouter.get("/:id", async (req, res) => {
    const heading = req.params.id;
    try {
        const data = await readFile(TASKS_FILE);

        // Item
        const item = data.filter(task => task.heading === heading);

        // Item does not exist
        if (item.length === 0) {
            return res.status(204).send("Task does not exist")
        }

        res.status(200).json(item)
    } catch(e) {
        return res.status(400).send("Error on request:", e)
    }
})

// Just to add task
tasksRouter.post("/", async (req, res) => {
    // board, column, heading, description and currentStatus are required for task to have. subtasks will first be set to 0 and []. They will be changed in future by client
    const { board, column, heading, description } = req.body;
    const currentStatus = req.body["current status"];

    try {
        const data = await readFile(TASKS_FILE);

        // Generate new task
        const newTask = {board, column, heading, description, "current status": currentStatus, "subtasks count": 0, "number of completed subtasks": 0, "subtasks": []};

        // Check if task already exists in database with same heading
        const checked = data.filter(task => task.heading === newTask.heading);
        if (checked.length !== 0) {
            return res.status(403).send("Task already exists with same heading")
        }
        
        // Add new task to array
        data.push(newTask);

        // save data to json file
        await writeFile(TASKS_FILE, data);

        res.status(200).send("New task added to database successfully");
    } catch(e) {
        return res.status(400).send(`Error on request: ${e}`)
    }
})

// task's put request
// heading, description, subtasks and status are necessary
// in subtasks array, for each subtask, only subtask name - "name" property is necessary. "task name" and "status" properties will be set by server automatically
tasksRouter.put("/:id", async (req, res) => {
    // id should be of previous name of task
    const heading = req.params.id;

    // new properties of existing task
    const newHeading = req.body.heading;
    const newDescription = req.body.description;
    const newSubtasks = req.body.subtasks;
    const currentStatus = req.body["current status"];

    try {
        const data = await readFile(TASKS_FILE);

        // Find task by previous heading
        const task = data.filter(task => task.heading === heading);
        
        // Task not found
        if (task.length === 0){
            return res.status(404).send("Task not found in database")
        }

        // Change task
        task[0].heading = newHeading;
        task[0].description = newDescription;
        let completedSubtaskCount = 0
        newSubtasks.map(item => { // Set "task name" and "status" properties automatically - it should not happen in client side, it is happening here in backend
            item["task name"] = newHeading;

            // if subtask with same name existed before put request, it's status should not be lost:
            const alreadyExists = task[0].subtasks.filter(taskItem => taskItem.name === item.name);
            if (alreadyExists.length > 0) {
                item["status"] = alreadyExists[0].status;

                // it subtask was completed previously, variable will be incremented for correct number of "number of completed subtasks" property
                if (alreadyExists[0].status === "Completed") completedSubtaskCount ++;
            } else {
                item["status"] = "Not completed";
            }
        });
        task[0].subtasks = newSubtasks;
        task[0]["subtasks count"] = newSubtasks.length; // This is automatically updated here, not in client side
        task[0]["number of completed subtasks"] = completedSubtaskCount; // This is also updated here, it is set to the value of completedSubtaskCount variable
        task[0]["current status"] = currentStatus;

        // Save changes to database
        await writeFile(TASKS_FILE, data);

        return res.status(200).send("Task successfully updated");
    } catch (e) {
        return res.status(400).send(`Error on request: ${e}`)
    }
})

// Task's delete request
// It is completed by ID
tasksRouter.delete("/:id", async (req, res) => {
    const heading = req.params.id;
    try {
        let data = await readFile(TASKS_FILE);

        // Find task by heading
        const task = data.filter(task => task.heading === heading);
        const ind = data.indexOf(task[0]);

        // Task not found
        if (task.length === 0) {
            return res.status(404).send("Task does not exist")
        }

        // Delete task from tasks
        data.splice(ind, 1);

        // Save changes to database
        await writeFile(TASKS_FILE, data);

        res.status(200).send("Task successfully deleted");
    } catch (e) {
        return res.status(400).send(`Error on request: ${e}`)
    }
})