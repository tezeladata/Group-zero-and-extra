const http = require("http");

const server = http.createServer((req, res) => {
    console.log(req.method, req.path);

    if (req.url === "/" || req.url === "/index.html") {
        res.end("Hello on website");
    } else if (req.url === "/users") {
        res.end(JSON.stringify([
            {name: "David", surname: "Tezelashvili"},
            {name: "Andria", surname: "Tezelashvili"},
            {name: "test", surname: "Testadze"},
            {name: "Chad", surname: "Chadadze"},
        ]));
    } else if (req.url === "/products") {
        res.end(JSON.stringify(["Apple", "Banana", "Kiwi"]));
    } else {
        res.end("Not Found");
    }
});

server.listen(5500, () => {
    console.log(server.address().port);
});