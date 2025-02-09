import express from 'express';
import cors from 'cors';
import {productsRoute} from "./Routes/products.route.js";

const app = express();

app.use(cors());
app.use(express.json());

// Routers
app.use('/products', productsRoute)

app.listen(3000, () => {
    console.log(`Server started on port 3000`);
})