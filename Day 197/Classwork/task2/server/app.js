import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';

const app = express();
app.use(cors());
app.use(bodyParser.json());

let accounts = [
    {
        name: "David Tezelashvili",
        email: "David Tezelashvili@gmail.com",
        password: "12345678"
    },
    {
        name: "Andria Tezelashvili",
        email: "Andria Tezelashvili@gmail.com",
        password: "12345678"
    },
]

app.post("/register", (req, res) => {
    const { email } = req.body;

    const existingAccount = accounts.find((account) => account.email === email);
    if (existingAccount) {
        return res.status(400).json({ error: 'Email already exists' });
    }

    accounts.push(req.body);
    res.json(accounts);
});

app.listen(3000, () => console.log("Server started on port 3000"));