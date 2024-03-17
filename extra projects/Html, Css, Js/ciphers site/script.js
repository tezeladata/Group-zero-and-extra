// Rot 13
let rot13Button = document.getElementById("button1");
rot13Button.addEventListener("click", function(){
    let inputText = document.querySelector(".rot13 .text-area").value;
    let rot13Input = document.getElementById("rot13-input")
    let alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let result = "";

    for (let i = 0; i < inputText.length; i++) {
        let char = inputText[i];
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
    
    let rot13P = document.getElementById("output1");
    rot13P.style.display = "block";
    rot13P.innerHTML = result;

    setTimeout(function() {
        rot13P.style.display = "none";
        rot13Input.value = "";
    }, 10000);
});

// Atbash cipher
let atbashButton = document.getElementById("button2");
atbashButton.addEventListener("click", function(){
    let originalInput = document.getElementById("atbash-input");
    let originalStr = originalInput.value.toLowerCase();
    let alphabet = 'abcdefghijklmnopqrstuvwxyz';
    let reversedAlphabet = 'zyxwvutsrqponmlkjihgfedcba';
    let result = "";

    for (let i = 0; i < originalStr.length; i++) {
        let char = originalStr[i];
        let charIndex = alphabet.indexOf(char);
        if (charIndex !== -1) {
            let cipheredChar = reversedAlphabet[charIndex];
            if (char === char.toUpperCase()) {
                result += cipheredChar.toUpperCase();
            } else {
                result += cipheredChar;
            }
        } else {
            result += char;
        }
    }

    let atbashCipherP = document.getElementById("output2");
    atbashCipherP.style.display = "block";
    atbashCipherP.innerHTML = result;

    setTimeout(function() {
        atbashCipherP.style.display = "none";
        originalInput.value = ""; 
    }, 10000); 
});

// Polybius square
let polybiusButton = document.getElementById("button3");
    polybiusButton.addEventListener("click", function(){
        let polybiusInput = document.getElementById("polybius-input")
        let originalStr = polybiusInput.value.toUpperCase();
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
                            break; 
                        }
                    }
                }
            } else {
                resStr += letter; 
            }
        }

        let polybiusP = document.getElementById("output6");
        polybiusP.style.display = "block";

        polybiusP.innerHTML = resStr;

        setTimeout(function() {
            polybiusP.style.display = "none";
            polybiusInput.value = "";
        }, 10000);
});

// Keyboard shift
let keyboardShiftButton=document.getElementById("button4");
keyboardShiftButton.addEventListener("click", function(){
    let keyboardShiftInput = document.getElementById("keyboard-shift-input1");
    let str = keyboardShiftInput.value.toUpperCase();
    let keyboardShiftInput2 = document.getElementById("keyboard-shift-input2");
    let shift=keyboardShiftInput2.value;

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
    } 
    
    let keyboardShiftP=document.getElementById("output4");
    keyboardShiftP.style.display = "block";
    keyboardShiftP.innerHTML = resStr;

    setTimeout(function() {
        keyboardShiftP.style.display = "none";
        keyboardShiftInput.value = "";
        keyboardShiftInput2.value = "";
    }, 10000);
})

// Morse code
let morseCodeButton = document.getElementById("button5");
morseCodeButton.addEventListener("click", function(){
    let morseCodeInput = document.getElementById("morse-code-input");
    let str=morseCodeInput.value.toUpperCase();
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

    let morseCodeP = document.getElementById("output5");
    morseCodeP.style.display = "block";
    morseCodeP.innerHTML = resStr;

    setTimeout(function() {
        morseCodeP.style.display = "none";
        morseCodeInput.value = "";
    }, 10000);
})

// Caesar cipher
let caesarCipherButton = document.getElementById("button6");
caesarCipherButton.addEventListener("click", function(){
    let caesarCipherInput = document.getElementById("caesar-cipher-input1").value;
    let caesarCipherInput2 = document.getElementById("caesar-cipher-input2").value;
    let shift = Math.abs(parseInt(caesarCipherInput2));
    let alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let result = "";
    
    for (let i = 0; i < caesarCipherInput.length; i++) {
        let char = caesarCipherInput[i];
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

    let caesarCipherP = document.getElementById("output3");
    caesarCipherP.style.display = "block";
    caesarCipherP.innerHTML = result;

    setTimeout(function() {
        caesarCipherP.style.display = "none";
        document.getElementById("caesar-cipher-input1").value = "";
        document.getElementById("caesar-cipher-input2").value = "";
    }, 10000);
});



// Removing contact messages
let form = document.getElementById("form")

form.addEventListener("submit", function(e){
    e.preventDefault();
    for (let i=0; i<form.elements.length; i++){
        // console.log(form.elements[i].value);
        form.elements[i].value = "";
    }
})