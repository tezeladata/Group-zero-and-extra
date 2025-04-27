const express = require('express');
const cors = require('cors');
const {userRouter} = require("./Router/user.router.js");
const path = require("path");

const app = express();

app.use(cors());

app.use("/images". express.static("images"));

// Router
app.use("/user", userRouter)

// Pages
app.get("/:page", (req, res) => {
    switch (req.params.page) {
        case "register":
            return res.sendFile(path.join(__dirname, "/pages/register.html"));
            break;
        default:
            return res.sendFile()
    }
})

app.listen(3000, () => console.log('Listening on port 3000'));