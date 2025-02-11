import express from 'express';
import readFile from "../utils/readFile.js";
import writeFile from "../utils/writeFile.js"

export const productsRoute = express.Router();

const allCategories = ["Accessories", "Laptops", "Displays", "Storage", "Audio", "Cameras", "Furniture", "Smart Home", "Drawing Tablets", "Networking"]

productsRoute.get('/', async (req, res) => {
    const {limit, sort, filt, remaining } = req.query;

    try {
        let products = await readFile("./database.json");

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

        if (filt) {
            if (filt === "expensive"){
                products = products.filter(item => item.price >= 50);
            } else if (filt === "cheap") {
                products = products.filter(item => item.price < 50);
            }
            console.log(products)
        }

        if (remaining) {
            if (remaining === "many"){
                products = products.filter(item => item.stock >= 50);
            } else if (remaining === "little"){
                products = products.filter(item => item.stock < 50);
            }
        }

        res.json(products);
    } catch (error) {
        res.status(500).json({error: error})
    }
})

productsRoute.get('/category', (req, res) => {
    res.json(allCategories)
});

productsRoute.get("/category/:category", async (req, res) => {

    const { category } = req.params;

    try {
        const products = await readFile("./database.json");
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

productsRoute.get('/item/:id', async (req, res) => {
    const {id} = req.params;

    try {
        const products = await readFile("./database.json");
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

productsRoute.post('/add', async (req, res) => {
    try {
        let products = await readFile("./database.json");
        const {name, price, category} = req.body;

        if (!name || !category || !price){
            res.status(200).send("Invalid information given")
        };

        if (allCategories.includes(category) === false) {
            res.status(404).send("Incorrect category")
        }

        if (products.some(item => item.name === name)) {
            return res.status(404).send("Item already in database");
        }        

        const newItem = {id: products.length + 1, name, price, category, stock: 1};
        products.push(newItem);

        await writeFile("./database.json", products);
        res.json(products);
    } catch(e) {
        console.error(e)
    }
})

productsRoute.put("/edit/:id", async (req, res) => {
    try {
        let products = await readFile("./database.json");
        const { name, price, category, stock } = req.body;
        const { id } = req.params;
        const productIndex = products.findIndex((product) => product.id === parseInt(id));

        if (productIndex === -1) {
            return res.status(404).send("Product not found");
        }

        if (!name || !category || !price) {
            return res.status(400).send("Not enough information provided");
        }

        if (!allCategories.includes(category)) {
            return res.status(400).send("Invalid category");
        }

        products[productIndex] = { ...products[productIndex], name, price, category, stock: stock ?? products[productIndex].stock };

        await writeFile("./database.json", products);
        res.json(products[productIndex]);
    } catch (e) {
        console.error(e);
        res.status(500).json({ error: "Failed to update product" });
    }
});

productsRoute.delete("/delete/:id", async (req, res) => {
    try {
        let products = await readFile("./database.json");
        const { id } = req.params;

        const productIndex = products.findIndex((product) => product.id === parseInt(id));

        if (productIndex === -1) {
            return res.status(404).send("Product not found");
        }

        products.splice(productIndex, 1);

        await writeFile("./database.json", products);
        res.status(200).send("Product deleted successfully");
    } catch (e) {
        console.error(e);
        res.status(500).json({ error: "Failed to delete product" });
    }
});