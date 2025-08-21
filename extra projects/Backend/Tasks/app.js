// Modules
import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import {tasksRouter} from "./Routers/tasks.route.js";
import Logger from "./Middlewares/logger.js";

// App, port and db
const app = express();
const PORT = 3000;
export const TASKS_FILE = "./Dbs/tasks.json";

// Middlewares
app.use(cors());
app.use(bodyParser.json());
app.use(Logger)

// Routers
app.use("/tasks", tasksRouter)

// Start server
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));