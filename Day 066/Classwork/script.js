// const multiplesOfFive = [];
// for (let i=0; i<=100; i++){
//     if (i%5==0){
//         multiplesOfFive.push(i)
//     }
// }
// for (let i=0; i<multiplesOfFive.length; i++){
//     if (multiplesOfFive[i]%10==0 && multiplesOfFive[i] > 0){
//         console.log(`${multiplesOfFive[i]} is a multiple of ten`)
//     }
// }

// 1
const numArr = [1,2,3,4,5,6,7,8,9,10];
for (let i=0; i<numArr.length; i++){
    let num=numArr[i];
    if (num%2==0){
        console.log(`${num} is even.`)
    } else{
        console.log(`${num} is odd.`)
    }
}

// 2
const numArr2 = [1,2,3,4,5,6,7,8,9,10];
const numArr3 = [];
for (let i=0; i<numArr2.length; i++){
    if (numArr2[i]%2==0){
        numArr3.push(numArr2[i])
    }
}
console.log(numArr3)

// 3
const multiplesOfFive = [];
let sum=0;
for (let i=1; i<=100; i++){
    if (i%5==0){
        multiplesOfFive.push(i)
        sum+=i
    }
}

console.log(multiplesOfFive)
console.log(sum)

// 4
const allNums=[];
const squares=[];
const roots=[];
let sumOfNumbers=0;
let productOfNumbers=1;

for (let i=0; i<10; i++){
    let newNum=parseInt(prompt("Enter Number here: "))
    sumOfNumbers+=newNum;
    productOfNumbers*=newNum
    squares.push(newNum**2)
    roots.push(newNum**0.5)
    allNums.push(newNum)
}

// 5
const codeNumbers = [0,1,2,3,4,5,6,7,8,9]
const tickets = [];
const numOfTickets=prompt("Enter how many tickets you want: ")
for (let i=1; i<=numOfTickets; i++){
    const name=prompt(`Enter name for ticket N${i}`);
    const surname=prompt(`Enter surname for ticket N${i}`);
    const age=parseInt(prompt(`Enter surname for ticket N${i}`));
    const ticketCode = generateRandomCode();

    const ticket = new Ticket(name, surname, age, ticketCode);
    tickets.push(ticket);
}
function generateRandomCode() {
    let code = '';
    for (let i = 0; i < 5; i++) {
        const randomIndex = Math.floor(Math.random() * codeNumbers.length);
        code += codeNumbers[randomIndex];
    }
}

function Ticket(name, surname, age, code) {
    this.name = name;
    this.surname = surname;
    this.age = age;
    this.code = code;
}

console.log(tickets)