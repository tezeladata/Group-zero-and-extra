let intro=document.getElementById("label1")
let name;
let age;
document.getElementById("button1").onclick=function(){
    name=document.getElementById("input1").value;
    age=document.getElementById("input2").value;
    intro.textContent="Hallo";
    document.getElementById("label2").innerHTML="Your name is " + name + " and you are " + age + " years old.";
}
let SecondButton=document.getElementById("button2");
const p=document.getElementById("p1")
let Iteration=0;
SecondButton.addEventListener("click", function(){
    Iteration+=1;
    p.textContent=Iteration;
})

let place=prompt("Where do you live?");
console.log(place)
//Add event listener-მოვლენის მსმენელის დამატება