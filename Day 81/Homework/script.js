// Task1:
const manualMap = function(array, subFunc){
    const resArr = []

    for (let i=0; i<array.length; i++){
        resArr.push(subFunc(array[i]))
    }

    return resArr
}

const secondDegree = function(element){
    return element**2
}

console.log(manualMap([1, 2, 3, 4, 5], secondDegree))


// Task2:
const manualFilter = function(array, subFunc){
    const resArr = []

    for (let i=0; i<array.length; i++){

        if (subFunc(array[i])){
            resArr.push(array[i] ** 3)
        }

    }

    return resArr
}

console.log(manualFilter([1, 21, 2, 22, 3, 23, 4, 24, 5, 25], function(element){
    return element >= 20
}))


// Task3:
const namesArr = ["david", "luka", "david", "vano"]
console.log(namesArr.map((element) => element.toUpperCase()))
// or:
console.log(namesArr.map(function(element){
    return element.toUpperCase()
}))


// Task4:
const namesArr2 = ["goal", "Orientadze", "David", "hello world"]
console.log(namesArr2.filter(function(element){
    return element[0] == element[0].toUpperCase() && element.length <= 5
}))


// Task5:
const numsArr = [10, 20, 30, 40, 45, 55, 65, 80, 90, 100]
console.log(numsArr.filter(function(element){
    return element > 20 && element%5 == 0
}))