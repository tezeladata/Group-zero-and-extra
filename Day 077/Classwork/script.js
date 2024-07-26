// // Task 1
// const parentDiv = document.getElementById("parent");
// const childDiv = document.getElementById("child");
// const body = document.querySelector("body");

// window.addEventListener("click", function(){
//     console.log("window")
// })

// body.addEventListener("click", function(){
//     console.log("Body")
// }, true)

// parentDiv.addEventListener("click", function(){
//     console.log("Parent div")
// }, true)

// childDiv.addEventListener("click", function(){
//     console.log("Child div")
// }, true)

const mainDiv = document.getElementById("container");
const img = document.getElementById("slider");
const nextBtn = document.getElementById("next");
const prevBtn = document.getElementById("prev");

const photos = [
    "image.png", "image2.png", "image3.png"
];

let sliderCount = 0;

function mainColor(varName){
    if (varName % 2 == 0){
        mainDiv.style.backgroundColor = "green";
    } else {
        mainDiv.style.backgroundColor = "red";
    }
}

function changeBorder(varName, photo){
    if (varName % 2 == 0){
        photo.style.borderRadius = "50%";
    } else {
        photo.style.borderRadius = "20px";
    }
}

nextBtn.addEventListener("click", function(){
    sliderCount ++;

    if (sliderCount >= photos.length){
        sliderCount = 0;
    }

    mainColor(sliderCount)
    changeBorder(sliderCount, img)

    img.src = photos[sliderCount];
});

prevBtn.addEventListener("click", function(){
    sliderCount --;
    
    if (sliderCount < 0){
        sliderCount = photos.length - 1;
    }

    mainColor(sliderCount)
    changeBorder(sliderCount, img)

    img.src = photos[sliderCount];
});