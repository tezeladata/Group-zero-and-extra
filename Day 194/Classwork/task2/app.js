import express from 'express';

const app = express();

app.get("/:id", (req, res) => {
    res.send(`Hello, ${req.params.id}`);
})

app.listen(3000, () => {
    console.log("Server started on https://localhost:3000");
});