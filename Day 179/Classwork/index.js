const http = require("http");

const server1 = http.createServer((req, res) => {
    // res - response, req - request
    res.end("Hello from server");
});

server1.listen(5500, () => {
    const {address, port} = server1.address();
    console.log(address, port)
})