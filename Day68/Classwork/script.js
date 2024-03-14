// const p = document.getElementById("p1");
// p.innerHTML="<i> David </i>"
// console.log(p)

// const elements=document.getElementsByClassName("my-p")
// console.log(elements)
// elements[1].innerHTML = "Hello World!"

// const allP = document.getElementsByTagName("p")
// allP[2].innerHTML = "Hello World!"


// // მივწვდით ელემენტს
// // We got the div
// const div = document.getElementById("my-div");

// // დააბრუნებს შვილობილი ელემენტების რაოდენობას
// // Returning the count of child elements
// console.log(div.childElementCount);

// // დააბრუნებს შვილობილ ელემენტებს
// // Returning the child elements
// console.log(div.children);

// // დააბრუნებს დივის შემდეგ ელემენტს რაც html-ში გვაქვს
// // Returning the next element after div
// console.log(div.nextElementSibling);

// // დააბრუნებს დივის წინა ელემენტს რაც html-ში გვაქვს
// // Returning the previous element before div
// console.log(div.previousElementSibling);

// // დააბრუნებს დივის მშობელ ელემენტს
// // Returning parent element
// console.log(div.parentElement);


// // Styling
// const p = document.getElementById("p1");
// p.style.fontSize = "124";


// hw1
const hw1Div = document.getElementById("hw1");
const button = document.getElementById("button1");
hw1Div.style.flexDirection = "row";
button.addEventListener("click", function(){
    const flexDirection = hw1Div.style.flexDirection;
    if (flexDirection == "row"){
        hw1Div.style.flexDirection = "column"
    } else{
        hw1Div.style.flexDirection = "row"
    }
})

// hw2
const hw2P = document.getElementById("hw2-p");
hw2P.parentElement.style.backgroundColor = "Green";

// hw3
const div = document.getElementById("hw3");
// Count of child elements
console.log(div.childElementCount);
// Parent element
console.log(div.parentElement);
// Collection of child elements
console.log(div.children);
// Element after div
console.log(div.nextElementSibling);
// Previous element
console.log(div.previousSibling);

// hw4
const hw4P = document.getElementsByClassName("hw4-p");
for (let i=0; i<hw4P.length; i++){
    hw4P[i].innerHTML = "David Tezelashvili"
}