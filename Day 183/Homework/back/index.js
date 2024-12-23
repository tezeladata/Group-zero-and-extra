const http = require("http");

const products = [
    { name: "apple", price: 1.99 },
    { name: "banana", price: 2.99 },
    { name: "mango", price: 2.49 },
    { name: "strawberry", price: 4.99 },
    { name: "kiwi", price: 7.99 },
];

const server = http.createServer((req, res) => {
    if (req.url === "/products" && req.method === "GET") {
        res.writeHead(200, {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        });
        res.end(JSON.stringify(products));
    } else {
        res.writeHead(404, { "Content-Type": "text/plain" });
        res.end("Route not found");
    }
});

server.listen(3000, () => {
    console.log("Server started on http://localhost:3000");
});