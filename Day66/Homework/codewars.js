// String repeat
function repeatStr (n, s) {
    let resStr="";
      for (let i=0; i<n; i++){
          resStr+=s
      }
      return resStr
  }

// Remove First and Last Character
function removeChar(str){
    let resStr="";
    for (let i=1; i<str.length-1; i++){
      resStr+=str[i]
    }
    return resStr
  };
  
// Reversed Strings
function solution(str){
  let split=str.split("");
  let reverse=split.reverse();
  let join=reverse.join("");
  return join
}

// Opposite number
function opposite(number) {
  return number*-1
}

// Century From Year
function century(year) {
  year=Math.floor((year+99)/100);
  return year
}

// Even or Odd
function evenOrOdd(number) {
  if (number%2==0){
    return "Even"
  } else{
    return "Odd"
  }
}

// Multiply
function multiply(a, b){
  return a * b
}

// Return Negative
function makeNegative(num) {
  if (num<0){
    return num
  } else{
    return num*-1
  }
}

// Counting sheep...
function countSheeps(sheep) {
  let counter=0;
  for (let i=0; i<sheep.length; i++){
    if (sheep[i]==true){
      counter++
    }
  }
  return counter
}

// Find the smallest integer in the array
class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min(...args)
  }
}

// Sum without highest and lowest number
function sumArray(array) {
  if (array && array.length>1){
    let min = Math.min(...array);
    let max = Math.max(...array);
    let sum=0;
    for (let i=0; i<array.length; i++){
      sum+=array[i]
    }
    return sum - (min + max);
  } else{
    return 0
  }
}

// Convert number to reversed array of digits
function digitize(n) {
  let newArr=String(n).split("");
  let res=[];
  for (let i=0; i<newArr.length; i++){
    res.push(Number(newArr[i]))
  }
  return res.reverse()
}

// Remove String Spaces
function noSpace(x){
  let res="";
  for (let i=0; i<x.length; i++){
    if (x[i]!=" "){
      res+=x[i]
    }
  }
  return res
}

// Number of People in the Bus
var number = function(busStops){
  let counter=0;
  for (let i=0; i<busStops.length; i++){
    counter+=busStops[i][0]-busStops[i][1]
  }
  return counter
}

// A Needle in the Haystack
function findNeedle(haystack) {
  const pos=haystack.indexOf("needle");
  return `found the needle at position ${pos}`;
}

// Basic Mathematical Operations
function basicOp(operation, value1, value2){
  if (operation=="+"){
    return value1+value2
  } else if (operation=="-"){
    return value1-value2
  } else if (operation=="*"){
    return value1*value2
  } else if (operation=="/"){
    return value1/value2
  }
}

// Jenny's secret message
function greet(name){
  if(name === "Johnny"){
    return "Hello, my love!";
  } else{
    return "Hello, " + name + "!";
  }
}

// Count of positives / sum of negatives
function countPositivesSumNegatives(input) {
  if (input==[] || !input){
    return []
  } else{
    let countOfPos=0;
    let sumOfNegative=0;
    for (let i=0; i<input.length; i++){
      if (input[i]>0){
        countOfPos+=1
      } else{
        sumOfNegative+=input[i]
      }
    }
    if (countOfPos!=0 || sumOfNegative!=0){
      res=[countOfPos, sumOfNegative]
      return res
    } else{
      return []
    }
  }
}

// Grasshopper - Summation
var summation = function (num) {
  let sum=0;
  for (let i=1; i<=num; i++){
    sum+=i;
  }
  return sum;
}

// Convert boolean values to strings 'Yes' or 'No'.
function boolToWord( bool ){
  if (bool){
    return "Yes"
  }else{
    return "No"
  }
}

// Find Maximum and Minimum Values of a List
var min = function(list){
    
    return Math.min(...list);
}

var max = function(list){
    
    return Math.max(...list);
}

// Invert values
function invert(array) {
   if (array.length==0){
    return []
  } else {
    let newArr=[]
    for (let i=0; i<array.length; i++){
      newArr.push(array[i] * -1)
    }
    return newArr
  }
}

// Double Char
function doubleChar(str) {
    let newStr=""
    for (let i=0; i<str.length; i++){
      newStr+=`${str[i]}${str[i]}`
    }
    return newStr
  }

// Rock Paper Scissors!
const rps = (p1, p2) => {
  if (p1 === "scissors" && p2 === "scissors") {
        return "Draw!";
    } else if (p1 === "paper" && p2 === "paper") {
        return "Draw!";
    } else if (p1 === "rock" && p2 === "rock") {
        return "Draw!";
    } else if (p1 === "rock" && p2 === "paper") {
        return "Player 2 won!";
    } else if (p1 === "paper" && p2 === "scissors") {
        return "Player 2 won!";
    } else if (p1 === "scissors" && p2 === "rock") {
        return "Player 2 won!";
    } else if (p1 === "rock" && p2 === "scissors") {
        return "Player 1 won!";
    } else if (p1 === "paper" && p2 === "rock") {
        return "Player 1 won!";
    } else if (p1 === "scissors" && p2 === "paper") {
        return "Player 1 won!";
    }
};

// Calculate average
function findAverage(array) {
  if (array.length==0){
    return 0
  } else{
    let sum=0
    for (let i=0; i<array.length; i++){
      sum+=array[i]
    }
    return sum/array.length
  }
}

// Convert a Number to a String!
function numberToString(num) {
  return String(num)
}

// Is n divisible by x and y?
function isDivisible(n, x, y) {
  if (n%x==0 && n%y==0){
    return true
  } else{
    return false
  }
}

// Do I get a bonus?
function bonusTime(salary, bonus) {
  if (bonus==true){
    return `£${salary*10}`
  } else{
    return `£${salary}`
  }
}

// Fake Binary
function fakeBin(x){
  newStr=""
  for (let i=0; i<x.length; i++){
    if (Number(x[i])<5){
      newStr+="0"
    } else{
      newStr+="1"
    }
  }
  return newStr
}

// Count by X
function countBy(x, n) {
  let newArr=[];
  for (let i=1; i<n+1; i++){
    b=x*i;
    newArr.push(b)
  }
  return newArr
}

// To square(root) or not to square(root)
function squareOrSquareRoot(arr) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
        var element = arr[i];
        var squareRoot = Math.sqrt(element);
        if (Number.isInteger(squareRoot)) {
            newArr.push(squareRoot);
        } else {
            newArr.push(element * element);
        }
    }
    return newArr;
}

// Reversed sequence
const reverseSeq = n => {
  const newArr = [];
  for (let i = n; i >= 1; i--) {
    newArr.push(i);
  }
  return newArr;
};

// Convert a String to a Number!
const stringToNumber = function(str){
  return Number(str)
}

// Keep Hydrated!
function litres(time) {
  return (Math.floor(time*0.5));
}

// Reversing Words in a String
function reverse(st) {
    const words = st.split(" ");
    return words.reverse().join(" ");
}