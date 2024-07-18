// // This is main file

// // console.log(person1) error

// // We had attrobute type with property "module", so we can use import and export

// // This object is imported from alt1.js
// import { person1 } from "./alt1.js";
// console.log(person1)

// module - შეკვრა
// Entry point is main file
// Main js file is always connected to index.html
// package.json contains info about project

// Load the full build.
const _ = require('lodash');

const numbers = [1, 2, 3, 4, 5]
const shuffledNumbers = _.shuffle(numbers)
console.log(shuffledNumbers)