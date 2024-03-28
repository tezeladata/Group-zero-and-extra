// Hw1
let counter = 0;
let hw1Div = document.getElementById("hw1");
let hw1P = document.getElementById("p1");
let hw1Button = document.getElementById("button1");

hw1Button.addEventListener("click", function(){
    counter++;
    if (hw1Div.style.backgroundColor === "green"){
        hw1Div.style.backgroundColor = "blue";
    } else {
        hw1Div.style.backgroundColor = "green";
    }

    if (hw1P.style.color === "blue"){
        hw1P.style.color = "green";
    } else {
        hw1P.style.color = "blue";
    }
    hw1P.innerHTML = counter;
});


// Hw2
let hw2Button = document.getElementById("button2");
let hw2Image = document.getElementById("img1")

hw2Button.addEventListener("click", function(){
    if (hw2Image.src.includes('GOA-background.png')){
        hw2Image.src = 'images/GOA-Mtskheta.png';
    } else {
        hw2Image.src = 'images/GOA-background.png';
    }
});


// Hw3
function randomNum(){
    return Math.ceil(Math.random() * 9);
}
let hw3Button = document.getElementById("button3");
let hw3P1 = document.getElementById("hw3P1");
let hw3P2 = document.getElementById("hw3P2");
let hw3P3 = document.getElementById("hw3P3");
let hw3P4 = document.getElementById("hw3P4");
let hw3P5 = document.getElementById("hw3P5");

hw3Button.addEventListener("click", function(){
    hw3P1.innerHTML = randomNum();
    hw3P2.innerHTML = randomNum();
    hw3P3.innerHTML = randomNum();
    hw3P4.innerHTML = randomNum();
    hw3P5.innerHTML = randomNum();
})


// Hw4
let hw4Div = document.getElementById("hw4");
let hw4Anchor = document.getElementById("a1");
let hw4Button = document.getElementById("button4");

hw4Button.addEventListener("click", function(){
    if (hw4Anchor.href == 'https://www.youtube.com/@Goal_Oriented_Academy__GOA'){
        hw4Anchor.href = 'https://www.facebook.com/nika11keshelava';
        hw4Anchor.innerHTML = "Goa Facebook";
    } else {
        hw4Anchor.href = 'https://www.youtube.com/@Goal_Oriented_Academy__GOA';
        hw4Anchor.innerHTML = "Goa Youtube"
    }

    if (hw4Div.style.backgroundColor === "green"){
        hw4Div.style.backgroundColor = "blue";
    } else {
        hw4Div.style.backgroundColor = "green";
    }
})


// Hw5
let labels = document.getElementsByTagName("label");
for (let i = 0; i < labels.length; i++) {
    labels[i].style.borderColor = 'blue';
}