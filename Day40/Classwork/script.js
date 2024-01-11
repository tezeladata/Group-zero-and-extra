// console.log("I Like Pizza");
// console.log("Hello World");

// window.alert("Hello World")

//this is a comment

/*
multi-line
comment
*/

//We use var, let or const to declare a variable
//declaring:
// let age;
// //assigning:
// age=21;  //number
// age+=1;
// console.log("You are", age, "years old.");

// //or:
// let FirstName="David";  //string
// console.log("Hello", FirstName);

// let role=false;  //boolean
// console.log(role);
// ;
// document.getElementById("p1").innerHTML = "Hello " + FirstName;
// document.getElementById("p2").innerHTML = "You are " + age + " years old";
// document.getElementById("p3").innerHTML = "You are student: " + role;

/*arithmetic expression is a combination of...
operands (values, variables, etc.)
operators (h
that can be evaluated to a value
*/

// let money=20;
// money*=5
// console.log(money);
// let remainder=money%3;
// console.log(remainder)

// let result=1+2*(4/2);
// console.log(result);

//inputs
// let name=window.prompt("What is your name?");
// console.log("His name is ", name);

// let UserAge;

// document.getElementById("button1").onclick=function(){
//     UserAge=document.getElementById("input1").value;
//     console.log(UserAge);
//     document.getElementById("label1").innerHTML="You are "+ UserAge + " yearls old.";
// }

// let UserGender;

// document.getElementById("button2").onclick=function(){
//     UserGender=document.getElementById("input2").value;
//     console.log("You are", UserGender)
//     document.getElementById("label2").innerHTML="You are "  + UserGender;
// }


// //type conversion
// let age=window.prompt("How old are you?");
// //Checking data type
// console.log(typeof age);
// age=Number(age);
// age+=1;
// console.log("Happy birthday, you are", age, "years old!")
// console.log(typeof age);

// console.log(Number("3.14"), typeof Number("3.14"))
// console.log(3==3);

// let a=("Pizza");
// console.log((typeof a)==Number);
// let b=Number("Hello");  //Nan- not a number
// console.log(b);



// const = a variable that can't be changed
// Circumference:
const PI=3.14159;  //pi is always 3.14159... so we use const we use uppercase letters with constants
let radius;
let circumference;

// PI=2423423; we cannot change constant value

document.getElementById("button1").onclick=function(){
    radius=document.getElementById("input1").value;
    radius=Number(radius);
    document.getElementById("label1").innerHTML="Radius is " + radius;
    circumference=2*PI*radius;
    document.getElementById("label2").innerHTML="Circumference of that circle is: " + circumference;
}
//const cannot be changed, it is better to use when we want variable to always be same

//Using MATH

let x=125.23423423;
console.log(x);
x=Math.round(x);
console.log(x);
let y=3.99;
y=Math.floor(y);  //floor always rounds down
console.log(y);
let z=5.1;
z=Math.ceil(z)  //ceil is short version of ceiling and it always rounds up a number
console.log(z);

//powers:
let a=2;
a=Math.pow(a, 5);
//     base, exponent
console.log(a)

//square root:
let b=4;
b=Math.sqrt(b);
console.log(b);