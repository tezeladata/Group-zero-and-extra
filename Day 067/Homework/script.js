const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Hw1
setInterval(function(){
    const time = new Date();
    const hour = time.getHours().toString();
    const minute = time.getMinutes().toString();
    const second = time.getSeconds().toString();
    console.log(`${hour} : ${minute} : ${second}`)
}, 1000) // 1000 milliseconds is 1 second


// Hw2
rl.question("Enter radius of your circle: ", (radius) =>{
    radius = parseInt(radius);
    const areaOfCircle = 2 * Math.PI * (radius**2);
    console.log(`Circle which has radius of ${radius} has following area: ${areaOfCircle}`);
    rl.close();
})


// Hw3
rl.question("Enter your camelCase string here: ", (st) => {
    let newStr = "";
    const numbers = "0123456789";
    for (let i = 0; i < st.length; i++) {
        if (st[i] !== st[i].toUpperCase()) {
            newStr += st[i];
        } else if (!numbers.includes(st[i]) && st[i] === st[i].toUpperCase()) {
            newStr += `-${st[i].toLowerCase()}`;
        }
    }
    if (newStr !== "") {
        if (newStr[0] === "-") {
            newStr = newStr.slice(1);
        }
        console.log(`kebabized string for ${st} is ${newStr}`);
    } else {
        console.log("Input string is empty.");
    }
    rl.close();
});


// Hw4
rl.question("Target for how many seconds: ", (seconds) =>{
    let countdown = setInterval(function(){
        seconds--;
        console.log(`${seconds} seconds remaining!`);

        if (seconds == 0){
            console.log("Timer has ended!");
            clearInterval(countdown); // To stop timer
        }
    }, 1000);
    rl.close();
});


// Hw5
rl.question("How many numbers do you want in your Fibonacci sequence: ", (totalNum) =>{
    let sequence = [0, 1]
    let num1 = 0;
    let num2 = 1;
    let num3;
    for (let i=2; i<totalNum; i++){
        num3 = num1 + num2;
        num1 = num2;
        num2 = num3;
        sequence.push(num3)
    }
    console.log(`Fibonacci sequence consisting of ${totalNum} terms is \n${sequence}`)
    rl.close()
})


// Hw6
const currentDate = new Date();
const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

console.log(`Today is ${days[currentDate.getDay()]}!`);


// Hw7
const year = currentDate.getFullYear();
const month = currentDate.getMonth() + 1;
const dayOfMonth = currentDate.getDate(); 

console.log(`Day in three different formats: \n ${dayOfMonth}.${month}.${year} \n ${month}.${dayOfMonth}.${year} \n ${year}.${month}.${dayOfMonth}`);


// Hw8
rl.question("Enter year to check if it's leap or not: ", (user_year) =>{
    if (user_year % 4 == 0){
        if (user_year % 100 == 0){
            if (user_year % 400 == 0){
                console.log(`${user_year} is a leap year!`)
            } else{
                console.log(`${user_year} is not a leap year!`)
            }
        } else{
            console.log(`${user_year} is a leap year!`)
        }
    } else{
        console.log(`${user_year} is not a leap year!`)
    }
    rl.close()
})


// Hw9
console.log("You have to enter date in following format: day.month.year")
rl.question("Enter first date: ", (date1) => {
    rl.question("Enter past date: ", (date2) => {
        let arr1 = date1.split(".");
        let arr2 = date2.split(".");

        let day1 = parseInt(arr1[0]);
        let month1 = parseInt(arr1[1]) - 1; 
        let year1 = parseInt(arr1[2]);
        let day2 = parseInt(arr2[0]);
        let month2 = parseInt(arr2[1]) - 1; 
        let year2 = parseInt(arr2[2]);

        let firstDate = new Date(year1, month1, day1);
        let secondDate = new Date(year2, month2, day2);

        let milisecondDifference = Math.abs(firstDate - secondDate) //It calculates in milliseconds
        let dayDifference = Math.ceil(milisecondDifference / (1000 * 60 * 60 * 24))

        console.log(`The day difference between ${date1} and ${date2} is ${dayDifference}`)

        rl.close()
    })
})


// Hw10
console.log("You have to enter yout birthday date in following format: day.month.year")
rl.question("Enter your birthday here: ", (birthdayDate) => {
    let birthdayArr = birthdayDate.split(".");
    let birthdayDay = parseInt(birthdayArr[0]);
    let birthdayMonth = parseInt(birthdayArr[1]) - 1; 
    let birthdayYear = parseInt(birthdayArr[2]);

    let currentTime = new Date();
    let currentDay = currentTime.getDate(); 
    let currentMonth = currentTime.getMonth();
    let currentYear = currentTime.getFullYear();

    if (birthdayMonth < currentMonth || (birthdayMonth === currentMonth && birthdayDay < currentDay)) {
        console.log(`You are ${currentYear - birthdayYear} years old.`);
    } else if (birthdayDay < currentDay || (birthdayDay === currentDay && birthdayMonth >= currentMonth)) {
        console.log(`You are ${currentYear - birthdayYear - 1} years old.`);
    } else {
        console.log(`You are ${currentYear - birthdayYear - 1} years old.`);
    }
    rl.close();
});