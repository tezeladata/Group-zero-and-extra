const Logger = async (req, res, next) => {
    const log = {
        method: req.method,
        url: req.url,
        timestamp: new Date().toISOString(),
    }

    // Log
    console.log(log);

    // Continue
    next()
};

export default Logger;