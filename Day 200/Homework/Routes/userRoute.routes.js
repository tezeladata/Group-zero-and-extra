import express from "express";

export const userRoute = express.Router();

const users = [
    {id: 1, name: "David Tezelashvili", academy: "GOA"},
    {id: 2, name: "Luka Tskhvaradze", academy: "GOA"},
    {id: 3, name: "Vano Motiashvili", academy: "GOA"},
    {id: 4, name: "Gabriel Molodini", academy: "GOA"},
    {id: 5, name: "Data Diasamidze", academy: "GOA"},
]

userRoute.get("/", (req, res) => {
    res.json(users)
})

userRoute.post("/", (req, res) => {
    const {name, academy} = req.body;

    users.push({id: users.length + 1, name, academy});

    res.json(users)
})