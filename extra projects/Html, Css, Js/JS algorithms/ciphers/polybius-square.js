console.log("Hello, this is Polybius square code");

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter your text here: ", (str) => {
    let originalStr = str.toUpperCase();
    let originalArr = originalStr.split(''); 
    const polybiusGrid = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "K"],
        ["L", "M", "N", "O", "P"],
        ["Q", "R", "S", "T", "U"],
        ['V', 'W', 'X', 'Y', 'Z']
    ];
    let resStr = "";

    for (let i = 0; i < originalArr.length; i++) {
        let letter = originalArr[i];
        if (letter === ' ') {
            resStr += '  '; 
        } else if (letter >= 'A' && letter <= 'Z') {
            for (let j = 0; j < polybiusGrid.length; j++) {
                for (let k = 0; k < polybiusGrid[j].length; k++) {
                    if (polybiusGrid[j][k] === letter) {
                        resStr += `${j + 1}${k + 1} `;
                    }
                }
            }
        } else {
            resStr += letter; 
        }
    }
    console.log(`Code for "${originalStr.toLowerCase()}" is "${resStr}"`);
    rl.close();
});