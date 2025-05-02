let myName = "David";
console.log(myName);

// data type - any
let age;

age = 10;
console.log(age);

age = "Seventeen";
console.log(age);

// type annotation with "any"
let academy : string;

academy = "GOA";
console.log(academy);

// Error
// academy = 10;
// console.log(academy);

const logInfo = (fullname: string, age: number, academy: string) => {
    console.log(`Fullname: ${fullname}\nAge: ${age}\nAcademy: ${academy}`);
}
logInfo("David Tezelashvili", 17, "GOA");

// Optional parameter
const greet = (name? : string) => {
    console.log(`Hello ${name}`);
};
greet("David");
greet();

// Default parameters
const logNumber = (num = 10) => {
    console.log(`Number: ${num}!`);
    return `Number: ${num}!`
}
logNumber(20);
logNumber(undefined);
logNumber();

// return types
const res1 : string = logNumber();
console.log(res1);