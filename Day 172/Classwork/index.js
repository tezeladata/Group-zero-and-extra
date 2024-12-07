// // new
// const callEvents = new events.EventEmitter();

// // new event
// callEvents.on("call", () => {
//     console.log("call initiated");
// })

// // call event
// callEvents.emit("call")

const events = require("events")

const accounts = []

const authenticationEvents = new events.EventEmitter();
authenticationEvents.on("registration", account => {
    accounts.push(account)

    console.log(accounts)
})

class Account {
    constructor(fisrtname, lastname, email, balance){
        this.fisrtname = fisrtname;
        this.lastname = lastname;
        this.email = email;
        this.balance = balance;
    }

    static createAccount(firstname, lastname, email, balance){
        const account = new Account(firstname, lastname, email, balance);
        authenticationEvents.emit("registration", account)
        return account;
    }
}


// Using this class
const acc1 = Account.createAccount("David", "Tezelashvili", "datatezelashvili8@gmail.com", 2000)


// input, output
console.log(process.stdout)

// process.stdin.on("data", (data) => {
//     process.stdout.write("Please შემოიტანე text")
//     const number = parseInt(data);

//     if (number%2 == 0){
//         process.exit();
//     }
// })


const numbers = [];
process.stdin.on("data", data => {
    const num = parseInt(data);

    if (numbers.length < 9) {
        numbers.push(num)
    } else {
        const lastSum = numbers.reduce((sum, numb) => sum += numb, 0);
        process.stdout.write(`${lastSum}`);

        process.exit();
    }
})