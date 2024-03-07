console.log("Hello, this is Keyboard shift cipher code");

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter your text here: ", (str) => {
    rl.question("Right shift or left shift: ", (shift) => {
        str = str.toUpperCase();
        let resStr = "";
        if (shift === "right" || shift === "Right") {
            const keyboardLayout = {
                'Q': 'W', 'W': 'E', 'E': 'R', 'R': 'T', 'T': 'Y', 'Y': 'U', 'U': 'I', 'I': 'O', 'O': 'P',
                'A': 'S', 'S': 'D', 'D': 'F', 'F': 'G', 'G': 'H', 'H': 'J', 'J': 'K', 'K': 'L', 'L': ';',
                'Z': 'X', 'X': 'C', 'C': 'V', 'V': 'B', 'B': 'N', 'N': 'M', 'M': ','
            };
            for (let i = 0; i < str.length; i++) {
                let char = str[i];
                resStr += keyboardLayout[char] || char;
            }
        } else if (shift === "left" || shift === "Left") {
            const keyboardLayout = {
                'Q': 'P', 'W': 'Q', 'E': 'W', 'R': 'E', 'T': 'R', 'Y': 'T', 'U': 'Y', 'I': 'U', 'O': 'I', 'P': 'O',
                'A': 'L', 'S': 'A', 'D': 'S', 'F': 'D', 'G': 'F', 'H': 'G', 'J': 'H', 'K': 'J', 'L': 'K',
                'Z': 'M', 'X': 'Z', 'C': 'X', 'V': 'C', 'B': 'V', 'N': 'B', 'M': 'N'
            };
            for (let i = 0; i < str.length; i++) {
                let char = str[i];
                resStr += keyboardLayout[char] || char;
            }
        } else {
            console.log("Incorrect command!");
            rl.close();
        }

        console.log(resStr);
        rl.close();
    });
});