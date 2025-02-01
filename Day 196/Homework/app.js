import express, {query} from 'express';
import cors from 'cors';
import bodyParser from "body-parser";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const app = express();

app.use(cors());
app.use(bodyParser.json());

// for data read and write
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.resolve(__dirname, "./products.json");

// read json file
const readDatabase = () => {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, "utf8", (err, data) => {
            if (err) {
                reject("Failed to read file");
            } else {
                try {
                    resolve(JSON.parse(data));
                } catch (parseError) {
                    reject("Failed to parse JSON");
                }
            }
        });
    });
};

// Update json file
const writeDatabase = async (data) => {
    try {
        await fs.writeFile(filePath, JSON.stringify(data, null, 2), "utf-8");
    } catch (error) {
        console.error("Error writing to the database:", error);
        throw new Error("Unable to write to database");
    }
};

app.get("/products", async (req, res) => {
    try {
        const queries = req.query;
        let allProducts = await readDatabase();

        if ("sort" in queries) {
            const sortType = req.query.sort?.toLowerCase();

            switch (sortType) {
                case "ascending":
                    allProducts.sort((a, b) => a.price - b.price);
                    break;
                case "descending":
                    allProducts.sort((a, b) => b.price - a.price);
                    break;
            }
        }

        if ("minPrice" in queries) {
            const minPrice = parseFloat(queries.minPrice);
            if (!isNaN(minPrice)) {
                allProducts = allProducts.filter(product => product.price >= minPrice);
            }
        }

        if ("maxPrice" in queries) {
            const maxPrice = parseFloat(queries.maxPrice);
            if (!isNaN(maxPrice)) {
                allProducts = allProducts.filter(product => product.price <= maxPrice);
            }
        }

        if ("limit" in queries) {
            const limit = parseInt(queries.limit);
            if (!isNaN(limit) && limit > 0) {
                allProducts = allProducts.slice(0, limit);
            }
        }


        res.json(allProducts);
    } catch (error) {
        res.status(500).json({ error });
    }
});

app.get("/products/:id", async (req, res) => {
    try {
        const id = parseInt(req.params.id);
        const allProducts = await readDatabase();

        const item = allProducts.filter(product => product.id === id);

        if (item.length === 0) {
            return res.status(404).send("Invalid ID");
        }

        res.json(item[0]);
    } catch (error) {
        res.status(500).json({ error });
    }
})

app.listen(3000, () => console.log('Server started on port 3000'));