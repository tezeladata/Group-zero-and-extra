import express from "express";
import { Post } from "../models/post.model.js";

export const postsRouter = express.Router();

// Add post
postsRouter.post("/", async (req, res) => {
    const {title, content} = req.body;

    const newPost = await Post.create({
        title,
        content,
        likesCount: 0
    });

    res.status(201).json(newPost)
})