import express from 'express';

export const productsRouter = express.Router();

const products = [
    {id: 1, name: "Product 1", price: 1},
    {id: 2, name: "Product 2", price: 2},
    {id: 3, name: "Product 3", price: 3}
]

productsRouter.get('/', (req, res) => {
    res.status(200).json(products);
})

productsRouter.get('/:id', (req, res) => {
    const id = req.params.id;

    const product = products.find(product => product.id === parseInt(id));

    if (!product) {
        res.status(404).json("Product not found");
    }

    res.status(200).json(product);
})