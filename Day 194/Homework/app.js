import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import fs from "fs/promises";

const app = express();

app.use(bodyParser.json());
app.use(cors());

const readJson = async (fileName) => {
    try {
        const data = await fs.readFile(fileName, "utf-8");
        return JSON.parse(data);
    } catch (error) {
        console.error("Error reading JSON file:", error);
        return [];
    }
};

const writeJson = async (fileName, data) => {
    try {
        await fs.writeFile(fileName, JSON.stringify(data, null, 2), "utf-8");
    } catch (error) {
        console.error("Error writing JSON file:", error);
    }
};

app.post("/items/add", async (req, res) => {
    const newFruit = req.body;

    if (!newFruit.id || !newFruit.name) {
        return res.status(400).json({ message: "Invalid fruit data. ID and name are required." });
    }

    const fruits = await readJson("fruits.json");

    if (fruits.some(fruit => fruit.id == newFruit.id)) {
        return res.status(400).json({ message: "Fruit with this ID already exists." });
    }

    fruits.push(newFruit);
    await writeJson("fruits.json", fruits);

    res.status(201).json({ message: "Fruit added successfully", fruit: newFruit });
});

app.listen(5050, () => {
    console.log("Server started on port 5050");
});