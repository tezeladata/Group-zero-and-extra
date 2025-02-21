import express from "express";

export const userTask = express.Router();

const tasks = [
    {id: 1, name: "Mentors exam"},
    {id: 2, name: "Group 54 lesson"},
    {id: 3, name: "Group 29 lesson"},
    {id: 4, name: "Mentor Control"},
    {id: 5, name: "Algo&AI video"},
    {id: 6, name: "Algo&AI homework"},
    {id: 7, name: "Workout"},
    {id: 8, name: "Read book"},
]

userTask.get("/", (req, res) => {
    res.json(tasks)
})

userTask.post("/", (req, res) => {
    const {name} = req.body;

    tasks.push({id: tasks.length + 1, name});

    res.json(tasks)
})