const http = require("http");

const products = [
  {name: "apple", price: 1.99},
  {name: "banana", price: 2.99},
  {name: "mango", price: 2.49},
  {name: "strawberry", price: 4.99},
  {name: "kiwi", price: 7.99}
]

const server = http.createServer((req, res) => {
    if (req.url === "/products" && req.method === "GET") {
        res.statscode = 200;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify(products));
    }
})

server.listen(5000, () => {
    console.log("Server started on http://localhost:5000");
});