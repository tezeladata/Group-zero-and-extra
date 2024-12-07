// const numbers = [];
//
// process.stdin.on("data", info => {
//     const number = parseInt(info)
//     numbers.push(number);
//
//     if (numbers.length === 10){
//         process.stdout.write(`Sum of numbers is: ${numbers.reduce((sum, num) => sum + num, 0)}\n`);
//         process.exit();
//     }
// })



// const errorFirstCallback = (err, data) => {
//     if (err){
//         console.log(`${err.message}`);
//     } else {
//         console.log(`Received ${data}`);
//     }
// }
//
// const filt = (input, callback) => {
//     if (input === 0 || isNaN(input)){
//         const err = Error("Error occured");
//         callback(err, input)
//     } else {
//         callback(null, input);
//     }
// }
//
// process.stdin.on("data", chunk => {
//     try {
//         const number = parseInt(chunk);
//
//         filt(number, errorFirstCallback);
//     } catch (error) {
//         console.error(error);
//     }
// })



// process.stdout.write("Choose one from the following numbers: 1, 2, 3, 4, 5\n");
//
// const taskOneCallback = (err, data) => {
//     if (err) {
//         process.stdout.write(`${err.message}\n`);
//     } else {
//         process.stdout.write(`Information received correctly: ${data}\n`);
//     }
// };
//
// process.stdin.on("data", chunk => {
//     try {
//         const number = parseInt(chunk.toString().trim(), 10);
//
//         if (isNaN(number) || (number < 1 || number > 5)) {
//             const err = new Error("Invalid number");
//             taskOneCallback(err, number);
//         } else {
//             taskOneCallback(null, number);
//         }
//     } catch (e) {
//         console.error(e.toString());
//     }
// });
//

const fs = require('fs');

const width = 1000;
const height = 1000;

const pixelData = Buffer.alloc(width * height * 4);

function drawCircle(centerX, centerY, radius) {
    for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x++) {
            const distance = Math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2);
            const index = (y * width + x) * 4;

            if (distance <= radius) {
                pixelData[index] = 0;   // Red
                pixelData[index + 1] = 255; // Green
                pixelData[index + 2] = 0;   // Blue
                pixelData[index + 3] = 255; // Alpha
            } else {
                pixelData[index] = 0;     // Red
                pixelData[index + 1] = 0; // Green
                pixelData[index + 2] = 0; // Blue
                pixelData[index + 3] = 255; // Alpha
            }
        }
    }
}

drawCircle(500, 500, 200);

fs.writeFileSync('output.raw', pixelData);
console.log('Raw image data has been written to output.raw');