import express from "express";
import readFile from "../Utils/readFile.js";

// Route
export const logs = express.Router();

// database
const filepath = "./Database/logs.json";

logs.get("/", async (req, res) => {
    try {
        const data = await readFile(filepath);
        return res.status(200).json(data);
    } catch(e) {
        return res.status(404).send(e)
    }
})