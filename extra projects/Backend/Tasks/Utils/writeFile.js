import fs from 'fs/promises';

const writeFile = async (file, data) => {
    try {
        // save data to file
        await fs.writeFile(file, JSON.stringify(data));
        return "Data saved successfully.";
    } catch (e) {
        return e
    }
};

export default writeFile;