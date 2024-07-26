// API - application programming interface
// Api is way for some devices to share information with each other

// Restaurant example
// Restaurant has online system. We open it and choose pizza. Application sends info about pizza and address at restaurant api
// Restaurant api collects info and processes it automatically
// Then result is shown on our app

// API is set of rules which is used to share information accross two programs

// Using api, we send request to server. Server will work on request and return information

// Using fetch, we can send request on every server
// Then is method of promise object
// Then is first class citizen

const mainDiv = document.getElementById("container")

fetch("https://fakestoreapi.com/products")
    .then(res => res.json())
    .then(res => {
        res.forEach(element => {
            if (element.category !== "electronics" && element.category !== "jewelery"){
                const html = `
                <div>
                    <h2>${element.title}</h2>
                    <img src="${element.image}" />
                    <p>${element.price}$</p>
                </div>`
                mainDiv.insertAdjacentHTML("beforeend", html)
            }
            console.log(element)
        });
    })
    .catch(error => console.log(error))

// 15 დავალება fetch, then, catch, finally