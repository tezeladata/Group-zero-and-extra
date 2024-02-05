// length
let country="Georgia"
let length=country.length;
console.log(length)
// The charAt() method returns the character at a specified index (position) in a string:
let secondChar=country.charAt(1)
//                    We use () instead of []
console.log(secondChar)
// The charCodeAt() method returns the code of the character at a specified index in a string:
let thirdCharCode=country.charCodeAt(2)
console.log(thirdCharCode)
// Property access
let fourthChar=country[3]
console.log(fourthChar)
// or
let fifthChar=country.at(4)
console.log(fifthChar)
// at allows to use negative indexes also
let lastChar=country.at(-1)
console.log(lastChar)
// Simple boolean
console.log(country[2]=="A")


// Extracting String Parts
// Slice(start, end)
let name="Goal-Oriented Academy"
console.log(name.slice(2,6))
// If you omit the second parameter, the method will slice out the rest of the string:
console.log(name.slice(3))
// Same for negative
console.log(name.slice(-10))
// It is same for two negative indexes

// Substring is almost same as slice, but negative indexes are counted as 0
console.log(name.substring(-13,-5))

// Substr is almost same as slice, but the difference is that the second parameter specifies the length of the extracted part.
let str = "Apple, Banana, Kiwi";
let part = str.substr(7, 12);
console.log(part)


// uppercase, lowercase
console.log("abcdefg".toUpperCase())
console.log("abcdefg".toUpperCase().toLowerCase())
// concat() joins two or more strings:
let part1="Abcdefghijk";
let part2="lmnopqrstuv"
console.log(part1.concat(" ", part2))

// The trim() method removes whitespace from both sides of a string:
console.log("                David                ".trim())
// trimStart only works for starting part:
console.log("                Andria              ".trimStart())
// TrimEnd only works for ending part:
console.log("                Andria                  ".trimEnd())

// The padStart() method pads a string from the start.
console.log("1".padStart(10, "."))

let numb = 5;
let text = numb.toString();
let padded = text.padStart(4,"0");
console.log(padded)
// Same is for padEnd

// repeat method returns string for specified times
console.log(" Hello World".repeat(10))

// The replace() method replaces a specified value with another value in a string:
console.log("ABCDEFGHIJKLMNOPQRSTUVWXYZ".replace("ABCDEF", "123456"))