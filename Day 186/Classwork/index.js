const http = require("http");
const fs = require("fs");

const writeData = (data) => {
    fs.readFile('data.json', 'utf8', (err, fileData) => {
        if (err) throw err;

        const products = fileData ? JSON.parse(fileData) : [];
        products.push(JSON.parse(data));

        fs.writeFile('data.json', JSON.stringify(products), (err) => {
            if (err) throw err;
            console.log("Data saved")
        });
    });
};

const server = http.createServer((req, res) => {
    if (req.url === "/products" && req.method === "POST") {
        let body = '';

        req.on('data', (chunk) => {
            body += chunk.toString();
        });

        req.on('end', () => {
            writeData(body);
            console.log("New added: ", body);
            res.end("Information received");
        });

    } else if (req.url === "/products" && req.method === "GET") {
        fs.readFile('data.json', 'utf8', (err, fileData) => {
            if (err) throw err;
            console.log(JSON.parse(fileData));
            res.end(JSON.stringify(fileData));
        })
    }

    else {
        res.statusCode = 404;
        res.end("Not Found");
    }
});

server.listen(3000, () => {
    console.log("Server started on port 3000");
});