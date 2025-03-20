import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import readFile from "./utils/readFile.js";
import writeFile from "./utils/writeFile.js";
import {users} from "./Routers/users.route.js";

// Server and port
const app = express();

dotenv.config();
const PORT = process.env.PORT;

// Middlewares
app.use(cors());
app.use(express.json());
// To log every request
app.use(async (req,res,next) => {
    try {
        // Current request's info
        const data = [req.url, req.method, req.params, req.query];

        // All the previous logs
        const allLogs = await readFile("./logs.json");

        // Add current info to all logs
        allLogs.push(data);

        // Save changes
        await writeFile("./logs.json", allLogs);
        next()
    } catch (error) {
        res.status(400).send("Could not receive request")
    }
})

// Routes
app.use("/users", users)


// Start server
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));