import express from 'express';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const adminRoutes = express.Router();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

adminRoutes.post('/register', (req, res) => {
    const {email, pass} = req.body;

    const filePath = path.resolve(__dirname, '../database/admins.json');

    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            return res.status(500).json({error: 'Failed to read admins.json'});
        } else {
            const admins = JSON.parse(data);

            const adminExsists = admins.findIndex(admin => admin.email === email);

            if (adminExsists != -1) {
                return res.status(400).json({error: 'Email already exists'});
            }

            const newAdmin = {email, pass};
            admins.push(newAdmin);

            fs.writeFile(filePath, JSON.stringify(admins), err => {
                if (err) {
                    res.status(500).json({error: 'Failed to write admins.json'});
                } else {
                    res.status(201).json({message: 'Admin registered successfully'});
                }
            })
        }
    })
})

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