//sticky navbar
window.addEventListener("scroll", function(){
    var header=document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
});

var menu=document.querySelector(".menu");
var menuBtn=document.querySelector('.menu-btn');
var closeBtn=document.querySelector(".close-btn");

menuBtn.addEventListener("click", () =>{
    menu.classList.add("active");
})

closeBtn.addEventListener("click", () =>{
    menu.classList.remove("active");
})


const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});