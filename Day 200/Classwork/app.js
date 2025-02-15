import express from 'express';
import cors from "cors";
import {productsRouter} from "./Routes/products.routes.js";
import {adminsRouter} from "./Routes/admins.routes.js";

const app = express();

// Middlewares
app.use(express.json());
app.use(cors())

// Routes
app.use("/products", productsRouter);
app.use("/admins", adminsRouter)

// we use express.router when we want all of the registered routes not to be in one file
// this reduces risks of errors
// we can write code in simpler way
// extra server is not created, new route is just an object
// we export new router from routeName.routes.js file and import in main file - app.js
// then we use method called "use" to use this route
// this method takes 2 arguments: route (string) and route object (which is from routeName.routes.js file)
// use method is also used with middlewares like cors

app.listen(3000, () => console.log("Server started on port 3000"));