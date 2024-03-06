console.log("Hello, this is Caesar cipher code");

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter your text here: ", (str) => {
    rl.question("Enter shift Number here: ", (shift) => {
        let alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        shift = parseInt(shift);
        let result = "";
        for (let i = 0; i < str.length; i++) {
            let char = str[i];
            if (alphabet.includes(char)) {
                let idx = alphabet.indexOf(char);
                if (char === char.toLowerCase()) {
                    idx = (idx + shift) % 26;
                } else {
                    idx = (idx + shift + 26) % 52; 
                }
                result += alphabet[idx];
            } else {
                result += char;
            }
        }
        console.log(`Here is your text:\n${result}`);
        rl.close();
    })
});