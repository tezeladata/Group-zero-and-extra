console.log("Hello, this code finds divisors of your number!")
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter your Number: ", (integer)=>{
    let divisors = [];
    for (let i = 2; i < integer; i++) {
        if (integer % i === 0) {
            divisors.push(i);
        }
    }
    if (divisors.length > 0) {
        console.log(divisors);
    } else {
        console.log(`${integer} is prime`);
    }
  rl.close()
})