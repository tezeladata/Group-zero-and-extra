import mongoose from "mongoose";

const postSchema = new mongoose.Schema(
    {
        title: String,
        content: String,
        likesCount: Number
    }
);

export const Post = mongoose.model("Posts", postSchema)