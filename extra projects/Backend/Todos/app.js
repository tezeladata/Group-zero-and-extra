import express from "express";
import cors from "cors";
import logger from "./Middlewares/logger.js";
import { todo } from "./Routes/todo.route.js";
import { logs } from "./Routes/logs.route.js";

// Server
const app = express();
const PORT = 3000;

// Middlewares
app.use(cors());
app.use(express.json());
app.use(logger);
app.use("/todos", todo);
app.use("/logs", logs)

// Start server
app.listen(PORT, () => console.log(`Server started on port ${PORT}`))