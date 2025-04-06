import fs from "fs/promises";

const readFile = async (file) => {
    try {
        // get data from json file and return it parsed
        const data = await fs.readFile(file, "utf8");
        return JSON.parse(data)
    } catch(e) {
        // return error if it exists
        return e
    }
};

export default readFile;