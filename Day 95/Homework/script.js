// // 1
// fetch('https://fakestoreapi.com/products')
//     .then(res => console.log(res))

// // 3
// // A Promise is an object used for handling asynchronous operations in JavaScript. 
// // It represents the eventual completion (or failure) of an asynchronous task and its resulting value.
// // When we don't know how long a task will take, using a Promise can help manage the result of that task.
// //
// // A Promise constructor takes a single function parameter, called the executor function, 
// // which itself takes two parameters: resolve and reject. 
// // 
// // - resolve: This function is called when the asynchronous task completes successfully. 
// //   It allows you to pass a value that will be used by the promise's `then` method.
// // - reject: This function is called when the asynchronous task fails. 
// //   It allows you to pass a reason (usually an error) that will be used by the promise's `catch` method.

// // 3.5
// // Fetch API comes with the fetch() method, which is used to fetch data from different sources.
// // API for get requests
// fetch("https://jsonplaceholder.typicode.com/todos/1")
//     .then(res => res.json())
//     .then(d => { console.log(d)})

// // 4
// // The insertAdjacentHTML() method inserts HTML code into a specified position.
// const h1 = document.getElementById("main-heading");
// const html = '<div><p>This is paragraph</p><i><u>This is italic and underlined text</u></i></div>'
// setTimeout(() => {
//     h1.insertAdjacentHTML("afterend", html)
// }, 2000)

const mainDiv = document.querySelector(".products-div");

fetch('https://fakestoreapi.com/products')
    .then(res => res.json())
    .then(res => {
        res.forEach(element => {
            console.log(element);
            if (element.category === "jewelery" || element.category === "men's clothing" || element.category === "women's clothing"){
                const newDiv = `
                <div>
                    <h3>${element.title}</h3>
                    <img src="${element.image}" alt="${element.title}" />
                    <p>Price: ${parseInt(element.price*0.8)}$ <span>${element.price}$</span></p>
                </div>`;
                mainDiv.insertAdjacentHTML("beforeend", newDiv);
            }
        });
    });

