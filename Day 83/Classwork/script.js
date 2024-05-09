// forEach does not return any new array

const numbers = [1, 2, 3, 4, 5]
for (let i=0; i<numbers.length; i++){
    console.log(numbers[i])
}
// Better way:
let result = 0;

numbers.forEach(function(value){
    result += value
})
console.log(result)


// manual forEach
function manualForEach(array, func1){
    for (let i=0; i<array.length; i++){
        func1(array[i])
    }
}

manualForEach(numbers, function(value){
    console.log(value)
})


// Manual reduce
function manualReduce(arr, func, startingValue){
    let result = startingValue;

    for (let i=0; i<arr.length; i++){
        result = func(result, arr[i])
    }

    return result
}

// 1
const strArr = "data".split("")
const result2 = manualReduce(strArr, function(result, nextElement){
    return result + nextElement
}, "data")
console.log(result2)
// 2
const result3 = manualReduce(numbers, function(result, nextElement){
    return result + nextElement
}, 3)
console.log(result3)

const sum1 = numbers.reduce(function(preValue, curValue){
    return preValue + curValue
})

// manual every
function manualEvery(arr, func){
    let allRes = 0;

    for (let i = 0; i < arr.length; i++){
        allRes += func(arr[i])
    }

    console.log(allRes > 0)
}

manualEvery([1, 2, 3, 4, 5], function(value){
    if (value > 3){
        return 1
    }
})