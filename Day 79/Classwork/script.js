// // Task 1
// function manualFilter(innerFunc, collection){
//     let resArr = [];
//     for (let i = 0; i < collection.length; i++){
//         if (innerFunc(collection[i])){
//             resArr.push(collection[i])
//         } else{
//             resArr.push(`${collection[i]} is not prime!`)
//         }
//     }
//     return resArr
// }

// function childFilter(element){
//     if (typeof(element) === 'number'){
//         return isPrime(element);
//     }
//     return false;
// }

// function isPrime(numb){
//     if (numb == 1){
//         return false;
//     } else if (numb == 2){
//         return true;
//     } else{
//         let isPrime = true;

//         for (let i=2; i<numb; i++){
//             if (numb % i == 0){
//                 isPrime = false;
//                 break;
//             }
//         }

//         if (isPrime){
//             return true;
//         } else{
//             return false;
//         }
//     }
// }

// console.log(manualFilter(childFilter, [10, 1, 9, 2, 8, 3, 7, 4, 5]));


// // Task 2
// function manualMap(innerFunc, collection){
//     let resArr = []

//     for (let i = 0; i < collection.length; i++){
//         resArr.push(innerFunc(collection[i]))
//     }
//     return resArr
// }

// function childMap(element){
//     return element**2
// }

// console.log(manualMap(childMap, [10, 1, 9, 2, 8, 3, 7, 4, 5]))


// console.log([1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map(function(numb){
//     return numb**2
// }))


// console.log([1, 2, 3, 4, 5, 6, 7, 8, 9, 10].filter(function(numb){
//     return numb%2 == 0
// }))


// Task 3:
console.log([1, "3d", true, 4.14, 2, 3, 5].filter(function(element){
    return typeof(element) === "number" && element%1==0
}))

// Task 4:
console.log([1, 2, 4, 5, 3, 2, 1, 7, 5].map(function(element, index){
    if (index %2 ==0){
        return element*2
    }
    return element
}))