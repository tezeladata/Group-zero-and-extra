import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import {promises as fs} from 'fs';
import path from 'path';
import {fileURLToPath} from 'url';

const app = express();

app.use(bodyParser.json());
app.use(cors())

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filepath = path.resolve(__dirname, "./products.json");

const readDatabase = async () => {
    try {
        const data = await fs.readFile(filepath, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        throw new Error("Failed to read database");
    }
}

const writeDatabase = async (data) => {
    try {
        await fs.writeFile(filepath, JSON.stringify(data), 'utf8');
    } catch (error) {
        console.error(error);
        throw new Error("Failed to write database");
    }
}

// all products with queries
app.get('/products', async (req, res) => {
    try {
        const queries = req.query;
        let data = await readDatabase();

        // sort query
        if("sort" in queries) {
            const sortType = queries["sort"].toLowerCase();

            switch(sortType) {
                case "ascending":
                    data = data.sort((a, b) => a.price - b.price);
                    break;
                case "descending":
                    data = data.sort((a, b) => b.price - a.price);
                    break;
            }
        }

        // minPrice query
        if("minPrice" in queries) {
            const minPrice = parseFloat(queries["minPrice"]);
            if (!isNaN(minPrice)) {
                data = data.filter(item => item.price >= minPrice);
            }
        }

        // maxPrice query
        if("maxPrice" in queries) {
            const maxPrice = parseFloat(queries["maxPrice"]);
            if (!isNaN(maxPrice)) {
                data = data.filter(item => item.price <= maxPrice);
            }
        }

        // limit query
        if("limit" in queries) {
            const limit = parseInt(queries["limit"]);
            if (!isNaN(limit)) {
                data = data.slice(0, limit);
            }
        }

        res.status(200).json(data);
    } catch (error) {
        console.error(error);
        return res.status(500).json({error: error.message});
    }
})

// single product by id
app.get("/products/:id", async (req, res) => {
    try {
        const id = parseInt(req.params.id);

        const data = await readDatabase();
        const item = data.filter(item => item.id === id);

        if (!item) {
            return res.status(404).json({error: 'Not Found'});
        }

        res.json(item);
    } catch (error) {
        console.error(error);
        res.status(500).json({error: error.message});
    }
})

// post
app.post("/products/add", async (req, res) => {
    try {
        const newProduct = req.body;

        const data = await readDatabase();
        const newId = data.length + 1;

        data.push({"id": newId, "name": newProduct.name, "price": newProduct.price});
        await writeDatabase(data);

        res.json(data)
    } catch (error){
        console.error(error);
        res.status(500).json({error: error.message});
    }
})

app.listen(3000, () => console.log('Server started on port 3000'));