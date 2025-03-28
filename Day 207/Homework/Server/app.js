import express from "express";
import cors from "cors";
import fs from "fs/promises";

// server
const PORT = 3000
const app = express();

// Middlewares
app.use(cors());
app.use(express.json());

// Readfile
const readfile = async (filepath) => {
    try {
        const data = await fs.readFile(filepath, "utf8");
        return JSON.parse(data)
    } catch (e) {
        return e
    }
}
// Writefile
const writefile = async (filepath, data) => {
    try {
        await fs.writeFile(filepath, JSON.stringify(data));
        return "Data written"
    } catch (e) {
        return e
    }
}

// Login
app.post("/user/login", async (req, res) => {
    const user = req.body;

    try {
        // All users
        const users = await readfile("./users.json");
        
        // Check user
        const exists = users.filter(item => item.email === user.email && item.password === user.password);
        if (exists.length > 0) {
            return res.status(200).json({"exists": true})
        } else {
            return res.status(404).json({"exists": false})
        }
    } catch (e) {
        return res.status(400).send(e)
    }
})

// Register
app.post("/user/register", async (req, res) => {
    const user = req.body;

    try {
        // Previous users
        const users = await readfile("./users.json");

        // Check if already exists
        const alreadyExists = users.filter(item => item.email === user.email)
        if (alreadyExists.length > 0) {
            return res.status(404).send("User already exists")
        }
        
        // Add new user to users
        users.push(user);

        // save changes
        await writefile("./users.json", users)
        
        return res.status(200).send("User added to users")
    } catch (e) {
        return res.status(400).send(e)
    }
})

// Start server
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));