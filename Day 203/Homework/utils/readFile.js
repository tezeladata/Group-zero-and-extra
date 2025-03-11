import fs from "fs/promises";

const readFile = async (file) => {
    try {
        return JSON.parse(await fs.readFile(file, "utf8"))
    } catch (e) {
        throw e
    }
};

export default readFile