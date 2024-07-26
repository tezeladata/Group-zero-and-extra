// <!-- beforebegin -->
// <p>
//   <!-- afterbegin -->
//   foo
//   <!-- beforeend -->
// </p>
// <!-- afterend -->

const mainDiv = document.querySelector(".products-div");
fetch('https://fakestoreapi.com/products')
    .then(res => res.json())
    .then(res => {
        res.forEach(element => {
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


// theory: http requests
// We can send requests on server using apis
// There are different types of requests, for example get request
// There is also post request, we request to send information to server
// Get - info to be returned to us, Post - info to be sent to server
// Get and Post are https requets

// async-await
// this method is easier syntax/way to work on asynchronous tasks
// async functions were created for better readibility
const fetchProducts = async () => {
    // When we have async functions, we use try-catch for error handling
    // If there is no error, try's code block will work and do it's job
    // If there is any error, that error is passed as an argument to catch

    try{
        // const res = fetch("https://fakestoreapi.com/products");
        // This is get request, because we are getting information. So we are working on asynchronous task.
        // Without await keyword, the result will be object which is pending.
        // We need to add await
        const res = await fetch("https://fakestoreapi.com/products");
        
        // Now we need to convert data
        const data = await res.json();
        //   We used await because it is asynchronous task

        for (const product of data){
            console.log(product)

            // We can also write html logic here
        }
    } catch(err){
        console.log(err)
    }
}
fetchProducts()

// We can give async function api parameter, so it will work on different apis

// Fetch can have more than 1 parameters.
// We can control how informations behavs


// We can send information to serverm such as jsonplaceholder
// stringify method turns js object into json object 