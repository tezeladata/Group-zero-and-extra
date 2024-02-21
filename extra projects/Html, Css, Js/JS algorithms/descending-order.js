console.log("Hello, this code write your number in descending order!")
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter your Number: ", (userNum)=>{
    let descended=Number(String(userNum).split("").sort().reverse().join(""));
    console.log(`Descended Number for ${userNum} is ${descended}`)
  rl.close()
})