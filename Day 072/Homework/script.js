// Copy functions of: Math.min, Math.max, Math.ceil, Math.pow, Math.round, Math.sqrt, Math.trunc, Math.abs


// Math.min
console.log(Math.min(6, 6, 5, 4, 3, 2, 1))
// Copy function:
function returnMinimal(array){
    let minimal = array[0]

    for (let i=0; i<array.length; i++){
        let numb = array[i]
    
        if (numb < minimal){
            minimal = numb
        }
    }
    return `Minimal number in the list is: ${minimal}`
}
// Test cases:
console.log(returnMinimal([6, 6, 5, 4, 3, 2, 1]))
console.log(returnMinimal([5, 4, 10, 12, 3, 7, 5]))
console.log(returnMinimal([100, 90, 80, 70, 60, 50]))



// Math.max
console.log(Math.max(6, 6, 5, 4, 3, 2, 1))
// Copy function:
function returnMaximal(array){
    let maximum = array[0]

    for (let i=0; i<array.length; i++){
        let numb = array[i]
    
        if (numb > maximum){
            maximum = numb
        }
    }
    return `Maximal number in the list is: ${maximum}`
}
// Test cases:
console.log(returnMaximal([6, 6, 5, 4, 3, 2, 1]))
console.log(returnMaximal([5, 4, 10, 12, 3, 7, 5]))
console.log(returnMaximal([100, 90, 80, 70, 60, 50]))



// Math.floor
console.log(Math.floor(3.7))
console.log(Math.floor(5.2))
console.log(Math.floor(-3.2))
// Copy function:
function returnFloor(number){
    // If already integer
    if (Number.isInteger(number)){
        return `Floor for ${number} is: ${number}`
    }

    // Negative numbers
    if (number < 0){
        if (number == parseInt(number)){
            return `Floor for ${number} is: ${parseInt(number)}`
        } else{
            return `Floor for ${number} is: ${parseInt(number) - 1}`
        }
    }

    // Positive floats
    return `Floor for ${number} is: ${parseInt(number)}`
}
// Test cases:
console.log(returnFloor(3.7))
console.log(returnFloor(5.2))
console.log(returnFloor(-3.2))



// Math.ceil
console.log(Math.ceil(3.7))
console.log(Math.ceil(5.2))
console.log(Math.ceil(-3.5))
console.log(Math.ceil(3))
// Copy function:
function returnCeil(number){
    // If already integer
    if (Number.isInteger(number)){
        return `Ceiling for ${number} is: ${number}`
    }

    // If negative number
    if (number < 0){
        return `Ceiling for ${number} is: ${parseInt(number)}`
    }

    return `Ceiling for ${number} is: ${parseInt(number) + 1}`
}
// Test cases:
console.log(returnCeil(3.7))
console.log(returnCeil(5.2))
console.log(returnCeil(-3.5))



// Math.pow
console.log(Math.pow(7, 2))
console.log(Math.pow(16, 0.5))
console.log(Math.pow(20, 2))
// Copy function:
function returnPower(number, power){
    return `${number} in power of ${power} is: ${number**power}`
}
// Test cases:
console.log(returnPower(7, 2))
console.log(returnPower(16, 0.5))
console.log(returnPower(20, 2))



// Math.round
console.log(Math.round(-5.5))
console.log(Math.round(-5.2))
console.log(Math.round(-5.7))
console.log(Math.round(-6))
// Copy function:
function returnRound(number) {
    // Already integer
    if (Number.isInteger(number)) {
        return `Rounded ${number} is: ${number}`;
    }

    // Convert number to string and split into array
    let numStr = number.toString();
    // Decimal part
    let numArr = numStr.split('');

    // negative numbers
    if (number < 0) {
        let decimalIndex = numArr.indexOf('.');

        // integer part
        let integerPart = parseInt(numArr.slice(0, decimalIndex).join(''));
        let decimalPart = parseInt(numArr[decimalIndex + 1]);

        if (decimalPart <= 5) {
            return `Rounded ${number} is: ${integerPart}`;
        } else {
            return `Rounded ${number} is: ${integerPart - 1}`;
        }
    }

    // Handle positive numbers
    let decimalIndex = numArr.indexOf('.');
    // integer part
    let integerPart = parseInt(numArr.slice(0, decimalIndex).join(''));
    // decimal part
    let decimalPart = parseInt(numArr[decimalIndex + 1]);

    if (decimalPart >= 5) {
        return `Rounded ${number} is: ${integerPart + 1}`;
    } else {
        return `Rounded ${number} is: ${integerPart}`;
    }
}
console.log(returnRound(-5.5))
console.log(returnRound(-5.2))
console.log(returnRound(-5.7))
console.log(returnRound(-6))



// Math.sqrt
console.log(Math.sqrt(4))
console.log(Math.sqrt(9))
console.log(Math.sqrt(10000))
// Copy function
function returnRoot(number){
    return `Square root from ${number} is: ${number**0.5}`
} 
console.log(returnRoot(4))
console.log(returnRoot(9))
console.log(returnRoot(10000))



// Math.trunc
console.log(Math.trunc(14.14))
console.log(Math.trunc(3.29))
console.log(Math.trunc(1.182))
// Copy function
function returnTrunc(number){
    number = String(number);
    let dotIndex = number.indexOf(".")

    let intArr = []
    for (let i=0; i<dotIndex; i++){
        intArr.push(number[i])
    }
    let result = intArr.join("");
    return `Truncated version of ${number} is: ${result}`
}
console.log(returnTrunc(14.14))
console.log(returnTrunc(3.29))
console.log(returnTrunc(1.182))



// Math.abs
console.log(Math.abs(5))
console.log(Math.abs(-5))
console.log(Math.abs(10))
console.log(Math.abs(-10))
// Copy function
function returnAbs(number){
    if (number >= 0){
        return `Absolute value for ${number} is: ${number}`
    } else{
        return `Absolute value for ${number} is: ${number * -1}`
    }
}
// Test cases:
console.log(returnAbs(5))
console.log(returnAbs(-5))
console.log(returnAbs(10))
console.log(returnAbs(-10))