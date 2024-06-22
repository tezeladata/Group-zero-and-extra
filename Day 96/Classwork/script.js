// 1
const promise1 = new Promise((resolve) => {
    setTimeout(() => resolve("Hello, World!"), 2000)
})
promise1.then(res => console.log(res))

// 2
const promise2 = new Promise((_, reject) => {
    setTimeout(() => reject("Something went wrong!"), 3000)
})
promise2
    .then((res) => console.log(res))
    .catch((res) => console.log(res))

// 3
const promise3 = new Promise(resolve => resolve(5))
const promise4 = new Promise(resolve => resolve(10))
promise3
    .then(res0 => {
        return promise4.then(res1 => {
            console.log(res0 + res1)
        })
    })

// 4
const promise5 = new Promise(resolve => resolve([1, 2, 3, 4, 5]))
promise5
    .then(res => {
        return res.forEach(element => {
            console.log(element)
        });
    })

// 5
const promise6 = new Promise(resolve => resolve("Hello World!"));
promise6
    .then(res => res.toUpperCase())
    .then(res => console.log(res.split("").filter(word => word.charCodeAt(0) > 75).reverse().join("")))

// 6
fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(res => res.json())
    .then(res => console.log(res))
    .catch(res => console.log("Something went wrong!"))

// 7
const promise7 = new Promise(resolve => resolve("Good "))
const promise8 = new Promise(resolve => resolve("One!"))
promise7
    .then(res0 => {
        console.log(res0)
        promise8.then(res1 => console.log(res1))
    })

// 8
const promise9 = new Promise(resolve => {
    setTimeout(() => {
        resolve(new Date())
    }, 1000)
})
promise9
    .then(res => console.log(res))

// 9
const promise10 = new Promise((resolve, reject) =>{
    let result = Math.random();

    if (result > .5){
        resolve(`Congrats, your number is ${result}`)
    } else{
        reject(`Maybe next time? Your number is ${result}`)
    }
})
promise10
    .then(res => console.log(res))
    .catch(res => console.log(res))

// 10
const promise11 = new Promise(resolve => {
    setTimeout(() => {
        resolve("John ")
    }, 4000)
})
promise11
    .then(res => {
        console.log(res)

        return new Promise(resolve => {
            setTimeout(() => {
                resolve("Johns")
            }, 2000)
        })
    })
    .then(modified => console.log(modified))

// 11
function sayJoke(apiUrl, jokeId) {
    return fetch(apiUrl)
        .then(response => response.json())
        .then(({ jokes }) => {
            if (jokes) {
                const joke = jokes.find(joke => joke.id === jokeId);
                if (joke) {
                    return {
                        saySetup: () => joke.setup,
                        sayPunchLine: () => joke.punchLine
                    };
                } else {
                    return Promise.reject(new Error(`No jokes found id: ${jokeId}`));
                }
            } else {
                return Promise.reject(new Error(`No jokes at url: ${apiUrl}`));
            }
        });
}

// CroCoder
// Promises in JavaScript are an essential tool for managing asynchronous operations with ease and clarity. They assure that a certain piece of work will be done at a later time. This is incredibly useful for tasks that need to wait for something else to finish, like fetching data from a website.
// Instead of juggling multiple callbacks, which can quickly become unwieldy and hard to follow, promises allow developers to chain operations in a linear and readable manner. This is done through .then() for successful operations, and .catch() for handling errors. This not only enhances code readability but also streamlines error handling, making the code more robust and maintainable.


// Create a JavaScript Promise that, after a delay of 2 seconds, either resolves with the message "Hello World" or rejects with the error message "Error occurred".
const croPromise1 = new Promise((resolve, reject) => {
    let result = Math.random() > .5;

    if (result) resolve("Message");
    else reject("Error")
})
croPromise1
    .then((message) => {
        console.log(message);
    })
    .catch((error) => {
        console.error(error);
    });


// Input a number, double it, increase it by 10, and then multiply by 3.
// Each operation should be in a separate Promise and then chained together.
const num1 = 5;

const croPromise2 = value => new Promise(resolve => resolve(value * 2));
const croPromise3 = value => new Promise(resolve => resolve(value + 10));
const croPromise4 = value => new Promise(resolve => resolve(value * 3));

croPromise2(num1)
    .then(croPromise3)
    .then(croPromise4)
    .then(result => console.log(result))
    .catch(error => console.error('Error:', error));


// Using fetchSimulator simulate fetching data from three different URLs in parallel.
// Each "fetch" will be represented by a Promise that resolves after a delay taken from the delays array.
// Use Promise.all to wait for all these Promises to resolve and then process the results.
const delays = [800, 1200, 1000];

const fetchSimulator = (url, delay) => {
    return new Promise(resolve => setTimeout(() => resolve(`Data from ${url}`), delay));
};

Promise.all([fetchSimulator('https://jsonplaceholder.typicode.com/todos/1', delays[0]), fetchSimulator('https://jsonplaceholder.typicode.com/todos/1', delays[1]), fetchSimulator('https://jsonplaceholder.typicode.com/todos/1', delays[2])])
    .then(allRes => console.log(allRes))


// Using fetchSimulator simulate fetching data from three different URLs with a twist.
// Each "fetch" will be represented by a Promise that resolves after a delay taken from the delays array.
// Use Promise.race to get the fastest response!
const delays2 = [800, 1200, 1000];

const fetchSimulator2 = (url, delay) => {
    return new Promise(resolve => setTimeout(() => resolve(`Data from ${url}`), delay));
};

Promise.race([fetchSimulator2('https://jsonplaceholder.typicode.com/todos/1', delays2[0]), fetchSimulator2('https://jsonplaceholder.typicode.com/todos/1', delays2[1]), fetchSimulator2('https://jsonplaceholder.typicode.com/todos/1', delays2[2])])
    .then(res => console.log(res))


// Create a Promise that simulates a data fetching operation with a delay. Introduce a cancellation token that can be used to cancel the Promise before it resolves.
// If the operation is cancelled, the Promise should reject with a "Cancelled" message; otherwise, it should resolve normally.
// Cancel it!
function createCancellationToken() {
    let cancel;
    const token = new Promise((_, reject) => {
        cancel = () => reject(new Error('Cancelled'));
    });
    return { token, cancel };
}

function fetchData(cancellationToken) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Data fetched");
        }, 3000);

        cancellationToken.token.catch(() => {
            reject(new Error('Operation cancelled'));
        });
    });
}

const { token, cancel } = createCancellationToken();

const fetchPromise = fetchData({ token });

setTimeout(() => {
    cancel();
}, 1500);

fetchPromise
    .then(data => console.log(data))
    .catch(error => console.error(error.message));