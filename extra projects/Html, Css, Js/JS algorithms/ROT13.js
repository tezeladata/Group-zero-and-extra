console.log("Hello, this is ROT13 cypher code");

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter your text here: ", (str) => {
    let alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let result = "";
    for (let i = 0; i < str.length; i++) {
        let char = str[i];
        if (alphabet.includes(char)) {
            let idx = (alphabet.indexOf(char) + 13) % 26;
            if (char === char.toLowerCase()) {
                result += alphabet[idx];
            } else {
                result += alphabet[idx + 26];
            }
        } else {
            result += char;
        }
    }
    console.log(`Here is your text:\n${result}`);
    rl.close();
});