const process = require("process")

// 1
console.log(process.argv[0])
console.log(process.argv[1])

// 2
console.log(process.cwd)

// 3
const os = require("os");
console.log(os.platform())
console.log(os.arch())

// 4
console.log(process.memoryUsage())

// 5
console.log(process.env)

// 6
console.log(os.totalmem())
console.log(os.freemem())

// 7
console.log(process.version)

// 8
console.log(process.argv[1])

// 9
console.log(os.arch())

// 10
console.log(os.uptime())
console.log(process.uptime())

// 11
if (process.argv.length >= 5) {
    const num1 = parseFloat(process.argv[2])
    const operator = process.argv[3]
    const num2 = parseFloat(process.argv[4])

    switch (operator) {
        case "+":
            console.log(num1 + num2);
            break;
        case "-":
            console.log(num1 - num2);
            break;
        case "*":
            console.log(num1 * num2);
            break;
        case "/":
            console.log(num1 / num2);
            break;
        case "%":
            console.log(num1 % num2);
            break;
        case "**":
            console.log(num1 ** num2);
            break;
    }
}