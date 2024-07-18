console.log("Hello world!")
console.log(process)

// import { shuffle } from "./second.js"
// // Needed package.json for it
// console.log(shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

// for fastest way, in terminal we write: "npm init -y"
// "main": "script.js",
// "type": "module",
// Those 2 have to be correctly adjusted

// Npm is tool that comes with node.js

const _ = require("lodash");
// require is same as import
console.log(_.shuffle([1, 2, 3, 4, 5, 6, 7]))

// module.exports is old way for export
const myShuffle = require("./second.js")
console.log(myShuffle([1, 2, 3, 4, 5, 6, 7]))