const express = require('express');
const cors = require("cors");
const fs = require("fs").promises; // Using promises for async file operations

const app = express();

app.use(express.json());
app.use(cors());

// Register route
app.post('/admin/register', async (req, res) => {
    const { fullName, email, password } = req.body;

    try {
        const data = await fs.readFile('./admins.json', 'utf8');
        const admins = JSON.parse(data);

        // Check if email already exists
        if (admins.some(admin => admin.email === email)) {
            return res.status(400).send("Email already exists!");
        }

        // Add new admin to the list
        admins.push({ fullName, email, password });

        // Save updated admins list
        await fs.writeFile('./admins.json', JSON.stringify(admins, null, 2));
        res.status(200).send("Admin registered");
    } catch (err) {
        console.error('Error handling register:', err);
        res.status(500).send("Server error");
    }
});

// Login route
app.post('/admin/login', async (req, res) => {
    const { email, password } = req.body;

    try {
        const data = await fs.readFile('./admins.json', 'utf8');
        const admins = JSON.parse(data);

        // Find admin by matching email and password
        const admin = admins.find(a => a.email === email && a.password === password);

        if (!admin) {
            console.log('Login failed: incorrect credentials');
            return res.status(404).send('Credentials are not correct!');
        }

        console.log('Login successful:', admin);
        res.status(200).send(admin);
    } catch (err) {
        console.error('Server error:', err);
        res.status(500).send('Server error');
    }
});

// Start the server
app.listen(3000, () => console.log('Listening on port 3000'));