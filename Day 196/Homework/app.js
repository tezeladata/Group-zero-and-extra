import express from 'express';
import cors from 'cors';
import bodyParser from 'body-parser';
import { promises as fs } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(express.json())

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.resolve(__dirname, './products.json');

const readDatabase = async () => {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        throw new Error('Failed to read or parse file');
    }
};

const writeDatabase = async (data) => {
    try {
        await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8');
    } catch (error) {
        console.error('Error writing to the database:', error);
        throw new Error('Unable to write to database');
    }
};

app.get('/products', async (req, res) => {
    try {
        const queries = req.query;
        let allProducts = await readDatabase();

        if ('sort' in queries) {
            const sortType = queries.sort.toLowerCase();
            if (sortType === 'ascending') {
                allProducts.sort((a, b) => a.price - b.price);
            } else if (sortType === 'descending') {
                allProducts.sort((a, b) => b.price - a.price);
            }
        }

        if ('minPrice' in queries) {
            const minPrice = parseFloat(queries.minPrice);
            if (!isNaN(minPrice)) {
                allProducts = allProducts.filter(product => product.price >= minPrice);
            }
        }

        if ('maxPrice' in queries) {
            const maxPrice = parseFloat(queries.maxPrice);
            if (!isNaN(maxPrice)) {
                allProducts = allProducts.filter(product => product.price <= maxPrice);
            }
        }

        if ('limit' in queries) {
            const limit = parseInt(queries.limit);
            if (!isNaN(limit) && limit > 0) {
                allProducts = allProducts.slice(0, limit);
            }
        }

        res.json(allProducts);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.get('/products/:id', async (req, res) => {
    try {
        const id = parseInt(req.params.id);
        const allProducts = await readDatabase();
        const item = allProducts.find(product => product.id === id);

        if (!item) {
            return res.status(404).json({ error: 'Invalid ID' });
        }

        res.json(item);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post("/products/add", async (req, res) => {
    try {
        const data = req.body;

        const allProducts = await readDatabase();
        const id = allProducts.length + 1;

        allProducts.push({id, "name": data.name, "price": data.price})
        writeDatabase(allProducts)

        res.json(JSON.stringify(allProducts));
    } catch (error) {
        res.status(500).json({ message: "An error occurred", error: error.message });
    }
});

app.put("/products/put", async (req, res) => {
    try {
        const { id, name, price } = req.body;

        if (!id) {return res.status(400).json({ message: "Product ID is required" })}

        let allProducts = await readDatabase();
        const productIndex = allProducts.findIndex(item => item.id === id);
        if (productIndex === -1) {return res.status(404).json({ message: "Product not found" })}

        allProducts[productIndex] = { ...allProducts[productIndex], name, price };

        writeDatabase(allProducts);
        res.json(allProducts)
    } catch (error){
        res.status(500).json({ message: "An error occurred", error: error.message });
    }
})

app.delete("/products/delete/:id", async (req, res) => {
    try {
        const { id } = req.params;
        const productId = Number(id);

        if (!productId) {return res.status(400).json({ message: "Product ID is required" })}

        let allProducts = await readDatabase();
        const productIndex = allProducts.findIndex(item => item.id === productId);

        if (productIndex === -1) {return res.status(404).json({ message: "Product not found" })}

        allProducts.splice(productIndex, 1);
        writeDatabase(allProducts);

        res.json(allProducts);
    } catch (error) {
        res.status(500).json({ message: "An error occurred", error: error.message });
    }
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));