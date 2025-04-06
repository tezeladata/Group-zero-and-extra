import readFile from "../Utils/readFile.js";
import writeFile from "../Utils/writeFile.js"

const logger = async (req, res, next) => {
    const log = {
        "timestamp": new Date().toISOString(),
        "method": req.method,
        "url": req.url
    }

    // Previous data
    const previous = await readFile("./Database/logs.json");
    
    // Add new data
    previous.push(log);

    // Save changes
    writeFile("./Database/logs.json", previous);

    // Go to next middleware
    next();
}

export default logger;