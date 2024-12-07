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