const ul = document.getElementById("nav");
const main = document.querySelector("main");

const home = `
    <div id="home">
        <h1>Home Page</h1>
        <p>Welcome to the home page.</p>
        <button>Click me</button>
    </div>
`;

const about = `
    <div id="about">
        <h1>About Page</h1>
        <p>Welcome to the about page.</p>
        <button>Click me</button>
    </div>
`

ul.addEventListener("click", event => {
    const page = event.target.textContent;

    if (page === "home"){
        main.innerHTML = home;
    } else {
        main.innerHTML = about;
    }
})