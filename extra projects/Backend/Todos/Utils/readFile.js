import fs from "fs/promises";

const readFile = async (filepath) => {
    try {
        const data = await fs.readFile(filepath, "utf8");
        return JSON.parse(data)
    } catch (e) {
        return e
    }
};

export default readFile;