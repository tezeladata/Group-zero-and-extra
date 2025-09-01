import express from "express";
import morgan from "morgan";
import dotenv from "dotenv";
import mongoose from "mongoose";
import { postsRouter } from "./routers/posts.route.js";

dotenv.config()

const app = express();

if (process.env.NODE_ENV === "development"){
    app.use(morgan("dev"))
}

app.use(express.json());
app.use("/posts", postsRouter);

mongoose.connect(process.env.DATABASE_URL)
    .then(() => {
        console.log("Connected to db");
        app.listen(process.env.PORT, () => console.log(`Server started on port ${process.env.PORT}`))
    })
    .catch(err => {
        console.log("db connection error")
        process.exit(1)
    })