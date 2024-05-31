const numbers = [1, 5, 8, 4, 9, 3, 10];
const lastPrime = numbers.lastIndexOf(function(value){
    let count = 0;
    for (let i=2; i<= value; i++){
        if (count > 2) return false;
        if (value%i==0) count ++;
        return true
    }
})

console.log(lastPrime)


// Hoisting with functions
const sum = calculateSum([1, 2, 3])
console.log(sum)

function calculateSum(numberArr){
    const sum = numberArr.reduce(function(prevSum, curValue){
        return prevSum + curValue
    }, 0)

    return sum
}

// Hoisting with variables
console.log(num)
var num = 5;


// Variables created with var
// When we use var, it uses hoisting, so it's placed at the start of the code
// var variables can be reassigned


// Template literals
console.log(`Number is ${num}`)


// for in gives us indices
for (const index in numbers){
    console.log(index)
}
// Weakness for for in is that it uses arbitary order (random number)


// for of
for (const value of numbers){
    console.log(value)
}


// arrow function
const calcSum = arr => arr[0]
console.log(calcSum(numbers))

const multip = (a, b, c) => a + b + c
console.log(multip(1, 2, 3))

console.log(numbers.forEach((_, __, arr) => arr))