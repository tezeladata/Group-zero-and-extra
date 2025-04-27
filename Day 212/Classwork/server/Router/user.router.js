const express = require('express');
const upload = require("../middlewares/multer.js")
const {userRegister} = require("../controllers/user.controllers");

const userRouter = express.Router();

userRouter.post("/register", upload.single("profile"), userRegister);

module.exports = {userRouter};