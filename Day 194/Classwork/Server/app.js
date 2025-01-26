import express from "express";
import bodyParser from "body-parser";
import AdminRoutes from "./Routes/account.route.js";
import cors from "cors";
import studentsRoutes from "./Routes/students.route.js";

const app = express();
app.use(bodyParser.json());
app.use(cors())

// Routes
app.use("/admin/", AdminRoutes)
app.use("/student", studentsRoutes)

app.listen(3000, () => {
    console.log("Server started on port 3000!");
})