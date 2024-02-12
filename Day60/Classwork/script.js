// for (let i=0; i<20; i++){
//     if (i==15){
//         console.log("Hello World")
//     } else{
//         console.log(`${i} < 20`)
//     }
// }
let counter=0;
while (true){
    if (counter==20){
        break
    }
    counter++;
    console.log(counter);
}

let num1=1;
while (num1<=100){
    console.log(num1)
    num1++;
}

let age=20;
if (age>15){
    console.log(`${age}>15`)
} else if (age==15){
    console.log(15)
} else{
    console.log(`${age}<15`)
}

console.log(Math.sqrt(-1))

//initialization, condition, updating
for (let i=0; i<10; i++){
    console.log(i)
}