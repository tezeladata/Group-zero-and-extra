const express = require('express');
const path = require('path');

const app = express();


// const accounts = [];
// const products = []
// app.get("/accounts", (req, res) => {
//     res.send(JSON.stringify(accounts))
// });
//
// app.get("/products", (req, res) => {
//     res.send(JSON.stringify(products))
// });
//
// app.post("/accounts", (req, res) => {
//     let body = "";
//
//     req.on("data", (chunk) => {
//         body += chunk;
//     })
//
//     req.on("end", (chunk) => {
//         accounts.push(body);
//
//         console.log(accounts);
//         res.send("Account added successfully.");
//     })
// })
//
// app.post("/products", (req, res) => {
//     let body = "";
//
//     req.on("data", (chunk) => {
//         body += chunk;
//     })
//
//     req.on("end", (chunk) => {
//         products.push(body);
//
//         console.log(products);
//         res.send("Product added successfully.");
//     })
// })

const idArr = [
    {name: "0", letter: "a"}, {name: "1", letter: "b"}, {name: "2", letter: "c"}, {name: "3", letter: "d"}, {name: "4", letter: "f"},
    {name: "5", letter: "g"}, {name: "6", letter: "h"}, {name: "7", letter: "i"}, {name: 8, letter: "j"}, {name: "9", letter: "k"}
]
app.get('/products/:id', (req, res) => {
    const productId = req.params.id;

    const newItem = idArr[productId];

    console.log(newItem);
    res.send(JSON.stringify(newItem));
})

app.listen(3000, () => { console.log("Server is running on port 3000") });