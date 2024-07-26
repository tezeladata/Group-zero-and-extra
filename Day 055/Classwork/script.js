let count=0;
document.getElementById("button1").onclick=function(){
    count-=1;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button2").onclick=function(){
    count-=5;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button3").onclick=function(){
    count-=10;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button4").onclick=function(){
    count-=20;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button5").onclick=function(){
    count-=50;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button6").onclick=function(){
    count-=100;
    document.getElementById("label1").innerHTML=count;
}


document.getElementById("button7").onclick=function(){
    count+=1;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button8").onclick=function(){
    count+=5;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button9").onclick=function(){
    count+=10;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button10").onclick=function(){
    count+=20;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button11").onclick=function(){
    count+=50;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button12").onclick=function(){
    count+=100;
    document.getElementById("label1").innerHTML=count;
}
document.getElementById("button13").onclick=function(){
    count=0;
    document.getElementById("label1").innerHTML=count;
}



// Booleans have two possible meanings: true or false
// && is and
// || is or
// ! is not



// let name="David";
// console.log(typeof name);

// let budget=prompt("Enter budget");
// budget=Number(budget);
// console.log(typeof budget);

// let age=Number(prompt("Enter your age:"));
// console.log(typeof age);

// 1
let a=8%2;
let b=Math.PI;
let c=a>b;
let d=(a===b);
console.log(c||d);
console.log(d||true);

// 2
console.log(Number("134234"));
console.log(Number(1===1));

// 3
let num1=Number(prompt("Enter First number: "));
let num2=Number(prompt("Enter Second number: "));
let sum=num1+num2;
console.log(sum)