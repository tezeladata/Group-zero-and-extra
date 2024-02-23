console.log("Hello, this is collatz conjecture or simply 3x+1 calculator")
const readline = require("readline")

const collatzConjecture={
    calculation: function(userNum){
        userNum=parseInt(userNum)
        let originalUserNum=userNum;
        let sequence=[];
        let counter=1;
        while (userNum > 1){
            if (userNum%2==0){
                userNum=Math.floor(userNum / 2)
            } else{
                userNum = userNum * 3 + 1
            }
            sequence.push(`\n${counter} : ${userNum}`)
            counter++;
        }
        console.log(`Collatz conjecture sequence for ${originalUserNum} is \n ${sequence}`)
        console.log(`Total steps needed: ${counter-1}`)
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.question("Enter natural number: ", (userNum) => {
    if (userNum>1){
        collatzConjecture.calculation(userNum);
    } else{
        console.log(`${userNum} is not a natural number!`)
    }
    rl.close()
})