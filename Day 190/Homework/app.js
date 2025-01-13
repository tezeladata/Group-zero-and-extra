const express = require('express');
const path = require('path');

const app = express();

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, './index.html'));
})

app.post('/products', (req, res) => {
    let body = "";

    req.on('data', (chunk) => {
        body += chunk;
    })

    req.on('end', () => {
        console.log(body);

        res.end(JSON.stringify(body));
    })
})

app.listen(3000, () => console.log('Server started on port 3000'));