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
    console.log(products);
    res.end(JSON.stringify(products));

  } else if (req.url === "/products" && req.method === "POST") {
    let body = '';

    req.on('data', chunk => {
      body += chunk.toString();
    });

    req.on('end', () => {
      const newProduct = JSON.parse(body);
      products.push(newProduct);

      console.log(products);
      res.end(JSON.stringify(products));
    })
  } else if (req.url === "/products" && req.method === "DELETE") {
    products.pop();
    console.log(products);
    res.end(JSON.stringify(products));
  }
});

server.listen(3000, () => {
    console.log("Server started on http://localhost:3000");
});