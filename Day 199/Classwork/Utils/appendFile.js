import fs from "fs/promises";
import readFile from "./readFile.js";

const appendFile = async (fileName, data) => {
    try {
        let products = await readFile(fileName);
        products.push(data);

        await fs.writeFile(fileName, JSON.stringify(products, null, 2));
        console.log("Data added successfully.");
    } catch (e) {
        throw new Error(`Error: ${e.message}`);
    }
};

export default appendFile;