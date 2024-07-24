const quote = document.getElementById("quote");
const author = document.getElementById("author");
const genButton = document.getElementById("generate-button");
const api_url = "https://api.quotable.io/random";

function getQuote(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            quote.innerHTML = data.content;
            author.innerHTML = data.author;
        })
        .catch(error => {
            quote.innerHTML = "An error occurred";
            author.innerHTML = "";
            console.error('Error fetching quote:', error);
        });
}

// When user opens the website, some quote has to be already generated:
getQuote(api_url);

genButton.addEventListener("click", () => {
    getQuote(api_url);
});

// For list
const saveButton = document.getElementById("save-button");
let quoteList = [];
const listDiv = document.getElementById("list-div");

saveButton.addEventListener("click", () => {
    const currentQuote = {
        author: author.textContent,
        content: quote.textContent
    };
    const isDuplicate = quoteList.some(savedQuote =>
        savedQuote.author === currentQuote.author && savedQuote.content === currentQuote.content
    );

    if (!isDuplicate) {
        // Add the current quote to the list
        quoteList.push(currentQuote);
        console.log("Quote saved:", currentQuote);

        // Create a new p element and append it to the list-div
        const newP = document.createElement("p");

        const authorSpan = document.createElement("span");
        authorSpan.textContent = currentQuote.author + ": ";

        newP.appendChild(authorSpan);
        newP.appendChild(document.createTextNode(currentQuote.content));

        listDiv.appendChild(newP);
    } else {
        const newDiv = document.getElementById("already-saved-div");
        newDiv.style.display = "block";
        setTimeout(() => {
            newDiv.style.display = "none";
        }, 1500);
    }
    console.log(quoteList);
});

// For list to appear:
const listButton = document.getElementById("list-button");
listButton.addEventListener("click", () => {
    listDiv.style.display = "block";
    setTimeout(() => {
        listDiv.style.display = "none";
    }, 7500);
});

// To clear whole list:
const clearButton = document.getElementById("clear-list");
clearButton.addEventListener("click", () => {
    quoteList = [];
    listDiv.innerHTML = '<div id="reset-div"><i class="fa-solid fa-circle-xmark" id="reset-button"></i></div>';
    listDiv.style.display = "none";
    attachResetButtonListener(); 
});

// Created function, because event was handled before the creation of element
function attachResetButtonListener() {
    const resetButton = document.getElementById("reset-button");
    if (resetButton) {
        resetButton.addEventListener("click", () => {
            listDiv.style.display = "none";
        });
    }
}

attachResetButtonListener();