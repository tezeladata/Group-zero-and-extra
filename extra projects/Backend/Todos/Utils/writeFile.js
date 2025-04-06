import fs from "fs/promises";

const writeFile = async (filepath, data) => {
    try {
        await fs.writeFile(filepath, JSON.stringify(data), "utf8");
        return "Data written successfully";
    } catch (e) {
        return e
    }
};

export default writeFile;