import express from "express";
import cors from "cors";
import { userRoute } from "./Routes/userRoute.routes.js";
import { userTask } from "./Routes/userTask.routes.js";

const app = express();

// middleware
app.use(cors());
app.use(express.json())

// Routes
app.use("/users", userRoute);
app.use("/tasks", userTask);


app.listen(3000, () => console.log("Server started on port 3000"))