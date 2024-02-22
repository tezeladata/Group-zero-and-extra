// The indexOf() method returns the index (position) of the first occurrence of a string in a string, or it returns -1 if the string is not found
const name = "David Tezelashvili";
console.log(name.indexOf("l"))

// Apparently lastIndexOf is used for the last occurence
console.log(name.lastIndexOf("i"))

// Both indexOf and lastIndexOf return -1 if given argument is not found
console.log(name.indexOf("g"), name.indexOf("b"))

// You can also give starting position, where it will start searching
console.log(name.indexOf("i", 5))

// Search method searches string for a string
console.log(name.search("li"))

// The match() method returns an array containing the results of matching a string
console.log(name.match("i"))

console.log(name.matchAll("i"))

// Includes is used to see if string includes some kind of text
console.log(name.includes("a")) // Boolean

// The startsWith() method returns true if a string begins with a specified value.
console.log(name.startsWith("D"))
// You can also give starting position
console.log(name.startsWith(("a"), 1))

// EndsWith() works like startsWith() method
console.log(name.endsWith("i"))