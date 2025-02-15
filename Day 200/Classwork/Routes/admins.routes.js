import express from 'express';

export const adminsRouter = express.Router();

const admins = [
    {id: 1, name: "David", academy: "GOA"},
    {id: 2, name: "David2", academy: "GOA"},
    {id: 3, name: "David3", academy: "GOA"},
    {id: 4, name: "David4", academy: "GOA"},
    {id: 5, name: "David5", academy: "GOA"}
]

adminsRouter.get('/', (req, res) => {
    res.status(200).json(admins);
})

adminsRouter.get('/:id', (req, res) => {
    const id = req.params.id;

    const admin = admins[id];

    if (!admin) {
        res.status(404).json("admin not found");
    }

    res.status(200).json(admin);
})