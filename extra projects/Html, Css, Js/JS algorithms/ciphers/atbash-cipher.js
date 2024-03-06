console.log("Hello, this is Atbash cipher code");

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter your text here: ", (str) => {
    let originalStr = str.toLowerCase();
    let alphabet = 'abcdefghijklmnopqrstuvwxyz';
    let reversedAlphabet = 'zyxwvutsrqponmlkjihgfedcba';
    let result = "";
    for (let i = 0; i < originalStr.length; i++) {
        let char = originalStr[i];
        let charIndex = alphabet.indexOf(char);
        if (charIndex !== -1) {
            let cipheredChar = reversedAlphabet[charIndex];
            // Preserve case
            if (char === char.toUpperCase()) {
                result += cipheredChar.toUpperCase();
            } else {
                result += cipheredChar;
            }
        } else {
            result += char;
        }
    }
    console.log(`Here is your text:\n${result}`);
    rl.close();
});