
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


rl.question("Enter your text here: ", (str) => {
    str=str.toUpperCase();
    const morseCodeDictionary = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', '"': '.-..-.', 
        ':': '---...', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', 
        '=': '-...-', '+': '.-.-.', '@': '.--.-.', " ": "  "
    }
    let resStr="";
    for (let i=0; i<str.length; i++){
        let char=str[i];
        char=morseCodeDictionary[char];
        resStr+=char + " ";
    }
    console.log(resStr)
    rl.close();
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