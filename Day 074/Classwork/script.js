const button = document.getElementById("button1");
let count = 0
const paragraph = document.getElementById("p1");

function clicker(){
    count += 1
    paragraph.textContent = count

    if (count == 10){
        button.removeEventListener("click", clicker)
        paragraph.textContent = "The end"
    }
}

button.addEventListener("click", clicker)