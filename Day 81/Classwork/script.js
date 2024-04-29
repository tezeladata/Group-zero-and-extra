// const names = [];

// for (let i = 0; i < nameObj.length; i++){
//     names.push(nameObj[i].name);
// }

// console.log(names);

// let nameObj = [
//     person1 = {
//         name: "David",
//         age: 16
//     },
//     person2 = {
//         name: "Andria",
//         age: 9
//     },
//     person3 = {
//         name: "Gio",
//         age: 15
//     }
// ];

// const manualMap = function(arr, subfunc){
//     const result = [];

//     for (let i = 0; i<arr.length; i++){
//         result.push(subfunc(arr[i]))
//     }

//     return result
// }

// const names = manualMap(nameObj, function(obj){
//     return obj.name.toUpperCase()
// })

// console.log(names)


// Task2:
const manualMap = function(arr, subFunc){
    const resArr = []

    for (let i = 0; i<arr.length; i++){
        resArr.push(subFunc(arr[i]))
    }

    return resArr
}

const degree = manualMap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], function(item){
    return item**2
})

console.log(degree)


// Task 3:
const students = [
    {
        name: "David",
        grade: 80
    },

    {
        name: "Andria",
        grade: 55
    },

    {
        name: "Tobi",
        grade: 65
    }
]

const manualFilter = function(arr, subFunc){
    const newArray = [];

    for (let i=0; i<arr.length; i++){
        if (subFunc(arr[i])){
            newArray.push(arr[i].name)
        }
    }

    return newArray;
}

console.log(manualFilter(students, function(obj){
    return obj.grade >= 60
}))


// Task 4
const manualDegree = function(arr, subFunc){
    const resArr = [];

    for (let i=0; i<arr.length; i++){
        resArr.push(subFunc(arr[i], i))
    }

    return resArr
}

const updatedList = manualDegree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], function(num, ind){
    if (ind%2==0){
        return num**2
    } else{
        return num**3
    }
})

console.log(updatedList)