import fs from "fs/promises";

const writeFile = async (file, data) => {
    try {
        // write data in given file and return message
        await fs.writeFile(file, JSON.stringify(data));
        return "Data written successfully"
    } catch(e) {
        // return error if it happens
        return e
    }
};

export default writeFile;