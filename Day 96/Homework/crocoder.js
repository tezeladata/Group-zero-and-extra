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