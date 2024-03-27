// Date
const newDate = new Date();

const day = newDate.getDay().toString();
const month = (newDate.getMonth() + 1).toString();
const year = newDate.getFullYear().toString();
const finalDay = `${day}.${month}.${year}`;

const htmlDate = document.getElementById("date-span");
htmlDate.innerHTML = finalDay;


// Form
const form = document.getElementById("form1");
const mainDiv = document.querySelector(".container3");

const randomColors = ["#F9D42B", "#FE465E", "#19A9F2", "#38C3AC", "#9D49DF", "#FF94B0", "#FD8054"];

function getRandomColor() {
    const randomNum = Math.floor(Math.random() * randomColors.length);
    return randomColors[randomNum];
}

form.addEventListener("submit", function(e){
    e.preventDefault();
    
    const divNode = document.createElement("div");

    const h2Node = document.createElement("h2");
    const pNode = document.createElement("p");
    const cont3Part1 = document.createElement("div");
    const removeI = document.createElement("i");
    const cont3Part2 = document.createElement("div");
    const editI = document.createElement("i");

    const heading = form.elements.name.value.trim();
    const paragraph = form.elements.description.value.trim();

    h2Node.textContent = heading;
    pNode.textContent = paragraph;

    removeI.classList.add("fa-solid", "fa-xmark");
    removeI.setAttribute("id", "remove-i");

    editI.classList.add("fa-solid", "fa-pen-to-square");
    editI.setAttribute("id", "edit-i");

    cont3Part1.appendChild(h2Node);
    cont3Part1.appendChild(removeI);
    cont3Part1.classList.add("cont3-part1");

    cont3Part2.appendChild(editI);
    cont3Part2.classList.add("cont3-part2");

    divNode.appendChild(cont3Part1);
    divNode.appendChild(pNode);
    divNode.appendChild(cont3Part2);
    divNode.style.backgroundColor = getRandomColor();

    mainDiv.appendChild(divNode);

    form.elements.name.value = "";
    form.elements.description.value = "";
});

// Div element functions
const parentDiv = document.querySelector('.container3');

parentDiv.addEventListener("click", function(event) {
    if (event.target && event.target.id === "remove-i") {
        const parentDiv = event.target.closest(".container3 > div");
        if (parentDiv) {
            parentDiv.remove();
        }
    } else if(event.target && event.target.id === "edit-i") {
        const parentDiv = event.target.closest(".container3 > div");
        if (parentDiv) {
            const newHeading = prompt("Enter task name: ");
            const newParagraph = prompt("Enter task description:");
            const h2Element = parentDiv.querySelector("h2");
            const pElement = parentDiv.querySelector("p");
            if (h2Element && pElement && newHeading !== null && newParagraph !== null) {
                h2Element.textContent = newHeading;
                pElement.textContent = newParagraph;
            }
        }
    }
});