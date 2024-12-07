// Part1

const events = require("events");
const handler1 = new events.EventEmitter();

handler1.on("registration", (name, surname) => {
    console.log(`Hello ${name} ${surname}!`)
})
handler1.emit("registration", "David", "Tezelashvili")


handler1.on("writeName", name => console.log(name));
handler1.on("writeSurname", surname => console.log(surname));
handler1.on("writeAge", age => console.log(age));
handler1.on("writeEmail", email => console.log(email));
handler1.on("custom", (name, surname, age, email) => {
    handler1.emit("writeName", name);
    handler1.emit("writeSurame", surname);
    handler1.emit("writeAge", age);
    handler1.emit("writeEmail", email);
})
handler1.emit("custom", "David", "Tezelashvili", 20, "datatezelashvili8@gmail.com")

handler1.once("greet", () => console.log("hello"))
handler1.emit("greet")


// Part2

// 1
// process.stdin.on("data", info => {
//     process.stdout.write(`${info}`);
//     process.exit();
// })

// 2
// process.stdin.on("data", info => {
//     const inp = info.toString().trim();
//     if (inp === "r" || inp === "R"){
//         process.exit();
//     }
// })


// 3
// let num1, num2, operator;

// process.stdin.on('data', (input) => {
//   const inputData = input.toString().trim().split(' ');

//   if (inputData.length === 3) {
//     num1 = parseFloat(inputData[0]);
//     operator = inputData[1];
//     num2 = parseFloat(inputData[2]);

//     if (isNaN(num1) || isNaN(num2)) {
//       console.log('Invalid numbers. Please enter valid numeric values.');
//       process.exit();
//     }

//     const result = calculate(num1, num2, operator);
//     console.log(`Result: ${result}`);
//     process.exit();
//   } else {
//     console.log('Invalid input. Please enter two numbers and an operator separated by spaces.');
//   }
// });

// function calculate(num1, num2, operator) {
//   switch (operator) {
//     case '+': return num1 + num2;
//     case '-': return num1 - num2;
//     case '*': return num1 * num2;
//     case '/':
//       if (num2 === 0) {
//         return 'Error: Division by zero';
//       }
//       return num1 / num2;
//     default:
//       return 'Invalid operator';
//   }
// }

// console.log('Enter the calculation (e.g., "3 + 4") and press Enter:');


// 4
// process.stdin.on("data", info => {
//     const input = info.toString().toUpperCase();
//     process.stdout.write(input);
//     process.exit();
// })


// 5
process.stdout.write("Input number to see bar and input 'r' to exit: \n");
process.stdin.on("data", info => {
    const inp = info.toString().trim();

    if (inp === "r") {
        process.exit();
    } else {
        const num = parseInt(inp);
        if (!isNaN(num) && num >= 0) {
            process.stdout.write(`Progress: ${"-".repeat(num)}\n`);
        } else {
            process.stdout.write("Please enter a valid number or 'r' to exit.\n");
        }
    }
});