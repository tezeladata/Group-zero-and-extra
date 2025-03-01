import express from 'express';
import cors from 'cors';

const app = express();

// middlewares
app.use(cors());
app.use(express.json());
app.use(["/users", "/products"], (req, res, next) => {
    console.log("Middleware is working on /users or /products route");
    next();
})

// Routes
app.get('/users', (req, res) => {
    res.send("Get request on users")
})
app.post('/users', (req, res) => {
    res.send("Post request on users")
})
app.delete('/users', (req, res) => {
    res.send("Delete request on users")
})

app.listen(3000, () => console.log("Server is running on port 3000"));