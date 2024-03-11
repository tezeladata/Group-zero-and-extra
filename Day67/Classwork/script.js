// const date1 = new Date("2024-3-11")
// const date1 = new Date();
// console.log(date1.getFullYear());
// date1.toDateString();
// console.log(date1);
// date1.toString();
// console.log(date1);

// new Date()
// new Date(date string)

// new Date(year,month)
// new Date(year,month,day)
// new Date(year,month,day,hours)
// new Date(year,month,day,hours,minutes)
// new Date(year,month,day,hours,minutes,seconds)
// new Date(year,month,day,hours,minutes,seconds,ms)

// new Date(milliseconds)


// In miliseconds:
// console.log(Date.parse(date1))


// const date1 = new Date();
// console.log(date1.getDate(), date1.getDay(), date1.getFullYear(), date1.getHours(), date1.getMilliseconds(), date1.getMinutes(), date1.getMonth(), date1.getSeconds())
// // setInterval(function(){
// //     const d = new Date();
// //     console.log(d.getMilliseconds())
// // }, 1000)
// console.log(date1.setDate(10), date1.setHours(10), date1.setMonth(4), date1.setMilliseconds(303))


// setInterval(function(){
//     const date1 = new Date();
//     console.log(date1.toString())
// },1000)

// let seconds=0;
// let minutes=0;
// let hours=0;
// let days=0;
// setInterval(function(){
//     seconds++;
//     if (seconds%60==0){
//         minutes++;
//         if (minutes%60==0){
//             hours++;
//             if (hours%24==0){
//                 days++;
//             }
//         }
//     }
//     console.log(days, hours, minutes, seconds)
// }, 1000)


// let user_minutes = 5;
// let user_seconds = 60;
// let combined = 60 + 60*5;

// let intervalSeconds=0;
// setInterval(function(){
//     intervalSeconds++;
//     if (intervalSeconds==combined){
//         clearInterval()
//     }
// }, 1000)


// for (let i=0; i<=10; i++){
//     setTimeout(function(){
//         console.log("David")
//     })
// }


function printTime() {
    var d = new Date();
    var hours = d.getHours();
    var mins = d.getMinutes();
    var secs = d.getSeconds();
    console.log(hours+":"+mins+":"+secs);
  }
  setInterval(printTime, 1000);