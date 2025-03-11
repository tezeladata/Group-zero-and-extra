import fs from "fs/promises";

const writeFile = async (file, data) => {
    try {
        await fs.writeFile(file, data);
        return "Information added successfully";
    } catch (e) {
        throw new Error("Error occurred while writing to file: " + e.message);
    }
};

export default writeFile;