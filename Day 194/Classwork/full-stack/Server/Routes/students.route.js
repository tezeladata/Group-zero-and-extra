import express from "express";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const studentsRoutes = express.Router();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Path to the students database
const filePath = path.resolve(__dirname, "../database/student.json");

// Ensure the file exists
if (!fs.existsSync(filePath)) {
    fs.writeFileSync(filePath, "[]", "utf8");
}

// Get all students
studentsRoutes.get("/", (req, res) => {
    fs.readFile(filePath, "utf8", (err, data) => {
        if (err) {
            return res.status(500).json({ err: "Failed to read students." });
        }
        try {
            const students = JSON.parse(data);
            res.status(200).json(students);
        } catch (parseError) {
            res.status(500).json({ err: "Invalid students data format." });
        }
    });
});

// Add a new student
studentsRoutes.post("/", (req, res) => {
    const { fullname, age, email } = req.body;

    fs.readFile(filePath, "utf8", (err, data) => {
        if (err) {
            return res.status(500).json({ err: "Failed to read students." });
        }
        try {
            const students = JSON.parse(data);
            const student = { fullname, age, email, id: students.length + 1 };
            students.push(student);

            fs.writeFile(filePath, JSON.stringify(students, null, 2), "utf8", (writeErr) => {
                if (writeErr) {
                    return res.status(500).json({ err: "Failed to save students." });
                }
                res.status(201).json({ student });
            });
        } catch (parseError) {
            res.status(500).json({ err: "Invalid students data format." });
        }
    });
});

export default studentsRoutes;