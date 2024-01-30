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