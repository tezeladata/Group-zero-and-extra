import express from 'express';
import readFile from "../Utils/readFile.js";

export const productsRoute = express.Router();

productsRoute.get('/', async (req, res) => {
    const {limit, sort} = req.query;

    try {
        let products = await readFile("C:\\Users\\PC\\OneDrive\\Desktop\\web development course\\Day 198\\Classwork\\database.json");

        if (limit) {
            products = products.slice(0, parseInt(limit));
        }

        if (sort) {
            products.sort((a, b) => {
                if (sort === "asc") {
                    return a.price - b.price;
                } else {
                    return b.price - a.price;
                }
            })
        }

        res.json(products);
    } catch (error) {
        res.status(500).json({error: error})
    }
})

productsRoute.get('/:id', async (req, res) => {
    const {id} = req.params;

    try {
        const products = await readFile("C:\\Users\\PC\\OneDrive\\Desktop\\web development course\\Day 198\\Classwork\\database.json");
        const product = products.find(product => product.id === parseInt(id));

        if (!product) {
            res.status(404).json({error: 'Product not found'});
        } else {
            res.json(product);
        }
    } catch (error) {
        res.status(500).json({error: error})
    }
})

productsRoute.get("/category/:category", async (req, res) => {

    const { category } = req.params;

    try {
        const products = await readFile("C:\\Users\\PC\\OneDrive\\Desktop\\web development course\\Day 198\\Classwork\\database.json");
        const filteredProducts = products.filter((product) => product.category === category);

        console.log("Filtered products: ", filteredProducts);

        if(filteredProducts.length === 0) {
            return res.status(404).json({ error: "No products found in this category" });
        }

        return res.status(200).json(filteredProducts);
    } catch (error) {
        return res.status(500).json({ error: "Failed to read products.json" });
    }
})

productsRoute.get("/category", (req, res) => {
    res.json(["Accessories", "Laptops", "Displays", "Storage", "Audio", "Cameras", "Furniture", "Smart Home", "Drawing Tablets", "Networking"])
});