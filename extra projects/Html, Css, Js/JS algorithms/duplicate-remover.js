console.log("Hello, this code removes duplicate words from your sentence!")
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter your sentence: ", (s)=>{
    let original=s;
    s=s.split(" ");
    let sentence=[];
    for (let i=0; i<s.length; i++){
        if (! sentence.includes(s[i])){
            sentence.push(s[i])
        }
    }
    if (original==sentence.join(" ")){
        console.log("No duplicates")
    } else{
        console.log(`Modified sentence: ${sentence.join(" ")}`)
    }
    rl.close()
})