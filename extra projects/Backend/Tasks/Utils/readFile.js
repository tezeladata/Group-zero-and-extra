import fs from "fs/promises";

const readFile = async (file) => {
    try {
        // get data and parse it
        const data = await fs.readFile(file, "utf8");
        return JSON.parse(data);
    } catch (e) {
        return e
    }
};

export default readFile;