// 1
function findSum(numbers){
    let sum = 0;
    for(const num of numbers){
        sum += num;
    }

    return sum
}
console.log(findSum([1, 2, 3, 4, 5, 6, 7]))

// 2
function findLongest(strs){
    let maxLen = strs[0].length;
    let res = strs[0];

    for (let word of strs){
        if (maxLen < word.length){
            res = word;
            maxLen = word.length
        }
    }
    
    return res
}
console.log(findLongest(["this", "is", "Goa", "Hello"]))

// 3
function countProp(obj){
    let count = 0;

    for (let i in obj){
        count ++;
    }

    return count
}
console.log(countProp({a: 10, b: 20, c: 30, d:40}))

// 4
function returnKeys(obj){
    let keys = [];

    for (key in obj){
        keys.push(key)
    }

    return keys
}
console.log(returnKeys({a: 10, b: 20, c: 30, d:40}))

// 5
// Scope is like a border for variable's sight. When variable has scope of loop or function, we cannot use it in another function or loop.
// Because of scopes, we are able to create variables with same names at different places
// variables created with var keyword have only function scope, else they can be called anywhere

// Variables declared with var, let and const are quite similar when declared inside a function.
// They all have Function Scope

// A variable declared outside a function, becomes GLOBAL
// Global variables can be accessed from anywhere in a JavaScript program.

// 6
// variables, which are created with var keyword, are hoisted. This means, that we can use them, before their declaration.
// This sometimes becomes annoying.
// Functions are also hoisted, so they become placed at the start of the code, at the top

// 7
console.log((num => num**2)(5))

// 8
console.log(((arr) => arr.filter((value) => value%2==0))([1, 2, 3, 4, 5, 6, 7]))

// 9
console.log((arr => arr.reduce((prevValue, curValue) => prevValue + curValue, 0))([1, 2, 3, 4, 5]))

// 10
const fib = (len => {
    let res = [0, 1];

    if (len <= 1) return "Invalid length"
    else if (len === 1) return res[0]
    else if (len === 2) return res
    else {
        while (res.length < len){
            res.push(res[res.length -2] + res[res.length -1])
        }

        return res
    }
})
console.log(fib(10))

// 11
console.log((str => str === str.split("").reverse().join(""))("aba"))