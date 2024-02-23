console.log("Hello, this code gerenaters prime numbers within your limit")
const readline = require("readline")

const generator={
    calculation: function(lowerLimit, upperLimit){
        lowerLimit=parseInt(lowerLimit);
        upperLimit=parseInt(upperLimit);
        let primeNums=[];
        for (let num=lowerLimit; num<=upperLimit; num++){
            let isPrime=true;
            if (num===1){
                isPrime=false
            } else if (num===2){
                isPrime=true
            } else{
                for (let i=2; i<=Math.sqrt(num); i++){
                    if (num%i==0){
                        isPrime=false;
                        break;
                    }
                }
                if (isPrime){
                    primeNums.push(`${num}\n`);
                }
            }
        }
        console.log(primeNums.join(''));
        console.log(`Total items: ${primeNums.length}`)
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.question("Enter lower limit: ", (lowerLimit) => {
    rl.question("enter upper limit: ", (upperLimit) =>{
        generator.calculation(lowerLimit, upperLimit)
        rl.close()
    })
})