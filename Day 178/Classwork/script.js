const fs = require("fs");

fs.readFile("data.json", "utf8", (err, data) => {
    if (err) throw err;

    console.log(data);
})

fs.writeFile("text2.txt", "Hello world", (err) => {
    if (err) {
        console.error("Error writing file:", err);
    } else {
        console.log("File written successfully");
    }
});