// asynchronous js


// JS is single threaded
// When 2 functions are run in js, asynchronisation is used

// Promise is an object which shows outcome of asynchronous operation
// First state of promise is pending
// Second state is fullfiled
// Third state is rejected

// Possible outcomes of promise are reject and resolve

// Creating promise object:

// const inventory = {
//     sunglasses: 1900,
//     pants: 1088,
//     bags: 1344
// }

// const executor = ((resolve, reject) => {
//     if (inventory.sunglasses > 0) resolve("Sunglasses order processed")
//     else reject("That item is sold out")
// });

// const orderSunglasses = () => {
//     return new Promise(executor)
// }

// const orderPromise = new Promise(executor);

// console.log(orderPromise)


// const myFirstPromise = new Promise((resolve, reject) => {
//     if (true){
//         resolve("Resolved")
//     } else{
//         reject("Rejected")
//     }
// })

// console.log(myFirstPromise)



// Example of asynchronisation
// console.log("Start");

// setTimeout(() => {
//     console.log("Opaa")
// }, 1000);

// console.log("End");


const pantsCount = 100;

const executerFunction = (resolve, reject) => {
    if (pantsCount > 0){
        setTimeout(() => {resolve("You can buy")}, 1000)
    } else{
        setTimeout(() => {reject("You cannot buy")}, 1000)
    }
}

const orderPant = () => {
    // returns promise
    return new Promise(executerFunction)
}

// // Then is used after execution of resolve / reject
// orderPant().then((resolved) => {
//     // "You can buy" was returned to then
//     console.log(resolved)
// }, (rejected) => {
//     // "You cannot buy" was returned to then
//     console.log(rejected)
// })


// orderPant()
//     .then((resolved) => {
//         console.log(resolved)
//     })
//     .catch((rejected) => {
//         console.log(rejected)
//     })


// Fetch function send request to server
fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json()) // json method turns info into js real object.
      .then(json => console.log(json))

// JSON is format to send and receive info in internet
// It takes time to turn js info into object, so it's asynchronous task


// 10 დავალება promises, setTimeout, then, catch.
// ჩანაწერის ყურება
// https://www.codecademy.com/learn/asynchronous-javascript ამ კურსის გავლა