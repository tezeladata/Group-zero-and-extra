// Multiply
function multiply(a, b){
    return a*b
  }

// Even or Odd
function evenOrOdd(number) {
    if (number%2==0){
      return "Even"
    }
    else{
      return "Odd"
    }
  }

// Convert a Number to a String!
function numberToString(num) {
    return String(num)
  }

// Opposite number
function opposite(number) {
    return number*(-1)
  }

// Reversed Strings
function solution(str){
    let splt= str.split("");
    let rvrs=splt.reverse();
    let ans=rvrs.join("");
    return ans
  }

// Return Negative
function makeNegative(num) {
  if (num>=0){
    return num*(-1)
  }
  else{
    return num
  }
}

// Convert boolean values to strings 'Yes' or 'No'.
function boolToWord( bool ){
  if (bool==true){
    return "Yes"
  }
  else{
    return "No"
  }
}

// Sum of positive
function positiveSum(arr) {
  let sum=0;
  for (let i=0; i<arr.length; i++){
    if (arr[i]>0){
      sum+=arr[i];
    }
  }
  return sum;
}

// String repeat
function repeatStr (n, s) {
  let newStr="";
  let i=0;
  while (i<n){
    newStr+=s;
    i++;
  }
  return newStr;
}

// Remove First and Last Character
function removeChar(str){
  return str.slice(1,-1)
};

// Square(n) Sum
function squareSum(numbers){
  let sum=0;
  for (let i=0; i<numbers.length; i++){
    sum+=(numbers[i])**2;
  }
  return sum;
}

// Grasshopper - Summation
var summation = function (num) {
  let sum=0;
  for (let i=1; i<=num; i++){
    sum+=i;
  }
  return sum;
}

// Function 1 - hello world
let greet=function(){
  return "hello world!"
}

// Convert a String to a Number!
const stringToNumber = function(str){
  return Number(str);
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

// Returning Strings
function greet(name){
  return "Hello, " + name + " how are you doing today?"
}

// Convert a Boolean to a String
function booleanToString(b){
  if (b==true){
    return "true"
  } else{
    return "false"
  }
}

// Keep Hydrated!
function litres(time) {
return (Math.floor(time*0.5));
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

// Century From Year
function century(year) {
  year=Math.floor((year+99) / 100);
  return year;
}

// Convert number to reversed array of digits
function digitize(n) {
newArr=String(n).split("")
res=[]
for (let i=0; i<newArr.length; i++){
  res.push(Number(newArr[i]))
}
return res.reverse()
}

// Beginner - Lost Without a Map
function maps(x){
res=[]
for (let i=0; i<x.length; i++){
  res.push(x[i]*2)
}
return res
}

// Beginner Series #2 Clock
function past(h, m, s){
milisec=h*3600000 + m*60000 + s*1000
return milisec
}

// Opposites Attract
function lovefunc(flower1, flower2){
if (flower1%2==0 && flower2%2!=0){
  return true
} else if (flower1%2!=0 && flower2%2==0){
  return true
} else{
  return false
}
}

// Beginner Series #1 School Paperwork
function paperwork(n, m) {
if (n<0 || m<0){
  res=0
  return res
} else{
  return n*m
}
}

// Abbreviate a Two Word Name
function abbrevName(name){
newArr=name.split(" ");
personName=newArr[0][0].toUpperCase();
personLastName=newArr[1][0].toUpperCase();
return `${personName}.${personLastName}`
}