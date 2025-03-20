import fs from 'fs/promises';

const readFile = async (path) => {
    const data = await fs.readFile(path, 'utf8');
    return JSON.parse(data);
}

export default readFile;