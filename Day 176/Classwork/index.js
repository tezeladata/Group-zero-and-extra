const fs = require("fs");

// read txt file
fs.readFile("text.txt", "utf8", (err, data) => {
    if (err) {
        console.error("Error reading file:", err);
        return;
    }

    const buffered = Buffer.from(data, "utf8");
    const updated = Buffer.from(buffered.map(byte => byte + 1));

    console.log(updated);
    console.log(updated.toString("utf8"));
});

// read json file
fs.readFile("data.json", "utf8", (err, data) => {
    if (err) {
        console.error("Error reading file:", err);
        return;
    }

    console.log(data);
})

// create file
let inputData = "";

process.stdin.on("data", (chunk) => {
    inputData += chunk.toString(); // Accumulate input data

    // Write the accumulated data to the file
    fs.writeFile("text2.txt", inputData, (err) => {
        if (err) {
            console.error("Error writing file:", err);
        } else {
            console.log("File written successfully");
        }
        process.exit(); // Exit the process after writing
    });
});


const readline = require("readline");

const interface1 = readline.createInterface({
    input: fs.createReadStream("data.txt")
})

let lineNumber = 1
interface1.on("line", (fileline) => {
    console.log(`Line N${lineNumber}: ${fileline}`)
    lineNumber++;
})