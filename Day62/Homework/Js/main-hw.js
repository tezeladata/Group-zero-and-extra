// Creating an object:
const person={
    name: "David",
    age: 15,
    city: "Tbilisi"
}

// Accessing object properties:
console.log(person.name)

// Modifying an object property:
person.age=16;
console.log(person.age)

// Adding a new property
person.country="Georgia";
console.log(person.country)

// Adding a method
person.greet=function(personName){
    console.log(`Welcome ${personName}, nice to meet you!`)
}
person.greet("Nick")

// Object comparison:
const person1={
    name: "Alex",
    surname: "Smith",
    age: 40
}

const person2={
    name: "Alex",
    surname: "Smith",
    age: 40
}

console.log(person1 === person2)
// No matter the similarity, objects are always unique and cannot be same with any other one.

// Nested objects
const school1={
    name: "Tbilisi School",
    students: [
        {name: "Jennifer", surname: "Ramirez", age: 16},
        {name: "Marcus", surname: "Johnson", age: 15},
        {name: "Emily", surname: "Patel", age: 14}
    ]
}
let studentNames=[];
let studentSurnames=[];
let studentAges=[];
for (let i=0; i<school1.students.length; i++){
    studentNames.push(school1.students[i].name)
    studentSurnames.push(school1.students[i].surname)
    studentAges.push(school1.students[i].age)
}
console.log(`
Student1 is ${studentNames[0]} ${studentSurnames[0]} and is ${studentAges[0]} years old. \n
Student2 is ${studentNames[1]} ${studentSurnames[1]} and is ${studentAges[1]} years old. \n
Student3 is ${studentNames[2]} ${studentSurnames[2]} and is ${studentAges[2]} years old. `)

// Another comparison
const school2={
    name: "Tbilisi School",
    students: [
        {name: "Jennifer", surname: "Ramirez", age: 16},
        {name: "Marcus", surname: "Johnson", age: 15},
        {name: "Emily", surname: "Patel", age: 14}
    ]
}
// We can see, that when comparing two objects which have same properties, it always gives negative answer, because no object is same and all of them are unique.
console.log(school1 === school2)

// Object methods - Calculator

const readline = require("readline");

const calculator={
    addition: function(num1, num2){
        console.log(`${num1} + ${num2} = ${num1 + num2}`)
    },
    subtraction: function(num1, num2){
        console.log(`${num1} - ${num2} = ${num1 - num2}`)
    },
    multiplication: function(num1, num2){
        console.log(`${num1} * ${num2} = ${num1 * num2}`)
    },
    division: function(num1, num2){
        console.log(`${num1} / ${num2} = ${num1 / num2}`)
    },
    floorDivision: function(num1, num2){
        console.log(`${num1} // ${num2} = ${Math.floor(num1 / num2)}`)
    },
    modulo: function(num1, num2){
        console.log(`${num1} % ${num2} = ${num1 % num2}`)
    },
    exponentiation: function(num1, num2){
        console.log(`${num1} ** ${num2} = ${num1 ** num2}`)
    },
    absoluteValue: function(num1, num2){
        console.log(`Absolute value for ${num1} is ${Math.abs(num1)} and is ${Math.abs(num2)} for ${num2}`)
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Choose an operation (addition, subtraction, multiplication, division, floorDivision, modulo, exponentiation, absoluteValue): ", function(userChoice) {
    rl.question("Enter the first number: ", function(num1) {
        rl.question("Enter the second number: ", function(num2) {
            num1 = Number(num1);
            num2 = Number(num2);
            if (calculator[userChoice]) {
                calculator[userChoice](num1, num2);
            } else {
                console.log("Invalid operation!");
            }
            rl.close();
        });
    });
});


