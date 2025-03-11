import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import dotenv from "dotenv";

// Server
const app = express();

// Port
dotenv.config();
const PORT = process.env.PORT

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use((req, res, next) => {
    console.log(`Request url is ${req.url}, request method is ${req.method}`);
    next();
});
app.use((req, res, next) => {
    console.log(`All headers are: ${req.rawHeaders}`);
    next();
})
app.use((req, res, next) => {
    console.log(req.errored === null ? "Error not occured": `Error occured ${req.errored}`);
    next();
})

// Db
let products = [
    {id: 1, name: "Apple", price: 1.5},
    {id: 2, name: "Mango", price: 2.5},
    {id: 3, name: "Banana", price: 2},
    {id: 4, name: "Kiwi", price: 4}
]

// Routes
app.get("/", (req, res) => {
    res.json([
        {name: "David", surname: "Tezelashvili"},
        {name: "Andria", surname: "Tezelashvili"},
        {name: "Luka", surname: "Tskhvaradze"},
        {name: "Vano", surname: "Motiashvili"}
    ])
})

app.get("/products", (req, res) => {
    res.status(200).json(products)
})

app.post("/products", (req, res) => {
    const {name, price} = req.body;

    if (!name || !price) {
        return res.status(404).send("Not enough info")
    }

    const newProduct = {id: products.length + 1, name, price};

    products.push(newProduct);

    console.log(products)
    res.status(200).json(products)
})

app.put("/products", (req, res) => {
    const {id, name, price} = req.body;
    const productId = products.findIndex(item => item.id === id && item.name === name);

    if (!id || !name || !price) {
        return res.status(400).send("Not enough info")
    }

    products[productId] = {id, name, price};

    if (productId === -1) {
        return res.status(404).send("Product not found");
    }

    console.log(products);
    res.status(200).json(products);
})

app.delete("/products/:id", (req, res) => {
    const id = parseInt(req.params.id);

    if (isNaN(id) || id < 1 || id > products.length) {
        return res.status(400).send("Wrong id")
    }

    products = products.filter(item => item.id !== id);

    console.log(products);
    res.status(200).json(products);
})

// Run server
app.listen(PORT, () => console.log(`Server is runnin on port ${PORT}`))