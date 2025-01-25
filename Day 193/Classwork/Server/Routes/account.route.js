import express from 'express';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const adminRoutes = express.Router();

const filename = fileURLToPath(import.meta.url);
const dirname = path.dirname(filename);

adminRoutes.post('/login', (req, res) => {
    const { email, pass } = req.body;

    const filePath = path.resolve(dirname, '../database/admins.json'); // Replace __dirname with dirname

    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            return res.status(500).json({ error: 'Failed to read admins.json' });
        } else {
            const admins = JSON.parse(data);

            const adminIndex = admins.findIndex(admin => admin.email === email && admin.pass === pass);

            if (adminIndex === -1) {
                return res.status(401).json({ error: 'Invalid credentials or admin does not exist' });
            }

            res.json(admins[adminIndex]);
        }
    });
});

adminRoutes.post('/login', (req, res) => {
    const {email, pass} = req.body;

    const filePath = path.resolve(__dirname, '../database/admins.json');

    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            return res.status(500).json({error: 'Failed to read admins.json'});
        } else {
            const admins = JSON.parse(data);

            const adminIndex = admins.findIndex(admin => admin.email === email && admin.pass === pass);

            if (adminIndex === -1) {
                return res.status(401).json({error: 'Invalid credentials or admin dont exsist'});
            }

            res.json(admins[adminIndex]);
        }
    })
})




export default adminRoutes;