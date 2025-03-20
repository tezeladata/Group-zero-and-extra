import express from 'express';
import readFile from "../utils/readFile.js";
import writeFile from "../utils/writeFile.js";

// Router
export const users = express.Router();

// Routes
users.get("/:id", async (req, res) => {
    const id = req.params.id;
    try {
        const data = await readFile("./database.json");

        // find user by ID
        let user = data.filter(item => item.userID === id);

        // If user not found
        if (user.length === 0) {
            return res.status(404).send("User not found");
        } else {
            // When filtering, result is array, and we want to store object in user variable
            user = user[0];
        }

        res.status(200).json(user);
    } catch (error) {
        return res.status(400).send("Failed to read database")
    }
})