console.log("Hello, this code finds greatest common divisor of two numbers");
const readline = require("readline");

const greatestCommonDivisor = {
    calculation: function(num1, num2) {
        const originalNum1 = num1;
        const originalNum2 = num2;
        num1 = Math.abs(parseInt(num1)); 
        num2 = Math.abs(parseInt(num2)); 
        let gcd = num1; 
        while (num2 !== 0) {
            let t = num2;
            num2 = num1 % num2;
            num1 = t;
            gcd = num1;
        }
        console.log(`Greatest common divisor for numbers: ${originalNum1} and ${originalNum2} is ${gcd}`);
    }
};

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter first number: ", (num1) => {
    rl.question("Enter second number: ", (num2) => {
        greatestCommonDivisor.calculation(num1, num2);
        rl.close();
    });
});