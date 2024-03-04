console.log("Hello, this code checks if your isbn10 is valid")

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter your Isbn here: ", (isbn)=>{
    let validChars = '0123456789X';
    let isValid = true;
    if (isbn.length !== 10 || isbn.slice(0, 9).includes('X')) {
      isValid = false;
    }
  
    let total = 0;
    let index = 1;
    for (let i = 0; i < isbn.length; i++) {
      if (!validChars.includes(isbn[i])) {
        isValid = false;
        break;
      }
      if (isbn[i] === 'X' && i === 9) {
        total += 10 * index;
      } else {
        total += parseInt(isbn[i]) * index;
      }
      index++;
    }
  
    if (total % 11 !== 0) {
      isValid = false;
    }
  
    if (isValid==true){
        console.log(`${isbn} is Correct!`)
    } else{
        console.log(`${isbn} is not Correct!`)
    }
    rl.close()
})