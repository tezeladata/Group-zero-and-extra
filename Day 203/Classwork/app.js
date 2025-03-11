import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';

const app = express();

app.use(cors());
app.use(bodyParser.json());

// app.use((req,res,next)=>{
//     console.log(req.method, req.url);
//     next();
// });
// app.use((req,res,next)=>{
//     console.log(req.rawHeaders);
//     next();
// });
// app.use((req,res,next)=>{
//     console.log(req.errored !== null ? "Error occurred" : "Error not occurred");
//     next();
// })

// const me = {
//     name: "John",
//     email: "john@example.com",
//     age: 30,
//     password: "123456",
//     city: "New York"
// }
//
// app.use("/user", (req,res,next) => {
//     const { email, password } = req.body;
//     if (email === me.email && password === me.password) {
//         next();
//     } else {
//         res.status(401).send("Invalid credentials");
//     }
// });
// app.use((req, res, next) => {
//     res.status(200).json(me);
// })

const credentials = {
    email: "datatezelashvili8@gmail.com",
    password: "123456",
}

const products = [
    {name: "Apple", price: 1.5},
    {name: "Alice", price: 2.5},
    {name: "Berlin", price: 1.5},
    {name: "Crimson", price: 2.5}
]

const authenticate = (req, res, next) => {
    const { email, password } = req.body;

    if (email === credentials.email && password === credentials.password) {
        next();
    } else {
        return res.status(401).send("Wrong email or password");
    }
}

const getData = (req, res, next) => {
    return res.status(200).json(products);
}

app.post("/products", authenticate, getData)


app.listen(3000, () => console.log('Server started on port 3000'));