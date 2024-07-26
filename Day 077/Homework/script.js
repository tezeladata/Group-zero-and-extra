const div1 = document.getElementById("chad1-div");
const div2 = document.getElementById("chad2-div");
const div3 = document.getElementById("chad3-div");

const rightArrow = document.getElementById("arrow-right");
const leftArrow = document.getElementById("arrow-left");

const allDivs = [div1, div2, div3];

let sliderCount = 0;

rightArrow.addEventListener("click", function(){
    allDivs[sliderCount].style.display = "none"; 

    sliderCount = (sliderCount + 1) % allDivs.length; 

    allDivs[sliderCount].style.display = "flex"; 
});

leftArrow.addEventListener("click", function(){
    allDivs[sliderCount].style.display = "none"; 

    sliderCount = (sliderCount - 1 + allDivs.length) % allDivs.length; 

    allDivs[sliderCount].style.display = "flex"; 
});