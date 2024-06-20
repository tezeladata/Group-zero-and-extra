// Server is just computer which is always turned on

// Shared server is server which is based on super strong computer and many websites are hosted on them

// Dedicated server is when server is dedicated on only one site and is super expensive

// We can open ports on our servers

// Server ips were so hard to remember so they created domains

// DNS is domain name system

// მოთხოვნა - http request

// get request, post request, put request, delete request


// Fetch is used to send requests to servers

const productsContainer = document.querySelector(".products")
const p = document.getElementById("title");
const img = document.getElementById("product-img");
const price = document.getElementById("price");

fetch('https://fakestoreapi.com/products/1')
    .then(res => res.json())
    .then(data => {
        p.textContent = data.title;
        img.src = data.image;
        price.textContent = `$${data.price}`; 
    })
    .catch(err => {
        console.error('Error fetching data:', err);
    });