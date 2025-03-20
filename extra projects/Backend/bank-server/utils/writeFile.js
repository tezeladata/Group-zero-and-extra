import fs from "fs/promises";

const writeFile = async (path, data) => {
    await fs.writeFile(path, JSON.stringify(data), { encoding: 'utf8' });
    return "Data written successfully.";
}

export default writeFile;