// 1
let sum = 0;
let numArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numArr.forEach(function(value){
    sum += value
})

console.log(sum)


// 2
numArr.forEach(function(value, index){
    console.log(`Value: ${value}, index: ${index}`)
})


// 3
let product = numArr.reduce(function(accumulator, curValue){
    return accumulator *= curValue
})

console.log(product)


// 4
let matrix = [
    [
        {"a": 1, "b": 2, "c": 3},
        {"d": 4, "e": 5, "f": 6}
    ],
    [
        {"h": 7, "i": 8, "j": 9},
        {"k": 10, "l": 11, "m": 12}
    ],
    [
        {"n": 13, "o": 14, "p": 15},
        {"q": 16, "r": 17, "s": 18}
    ]
];

let hom4_list = matrix.reduce(function(accumulator, currentValue) {
    return accumulator.concat(currentValue);
});

console.log(hom4_list);


// 5
function manualForEach(iterable, func){
    let res = [];

    for (let i=0; i<iterable.length; i++){
        res.push(func(iterable[i]))
    }

    return res
}

function forEachFunc(value){
    return value**2
}
console.log(manualForEach([10, 15, 20, 25, 30], forEachFunc))


// 6
function manualReduce(arr, func, startingValue){
    let result = startingValue;

    for (let i=0; i<arr.length; i++){
        result = func(result, arr[i])
    }

    return result
}

// 6-1
const strArr = "data".split("")
const result2 = manualReduce(strArr, function(result, nextElement){
    return result + nextElement
}, "data")
console.log(result2)


// 7
let strs = ["Hello", "this", "is", "David", "Hello", "again"]
function task7(strArr){
    // First we flatten into one string
    let strs2 = strArr.reduce(function(accumulator, curValue){
        return accumulator += ` ${curValue}`
    })

    // Then we show flattened string
    console.log(`Flattened array is: "${strs2.trim()}"`)

    // Then str is converted into array
    strs2 = strs2.split(" ")
    
    // Then we show occurencers
    let resObj = Object();

    strs2.forEach(function(word){
        if (resObj[word]){
            resObj[word] ++;
        } else{
            resObj[word] = 1;
        }
    })

    return resObj
}

console.log(task7(strs))