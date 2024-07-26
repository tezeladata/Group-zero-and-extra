// slicing
let fullName="hello world";
let firstName;
let lastName;

// firstName=fullName.slice(0, 6)
// lastName=fullName.slice(6);

firstName=fullName.slice(0, fullName.indexOf(" "));
lastName=fullName.slice(fullName.indexOf(" ")+1);
console.log(firstName);
console.log(lastName);
console.log(lastName, firstName);

//Method chaining
let name1="    andria      ";
let letter=name1.trim().charAt(0).toUpperCase();
console.log(letter);



//if statements
// let age = window.prompt("Enter age");
// age=Number(age)
// if (age >= 18) {
//     console.log("Adult");
// } 
// else if(age<0){
//     console.log("Incorrect age")
// }
// else {
//     console.log("Child");
// }

let online=false;
if (online){
    console.log("You are online")
}
else {
    console.log("You are offline")
}