// 8 Datatypes:
// 1-string: 
let name="David";
let surname="Tezelashvili";
// 2-number:
let age=15;
let year=2024;
// 3-BigInt variables are used to store big integer values that are too big to be represented by a normal JavaScript Number:
let x=239487215091364593257;
let y=134892734923467293423847;
// 4-boolean:
let a=true;
let b=false;
// 5-undefined is a variable that has not been assigned a value is of type undefined:
let c;
console.log(c)
// 6-null is a special value that represents an empty or unknown value:
let d=null;
console.log(d)
// 7-symbol
// 8-object:
let myInfo={
    name: "David",
    surname: "Tezelashvili",
    age: 15,
    country: "Georgia"
}
// The object data type can contain:
// 1. An object
// 2. An array
// 3. A date

// Array object:
let cars=["BMW", "Mercedes", "Audi", "Porsche"]
// Date object:
let date=new Date("2024-01-02")

// JavaScript has dynamic types. This means that the same variable can be used to hold different data types:
let e=4;
e=20;
e="";
console.log(e)

// Strings are written with quotes. You can use single or double quotes:
let carName1="Bmw e34"
let carName2='Bmw e60'

// Extra large or extra small numbers can be written with scientific (exponential) notation:
let num1=50e5;
console.log(num1)

// JavaScript BigInt is a datatype that can be used to store integer values that are too big to be represented by a normal JavaScript Number.
let num2=BigInt(9574590374509137450913457019347);
console.log(num2)

// The typeof operator returns the type of a variable or an expression:
let A=true;
console.log(typeof A)

// In JavaScript, a variable without a value, has the value undefined. The type is also undefined.
let place;
console.log(place, typeof place)
// variable can be emptied:
let num4=23409;
num4=undefined;
console.log(num4)

// Empty values are not assosiacted with undefined ones:
let num5="";
console.log(num5, typeof num5)