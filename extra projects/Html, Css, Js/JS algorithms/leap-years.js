console.log("Hello, this is leap year checker")
const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin, 
    output: process.stdout
})

rl.question("Enter year: ", (year)=>{
    if (year%4==0){
        if (year%100==0){
          if (year%400==0){
            console.log(`${year} is Leap!`)
          } else{
            console.log(`${year} is not leap!`)
          }
        } else{
            console.log(`${year} is Leap!`)
        }
      } else{
        console.log(`${year} is not leap!`)
      }
    rl.close()
})