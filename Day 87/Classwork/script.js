// if we const, it is permanent information storage, not changeable

// every
const carArr = [{name: "Bmw", color: "blue"}, {name: "Audi", color: "blue"}, {name: "Fiat", color: "blue"}, {name: "Bmw", color: "red"}]
const isAllRed = carArr.every(function(value){
    return value.color.toLowerCase() === "blue";
})
console.log(isAllRed)


function manualEvery(arr, func){
    for (let i=0; i<arr.length; i++){
        const isTrue = func(arr[i])

        // if false
        if (! isTrue){
            return false
        }
    }

    return true
}
console.log(manualEvery(carArr, function(value){
    return value.color.toLowerCase() === "blue"
}))


// some
const isAnyRed = carArr.some(function(value){
    return value.color.toLowerCase() === "red";
})
console.log(isAnyRed)

function manualSome(arr, func){
    for (let i=0; i<arr.length; i++){
        const isTrue = func(arr[i])

        // if true
        if (isTrue){
            return true
        }
    }

    return false
}
console.log(manualSome(carArr, function(value){
    return value.color.toLowerCase() === "red"
}))


// find
console.log(carArr.find(function(value){
    return value.color.toLowerCase() === "red"
}))

function manualFind(arr, func){
    for (let i=0; i<arr.length; i++){
        const isTrue = func(arr[i])

        // if true
        if (isTrue){
            return arr[i]
        }
    }

    return undefined
}
console.log(manualFind(carArr, function(value){
    return value.color.toLowerCase() === "red"
}))



// findIndex
console.log(carArr.findIndex(function(value){
    return value.color.toLowerCase() === "red"
}))

function manualFindIndex(arr, func){
    for (let i=0; i<arr.length; i++){
        const isTrue = func(arr[i])

        // if true
        if (isTrue){
            return i
        }
    }

    return -1
}
console.log(manualFindIndex(carArr, function(value){
    return value.color.toLowerCase() === "red"
}))



// indexOf
const numsArr = [1, 2, 3, 4, 1, 2, 3, 4]
console.log(numsArr.indexOf(3))



// lastIndexOf
console.log(numsArr.lastIndexOf(4))



// Destruction:
const fruits = ["Apple", "Banana", "Melon"]

// Rest operator
const [firstFruit, ...secondFruit] = fruits
console.log(firstFruit, secondFruit)

// We can also spread them:
console.log(firstFruit, ...secondFruit)