const http = require("http");

let all = [
  {"title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", "price": 109.95, "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday", "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"},
  {"title": "Mens Casual Premium Slim Fit T-Shirts ", "price": 22.3, "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.", "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg"},
  {"title": "Mens Cotton Jacket", "price": 55.99, "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.", "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg"},
    {"title": "Mens Casual Slim Fit", "price": 15.99, "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.", "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_.jpg"}
]
let newArr = [];


const server = http.createServer((req, res) => {
  if (req.url === "/" || req.url === "/index.html") {
    res.writeHead(200, { "Content-Type": "text/html" });
    res.write(`
      <!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Simple Website</title>
        </head>
        <body>
          <h1>Welcome to our website</h1>
          <ul>
            ${all.map(product => `
              <li>
                <h2>${product.title}</h2>
                <p>Price: $${product.price}</p>
                <p>${product.description}</p>
                <img src="${product.image}" alt="${product.title}" style="width:150px;height:auto;">
              </li>
            `).join('')}
          </ul>
        </body>
      </html>
    `);
    res.end();
  } else if (req.url === "/users" && req.method === "GET") {
    res.end(JSON.stringify([
        {name: "David", surname: "Tezelashvili"},
        {name: "Andria", surname: "Tezelashvili"},
        {name: "test", surname: "Testadze"},
        {name: "Chad", surname: "Chadadze"},
    ]))
  } else if (req.url === "/users" && req.method === "POST") {
    let body = '';

    req.on('data', chunk => {
      body += chunk.toString();
    });

    req.on('end', () => {
      const parsedBody = JSON.parse(body);
      newArr.push(parsedBody);
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(newArr));
  });
}
});

server.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});