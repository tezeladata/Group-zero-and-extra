// An asynchronous operation is one that allows the computer to “move on” to other tasks while waiting for the asynchronous operation to complete. Asynchronous programming means that time-consuming operations don’t have to bring everything else in our programs to a halt.

// Promises are objects that represent the eventual outcome of an asynchronous operation.
// Promise objects have 3 possible outcomes: pending, resolved, rejected

// Creating a promise object:
const inventory = {
    sunglasses: 1900,
    pants: 1088,
    bags: 1344
};


const promise = new Promise((resolve, reject) => {
    if (inventory.sunglasses > 1000){
        resolve("Good")
    } else{
        reject("Bad");
    }
});

console.log(promise)

// The executor function has two function parameters, usually referred to as the resolve() and reject() functions. The resolve() and reject() functions aren’t defined by the programmer. When the Promise constructor runs, JavaScript will pass its own resolve() and reject() functions into the executor function.


// The initial state of an asynchronous promise is pending, but we have a guarantee that it will settle. How do we tell the computer what should happen then? Promise objects come with an aptly named .then() method. It allows us to say, “I have a promise, when it settles, then here’s what I want to happen…”

// const prom = new Promise((resolve, reject) => {
//   resolve('Yay!');
// });

// const handleSuccess = (resolvedValue) => {
//   console.log(resolvedValue);
// };

// prom.then(handleSuccess); // Prints: 'Yay!'


let prom = new Promise((resolve, reject) => {
  let num = Math.random();
  if (num < .5 ){
    resolve('Yay!');
  } else {
    reject('Ohhh noooo!');
  }
});

const handleSuccess = (resolvedValue) => {
  console.log(resolvedValue);
};

const handleFailure = (rejectionReason) => {
  console.log(rejectionReason);
};

prom.then(handleSuccess, handleFailure);


// One way to write cleaner code is to follow a principle called separation of concerns. Separation of concerns means organizing code into distinct sections each handling a specific task. It enables us to quickly navigate our code and know where to look if something isn’t working.

// The .catch() function takes only one argument, onRejected. In the case of a rejected promise, this failure handler will be invoked with the reason for rejection. Using .catch() accomplishes the same thing as using a .then() with only a failure handler.


// process of chaining promises together is called composition. Promises are designed with composition in mind! Here’s a simple promise chain in code:
// firstPromiseFunction()
//     .then((firstResolveVal) => {
//     return secondPromiseFunction(firstResolveVal);
//     })
//     .then((secondResolveVal) => {
//     console.log(secondResolveVal);
//     });



// To maximize efficiency we should use concurrency, multiple asynchronous operations happening together. With promises, we can do this with the function Promise.all().

// If every promise in the argument array resolves, the single promise returned from Promise.all() will resolve with an array containing the resolve value from each promise in the argument array.
// If any promise from the argument array rejects, the single promise returned from Promise.all() will immediately reject with the reason that promise rejected. This behavior is sometimes referred to as failing fast.



// Homework:
// 1
const promise1 = new Promise((resolve) => {resolve("Hello, world!")})
promise1.then((result) => console.log(result))

// 2
const promise2 = new Promise((resolve) => {
    setTimeout(() => {
        resolve("Resolved after 2 seconds")
    }, 2000)
})
promise2.then((result) => console.log(result))

// 3
const promise3 = new Promise((resolve) => resolve("First"));
const promise4 = promise3.then((result) => result + " + Second");
promise4.then(finalRes => console.log(finalRes))

// 4
const promise5 = new Promise((resolve) => resolve(4));
const promise6 = promise5.then((result) => result * 2);
const promise7 = promise6.then((result) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(result * 10);
        }, 1000);
    });
});
promise7.then(finalRes => console.log(finalRes)); 

// 5
const promise8 = new Promise((_, reject) => {
    setTimeout(() => {
        reject("Rejected")
    }, 1000)
})
promise8
    .then((finalRes) => console.log(finalRes))
    .catch((finalRes) => console.log(finalRes))

// 6
const delayer = (() => {
    setTimeout(() => {
        console.log(1)
    }, 1000)

    setTimeout(() => {
        console.log(2)
    }, 2000)

    setTimeout(() => {
        console.log(3)
    }, 3000)
})

delayer()

// 7
function delay(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

delay(1000)
    .then(() => {
        console.log("One");
        return delay(1000); 
    })
    .then(() => {
        console.log("Two");
        return delay(1000); 
    })
    .then(() => {
        console.log("Three");
    });

// 8
const promise9 = new Promise((resolve, reject) => {
    const dec = Math.random() > .5;

    if (dec){
        resolve("Congrats")
    } else{
        reject("Maybe next time?")
    }
})
promise9
    .then((res) => console.log(res))
    .catch(res => console.log(res))

// 9
const promise10 = new Promise((resolve) => {
    setTimeout(() => {
        resolve("Good job")
    }, 5000)
})
promise10.then((res) => console.log(`After 5 seconds, we have message ready for you: ${res}`))

// 10
const promise11 = new Promise((resolve) => {
    setTimeout(() => {
        resolve("Start");
    }, 1000); 
});

promise11
    .then((result) => {
        console.log(result);
        return `${result} -> Step 1`;  
    })
    .then((result) => {
        console.log(result); 
        return `${result} -> Step 2`;   
    })
    .then((result) => {
        console.log(result); 
        return `${result} -> Step 3`;   
    })
    .then((result) => {
        console.log(result); 
    });